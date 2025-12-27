# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'proje_arayuz.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSlider,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"/* --- GENEL AYARLAR --- */\n"
"QMainWindow, QWidget {\n"
"    background-color: #1e1e1e; /* K\u00f6m\u00fcr Grisi Arka Plan */\n"
"    color: white;\n"
"}\n"
"\n"
"/* --- GRUP KUTUSU (\u00c7er\u00e7eve) --- */\n"
"QGroupBox {\n"
"    border: 2px solid #00aaff; /* Neon Mavi \u00c7er\u00e7eve */\n"
"    border-radius: 6px;\n"
"    margin-top: 20px;\n"
"    font-weight: bold;\n"
"    color: #00aaff;\n"
"}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 5px;\n"
"}\n"
"\n"
"/* --- BUTONLAR (Mavi ve S\u0131\u011facak \u015eekilde) --- */\n"
"QPushButton {\n"
"    background-color: #005bb5;\n"
"    border: 1px solid #004c99;\n"
"    color: white;\n"
"    padding: 4px; /* Yaz\u0131lar s\u0131\u011fs\u0131n diye bo\u015flu\u011fu azaltt\u0131k */\n"
"    border-radius: 5px;\n"
"    font-size: 10px;\n"
"    font-weight: bold;\n"
"    min-height: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0077ea; /* Parlak Mavi */\n"
"    border: 1px solid #00aaff"
                        ";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #003366; /* Koyu Mavi */\n"
"    border: 1px solid #002244;\n"
"}\n"
"\n"
"/* --- SLIDER \u00d6ZEL TASARIMI (MAV\u0130) --- */\n"
"\n"
"/* 1. Kanal (Slider'\u0131n \u00fczerinde gitti\u011fi yol) */\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #333;\n"
"    height: 8px; /* Yolun kal\u0131nl\u0131\u011f\u0131 */\n"
"    background: #222; /* Yolun rengi (Koyu) */\n"
"    margin: 2px 0;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* 2. Topuz (Tuttu\u011fumuz k\u0131s\u0131m) */\n"
"QSlider::handle:horizontal {\n"
"    background: #00aaff; /* Parlak Neon Mavi */\n"
"    border: 1px solid #00aaff;\n"
"    width: 18px; /* Topuzun geni\u015fli\u011fi */\n"
"    height: 18px;\n"
"    margin: -7px 0; /* Ortalamak i\u00e7in */\n"
"    border-radius: 9px; /* Yuvarlak olmas\u0131 i\u00e7in */\n"
"}\n"
"\n"
"/* 3. Dolan K\u0131s\u0131m (Solda kalan alan) */\n"
"QSlider::sub-page:horizontal {\n"
"    background: #005bb5; /* Butonlarla ayn\u0131 ma"
                        "vi */\n"
"    border-radius: 4px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: #1e1e1e;\n"
"color: white;")
        self.label_video = QLabel(self.centralwidget)
        self.label_video.setObjectName(u"label_video")
        self.label_video.setGeometry(QRect(0, 0, 640, 430))
        self.label_video.setMinimumSize(QSize(640, 430))
        self.label_video.setStyleSheet(u"background-color: black; border: 3px solid #444;")
        self.label_video.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(660, 20, 121, 451))
        self.btn_roi_oynat = QPushButton(self.groupBox)
        self.btn_roi_oynat.setObjectName(u"btn_roi_oynat")
        self.btn_roi_oynat.setGeometry(QRect(0, 100, 121, 35))
        self.btn_ters = QPushButton(self.groupBox)
        self.btn_ters.setObjectName(u"btn_ters")
        self.btn_ters.setGeometry(QRect(0, 160, 121, 35))
        self.btn_kesit = QPushButton(self.groupBox)
        self.btn_kesit.setObjectName(u"btn_kesit")
        self.btn_kesit.setGeometry(QRect(0, 220, 121, 35))
        self.btn_sahne = QPushButton(self.groupBox)
        self.btn_sahne.setObjectName(u"btn_sahne")
        self.btn_sahne.setGeometry(QRect(0, 280, 121, 35))
        self.btn_blur = QPushButton(self.groupBox)
        self.btn_blur.setObjectName(u"btn_blur")
        self.btn_blur.setGeometry(QRect(0, 340, 121, 35))
        self.btn_yukle = QPushButton(self.groupBox)
        self.btn_yukle.setObjectName(u"btn_yukle")
        self.btn_yukle.setGeometry(QRect(0, 40, 121, 35))
        self.btn_sb = QPushButton(self.groupBox)
        self.btn_sb.setObjectName(u"btn_sb")
        self.btn_sb.setGeometry(QRect(0, 400, 121, 35))
        self.slider_hiz = QSlider(self.centralwidget)
        self.slider_hiz.setObjectName(u"slider_hiz")
        self.slider_hiz.setGeometry(QRect(30, 450, 301, 16))
        self.slider_hiz.setMinimumSize(QSize(0, 0))
        self.slider_hiz.setMinimum(1)
        self.slider_hiz.setMaximum(100)
        self.slider_hiz.setValue(30)
        self.slider_hiz.setOrientation(Qt.Orientation.Horizontal)
        self.slider_r = QSlider(self.centralwidget)
        self.slider_r.setObjectName(u"slider_r")
        self.slider_r.setGeometry(QRect(360, 450, 271, 16))
        self.slider_r.setMaximum(255)
        self.slider_r.setOrientation(Qt.Orientation.Horizontal)
        self.hiz_ayari = QLabel(self.centralwidget)
        self.hiz_ayari.setObjectName(u"hiz_ayari")
        self.hiz_ayari.setGeometry(QRect(120, 480, 101, 31))
        self.hiz_ayari.setMinimumSize(QSize(50, 20))
        self.slider_g = QSlider(self.centralwidget)
        self.slider_g.setObjectName(u"slider_g")
        self.slider_g.setGeometry(QRect(360, 480, 271, 16))
        self.slider_g.setMaximum(255)
        self.slider_g.setOrientation(Qt.Orientation.Horizontal)
        self.slider_b = QSlider(self.centralwidget)
        self.slider_b.setObjectName(u"slider_b")
        self.slider_b.setGeometry(QRect(360, 510, 271, 16))
        self.slider_b.setMaximum(255)
        self.slider_b.setOrientation(Qt.Orientation.Horizontal)
        MainWindow.setCentralWidget(self.centralwidget)
        self.label_video.raise_()
        self.slider_hiz.raise_()
        self.slider_r.raise_()
        self.hiz_ayari.raise_()
        self.slider_g.raise_()
        self.slider_b.raise_()
        self.groupBox.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_video.setText(QCoreApplication.translate("MainWindow", u"BA\u015eLAMAK \u0130\u00c7\u0130N V\u0130DEO Y\u00dcKLEY\u0130N", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"KONTROL KONSOLU", None))
        self.btn_roi_oynat.setText(QCoreApplication.translate("MainWindow", u"SE\u00c7\u0130L\u0130 ALANI OYNAT", None))
        self.btn_ters.setText(QCoreApplication.translate("MainWindow", u"TERS AKI\u015e MODU", None))
        self.btn_kesit.setText(QCoreApplication.translate("MainWindow", u"ARALIK ANAL\u0130Z\u0130", None))
        self.btn_sahne.setText(QCoreApplication.translate("MainWindow", u"HAREKET ALGILAMA", None))
        self.btn_blur.setText(QCoreApplication.translate("MainWindow", u"Y\u00dcZLER\u0130 G\u0130ZLE", None))
        self.btn_yukle.setText(QCoreApplication.translate("MainWindow", u"V\u0130DEO KAYNA\u011eI SE\u00c7", None))
        self.btn_sb.setText(QCoreApplication.translate("MainWindow", u"GR\u0130 TONLAMA", None))
        self.hiz_ayari.setText(QCoreApplication.translate("MainWindow", u"OYNATMA HIZI", None))
    # retranslateUi

