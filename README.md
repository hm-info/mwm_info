# MWM Hmi Manual

## 📖 Documentation

[MWM documentation](https://hm-info.github.io/mwm_info/)

[TT / MSC → MWM barkod bilgi sayfası (Türkçe)](https://hm-info.github.io/mwm_info/barcode-tr.html)

[TT / MSC → MWM barcode information (English)](https://hm-info.github.io/mwm_info/barcode-en.html)

MWM kaynak makinelerinde barkod alanları, profil / conta / renk seçimi, ölçüler ve iş listesiyle çalışma hakkında operatör rehberi. Türkçe ve İngilizce sayfalarda PDF indirme bağlantıları bulunur. Mevcut KD658 iş dosyası rehberleri de iki dilde sunulur.

Dokümanlar `docs/` altındadır. Yerel kontrol: `pip install -r requirements.txt` ardından `mkdocs build --strict`. PDF üretimi için sistemde Pango, HarfBuzz ve DejaVu fontları bulunmalıdır; Ubuntu paketleri yayın iş akışında listelenmiştir. PDF dosyaları aynı sayfa içeriğinden her yayında otomatik üretilir. `main` dalına gönderim GitHub Pages yayını oluşturur.
