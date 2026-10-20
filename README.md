# MWM Kullanım Rehberi / MWM User Guide

## 📖 Documentation

[MWM documentation](https://hm-info.github.io/mwm_info/)

[English home](https://hm-info.github.io/mwm_info/home-en.html)

[TT / MSC → MWM barkod bilgi sayfası (Türkçe)](https://hm-info.github.io/mwm_info/barcode-tr.html)

[TT / MSC → MWM barcode information (English)](https://hm-info.github.io/mwm_info/barcode-en.html)

MWM kaynak makinelerinde barkod alanları, profil / conta / renk seçimi, ölçüler ve iş listesiyle çalışma hakkında operatör rehberi. Türkçe ve İngilizce sayfalarda PDF indirme bağlantıları bulunur. Mevcut KD658 iş dosyası rehberleri de iki dilde sunulur.

Menü konu bazlıdır: Başlangıç, Barkod rehberi ve İş dosyaları → KD658. Üstteki dil seçimi, açık olan konunun diğer dildeki karşılığına geçer. Mevcut rehber URL'leri korunur. Ana sayfada seçilen dile ait iki rehber kartı yer alır; PDF indirme bağlantıları ilgili rehberin başındadır.

Dokümanlar `docs/` altındadır. Yerel kontrol: `pip install -r requirements.txt` ardından `mkdocs build --strict`. PDF üretimi için sistemde Pango, HarfBuzz ve DejaVu fontları bulunmalıdır; Ubuntu paketleri yayın iş akışında listelenmiştir. PDF dosyaları aynı sayfa içeriğinden her yayında otomatik üretilir. `main` dalına gönderim GitHub Pages yayını oluşturur.
