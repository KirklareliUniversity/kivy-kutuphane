# Kivy Dokunmatik Çizim Uygulaması

Bu proje, **Python** ve **Kivy Framework** kullanılarak geliştirilmiş,
dokunmatik ekran ve fare desteğine sahip, kullanıcı dostu bir
**çizim uygulamasıdır**.

Uygulama; temel çizim ihtiyaçlarını karşılayacak şekilde tasarlanmış olup,
renk seçimi, fırça kalınlığı ayarı ve çizim alanını temizleme gibi işlevler
sunar. Basit, anlaşılır ve mobil uyumlu bir arayüze sahiptir.

## Uygulama Özellikleri

- Fare veya dokunmatik ekran ile serbest çizim
- Renk seçimi:
- Siyah
- Kırmızı
- Mavi
- Yeşil
- Ayarlanabilir fırça kalınlığı
- Tek tuş ile çizim alanını temizleme
- Masaüstü ve mobil cihazlara uyumlu arayüz
- Basit ve kullanıcı odaklı tasarım

## Kullanılan Teknolojiler

- **Python 3.11**
- **Kivy 2.3.1**
- **Kivy KV Language**
- **Virtual Environment (venv)**

---

## Proje Yapısı

dokunmatik_cizim/
│
├── main.py
│ └─ Uygulamanın ana çalışma dosyası
│
├── dokunmatikcizim.kv
│ └─ Arayüz tasarımının tanımlandığı KV dosyası
│
├── venv/
│ └─ Python sanal ortam klasörü
│
└── README.md
└─ Proje açıklama dosyası

---

## Kurulum

### 1️ Proje klasörüne gir

```bash
cd dokunmatik_cizim
python -m venv venv
venv\Scripts\activate.bat
pip install kivy
python main.py


## Kullanım

Çizim alanına fare veya parmak ile çizim yapılır

Alt bölümde bulunan renk butonları ile fırça rengi seçilir

Kaydırma çubuğu ile fırça kalınlığı ayarlanır

Temizle butonu ile tüm çizimler silinir
## Amaç ve Kullanım Alanı

Bu proje, Kivy Framework’ünü öğrenmek,
dokunmatik arayüz mantığını kavramak ve
Python ile görsel uygulama geliştirme pratiği kazanmak
amacıyla hazırlanmıştır.

Eğitim ve akademik çalışmalar için uygundur.
```
