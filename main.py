import sys
import cv2
import numpy as np
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel, QMessageBox
from PySide6.QtCore import QTimer, Qt, QRect
from PySide6.QtGui import QImage, QPixmap, QPainter, QPen, QColor

# Tasarım dosyanı çağırıyoruz
from proje_arayuz import Ui_MainWindow

# --- 1. GELİŞMİŞ SMART LABEL ---
class SmartLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.start_point = None
        self.end_point = None
        self.is_drawing = False
        self.selected_roi = None 
        self.draw_visible = True # Kutunun görünüp görünmeyeceğini kontrol eder
        self.setMouseTracking(True)
        self.setCursor(Qt.CrossCursor) 
        self.setText("SİSTEM HAZIR\nLÜTFEN VİDEO KAYNAĞI SEÇİN")
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("color: #aaaaaa; font-weight: bold; font-size: 14px; border: 2px solid #00aaff;")

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.start_point = event.position().toPoint()
            self.end_point = self.start_point
            self.is_drawing = True
            self.selected_roi = None 
            self.draw_visible = True # Yeni çizim yaparken görünür yap

        elif event.button() == Qt.RightButton:
            self.clear_selection()

    def mouseMoveEvent(self, event):
        if self.is_drawing:
            self.end_point = event.position().toPoint()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.is_drawing = False
            self.end_point = event.position().toPoint()
            x = min(self.start_point.x(), self.end_point.x())
            y = min(self.start_point.y(), self.end_point.y())
            w = abs(self.start_point.x() - self.end_point.x())
            h = abs(self.start_point.y() - self.end_point.y())
            if w > 10 and h > 10:
                self.selected_roi = (x, y, w, h)
            self.update()
    
    def clear_selection(self):
        self.selected_roi = None
        self.start_point = None
        self.update()

    def set_drawing_visible(self, status):
        """Kutuyu gizlemek veya göstermek için"""
        self.draw_visible = status
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        # Eğer draw_visible False ise çizim yapma (Kutu gizlenir)
        if not self.draw_visible: return 

        if (self.is_drawing and self.start_point) or self.selected_roi:
            painter = QPainter(self)
            painter.setPen(QPen(QColor(0, 255, 0), 2, Qt.SolidLine))
            
            if self.is_drawing:
                painter.drawRect(QRect(self.start_point, self.end_point))
            elif self.selected_roi:
                painter.drawRect(self.selected_roi[0], self.selected_roi[1], 
                               self.selected_roi[2], self.selected_roi[3])
                painter.drawText(self.selected_roi[0], self.selected_roi[1]-5, "HEDEF")

# --- 2. ANA UYGULAMA ---
class FinalApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Defense Vision System - Final")

        self.old_label = self.ui.label_video
        self.video_screen = SmartLabel(self.old_label.parent())
        self.video_screen.setGeometry(self.old_label.geometry())
        self.video_screen.setStyleSheet(self.old_label.styleSheet())
        self.old_label.hide()

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.all_frames = [] 
        self.current_frame_index = 0
        self.fps = 30.0
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        self.active_mode = "normal"
        self.prev_gray = None
        self.interval_range = (0, 0)

        # Butonlar
        self.ui.btn_yukle.clicked.connect(self.load_video)
        self.ui.btn_roi_oynat.clicked.connect(lambda: self.set_mode("roi"))
        self.ui.btn_ters.clicked.connect(lambda: self.set_mode("reverse"))
        self.ui.btn_kesit.clicked.connect(lambda: self.set_mode("interval"))
        self.ui.btn_sahne.clicked.connect(lambda: self.set_mode("scene"))
        self.ui.btn_blur.clicked.connect(lambda: self.set_mode("blur"))
        self.ui.btn_sb.clicked.connect(lambda: self.set_mode("bw"))

        if hasattr(self.ui, 'slider_hiz'):
            self.ui.slider_hiz.valueChanged.connect(self.update_speed)

    def load_video(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Video Seç")
        if file_path:
            self.ui.label_video.setText("YÜKLENİYOR...")
            QApplication.processEvents()
            
            cap = cv2.VideoCapture(file_path)
            self.fps = cap.get(cv2.CAP_PROP_FPS)
            if self.fps <= 0 or np.isnan(self.fps): self.fps = 30.0 
            
            self.all_frames = []
            while True:
                ret, frame = cap.read()
                if not ret: break
                frame = cv2.resize(frame, (640, 480))
                self.all_frames.append(frame)
            cap.release()
            
            if not self.all_frames:
                QMessageBox.warning(self, "Hata", "Video okunamadı!")
                return
            
            self.current_frame_index = 0
            start_f = int(10 * self.fps)
            end_f = int(30 * self.fps)
            if start_f >= len(self.all_frames): start_f = 0
            if end_f >= len(self.all_frames): end_f = len(self.all_frames) - 1
            self.interval_range = (start_f, end_f)
            
            self.timer.start(int(1000/30))
            self.set_mode("normal")

    def update_speed(self):
        val = self.ui.slider_hiz.value()
        self.timer.setInterval(val)

    # --- MOD YÖNETİCİSİ ---
    def set_mode(self, mode):
        # 1. Mod değişirken temizlik yap
        self.prev_gray = None 
        
        # Eğer ROI moduna giriyorsak kutuyu gizle (İSTEĞİN BU)
        # Eğer ROI'den çıkıyorsak kutuyu tekrar görünür yap (Çizim için)
        if mode == "roi":
            self.video_screen.set_drawing_visible(False)
        else:
            self.video_screen.set_drawing_visible(True)
            if mode != "roi": # ROI hariç diğerlerinde seçimi sil
                self.video_screen.clear_selection()

        # 2. Modu Aktifleştir
        if self.active_mode == mode:
            self.active_mode = "normal"
        else:
            self.active_mode = mode

            if mode == "interval":
                self.current_frame_index = self.interval_range[0]
            elif mode == "roi" and not self.video_screen.selected_roi:
                 QMessageBox.information(self, "Bilgi", "Lütfen önce ekranda mouse ile bir kutu çizin.")
                 self.active_mode = "normal"
                 self.video_screen.set_drawing_visible(True)

    # --- GÖRÜNTÜ MOTORU ---
    def update_frame(self):
        if not self.all_frames: return

        # KARE SEÇİMİ
        if self.active_mode == "interval":
            self.current_frame_index += 1
            if self.current_frame_index >= self.interval_range[1]:
                self.current_frame_index = self.interval_range[0]
        elif self.active_mode == "reverse":
            self.current_frame_index -= 1
            if self.current_frame_index < 0:
                self.current_frame_index = len(self.all_frames) - 1
        else:
            self.current_frame_index += 1
            if self.current_frame_index >= len(self.all_frames):
                self.current_frame_index = 0

        frame = self.all_frames[self.current_frame_index].copy()

        # --- EFEKTLER ---

        # 1. ROI ZOOM (Kutu artık gizli, sadece zoom var)
        if self.active_mode == "roi" and self.video_screen.selected_roi:
            x, y, w, h = self.video_screen.selected_roi
            roi_cut = frame[y:y+h, x:x+w]
            if roi_cut.size > 0:
                frame = cv2.resize(roi_cut, (640, 480))
                cv2.putText(frame, "ODAKLANILDI", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # 2. SAHNE TESPİTİ (HASSASİYET DÜZELTİLDİ)
        elif self.active_mode == "scene":
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray = cv2.GaussianBlur(gray, (21, 21), 0)
            
            if self.prev_gray is not None:
                # İki kare arasındaki farkı al
                diff = cv2.absdiff(self.prev_gray, gray)
                # Fark görüntüsünü siyaha/beyaza çevir (Threshold)
                _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
                
                # Beyaz piksel sayısı (Değişim miktarı)
                change_count = np.sum(thresh > 0)
                
                # Eğer değişim 500 pikselden fazlaysa (Hassasiyet)
                if change_count > 500:
                    cv2.rectangle(frame, (0, 0), (640, 480), (0, 0, 255), 10) # Ekranı kırmızı çerçeveye al
                    cv2.putText(frame, "ALARM: HAREKET!", (150, 240), 
                                cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 3)
                else:
                    cv2.putText(frame, "IZLENIYOR...", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            
            self.prev_gray = gray # Hafızayı güncelle
        # 3. BLUR
        elif self.active_mode == "blur":
            gray_f = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray_f, 1.1, 4)
            for (fx, fy, fw, fh) in faces:
                roi = frame[fy:fy+fh, fx:fx+fw]
                roi = cv2.GaussianBlur(roi, (51, 51), 30)
                frame[fy:fy+fh, fx:fx+fw] = roi

        # 4. SİYAH BEYAZ
        elif self.active_mode == "bw":
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)

        # 5. RGB (Sliderlar bağlı)
        try:
            r = self.ui.slider_r.value()
            g = self.ui.slider_g.value()
            b = self.ui.slider_b.value()
            if r > 0 or g > 0 or b > 0:
                color_layer = np.zeros_like(frame)
                color_layer[:] = (b, g, r)
                frame = cv2.addWeighted(frame, 1.0, color_layer, 0.3, 0)
        except: pass

        # Bilgi Yazıları
        if self.active_mode == "interval":
            cv2.putText(frame, "10-30 SN DONGUSU", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
        elif self.active_mode == "reverse":
            cv2.putText(frame, "<< GERI SARIYOR", (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_frame.shape
        qt_image = QImage(rgb_frame.data, w, h, ch * w, QImage.Format_RGB888)
        self.video_screen.setPixmap(QPixmap.fromImage(qt_image))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FinalApp()
    window.show()
    sys.exit(app.exec())