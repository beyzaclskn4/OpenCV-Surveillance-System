# OpenCV Gözetim Sistemi (Surveillance System)

Bu proje,taktiksel gözetim sistemleri için geliştirilmiş, **Python** ve **OpenCV** tabanlı bir video analiz arayüzüdür. Kullanıcı dostu **PySide6 (Qt)** arayüzü ile operatöre gelişmiş görüntü işleme yetenekleri sunar.

## 🚀 Özellikler

Sistem, gerçek zamanlı video işleme üzerine 7 temel modül içerir:

- **🎯 ROI Odaklanma (Target Zoom):** Mouse ile seçilen hedef alanı (Region of Interest) kesip tam ekrana yansıtır.
- **⚠️ Hareket Algılama (Motion Detection):** Sahne değişimlerini ve ani hareketleri algılayarak operatörü görsel olarak uyarır (Kırmızı Çerçeve Alarmı).
- **🕵️ Gizlilik Modu (Face Blur):** Haar Cascade algoritması ile yüzleri otomatik tespit eder ve sansürler (Mozaikleme).
- **⚫⚪ Siyah Beyaz (Monochrome):** Görüntüyü anlık olarak gri tonlamalı (Grayscale) formata çevirir.
- **⏱️ Taktiksel Döngü (10-30s):** Videonun kritik 10. ve 30. saniyeleri arasında otomatik devriye döngüsü sağlar.
- **⏪ Ters Akış (Reverse Play):** Görüntü akışını kare kare geriye sarar.
- **🎨 RGB & Hız Kontrolü:** Görüntü kanallarına (Kırmızı-Yeşil-Mavi) müdahale imkanı ve oynatma hızı ayarı.

## 🛠️ Kurulum

Projeyi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyin:

1. **Gereksinimleri Yükleyin:**
   ```bash
   pip install -r requirements.txt