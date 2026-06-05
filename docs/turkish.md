# MWM HMI Arayüzü — KD658 Barkod Okuyucu ve İş Dosyası

KD658 barkod okuyucu, MWM HMI üzerinde iki farklı çalışma modunda kullanılır: **iş dosyası ile** ve **iş dosyasız**.

## İş dosyası ile çalışırken

İş dosyası (batch dosyası) yüklüyken barkod tarandığında, barkod içeriğinde **N karakterinin ardından gelen 3 hane** yeterlidir. HMI, bu numarayı iş dosyasındaki satırla eşleştirir ve satırdaki tüm üretim verisini kullanır.

Örnek iş dosyası satırları (`batch_test_1.txt`):

```
N000KStandard  P00001F001X06780Y07490Z00000C1717171700S001
N001KStandard  P00001F002X06780Y07490Z00000C1717171700S001
N002KStandard  P00001F003X06780Y07490Z00000C1717171700S001
```

Bu örnekte `N000`, `N001`, `N002` gibi liste numaraları barkod tarandığında eşleşme anahtarı olarak kullanılır.

### İş dosyası satır formatı (KD6xx)

Her satır, sabit başlık karakterleriyle ayrılmış alanlardan oluşur. Alan tanımları `KD6xx_BathcFile_Desc.xlsx` dosyasına göredir:

| Karakter | Başlık | Boyut | Tip | Açıklama |
|----------|--------|-------|-----|----------|
| N | Liste numarası | N + 3 karakter | Sayısal | Barkod eşleşmesinde kullanılan sıra numarası |
| K | Profil kodu | K + 10 karakter | Metin | Profil tanımı (ör. `Standard`, `Profiles01`) |
| P | BIN / Trolley numarası | P + 5 karakter | Sayısal | Palet veya trolley numarası |
| F | Pencere numarası | F + 3 karakter | Sayısal | Pencere sıra numarası |
| X | Çerçeve X değeri | X + 5 karakter | Sayısal | Beşinci karakter ondalık basamağıdır. Örn. `15005` = 1500,5 |
| Y | Çerçeve Y değeri | Y + 5 karakter | Sayısal | Beşinci karakter ondalık basamağıdır. Örn. `15005` = 1500,5 |
| Z | Kullanılmıyor | Z + 5 karakter | Metin | Rezerve alan |
| C | Operatör bilgisi | C + 10 karakter | Metin | Operatör için ek bilgi |
| S | Adet | S + 3 karakter | Sayısal | Üretim adedi |

**Örnek satır (xlsx):**

```
N000KProfiles01P00001F001X06780Y07490Z00000C1717171700S001
```

**İş dosyası örneği ----->>>** [batch_test_1.txt](./batch_test_1.txt)

## İş dosyasız modda

İş dosyası yüklü değilken barkod verisi doğrudan taranan string üzerinden ayrıştırılır. Gerekli alanlar MWM HMI **Load Barcode** ekranından tanımlanır.

![KD658 Load Barcode ekranı](./images/kd658-load-barcode.png)

### Load Barcode ayarları

| Alan | First (Başlangıç) | Last / End (Uzunluk) | Açıklama |
|------|-------------------|----------------------|----------|
| Barcode ID | 1 | — | Barkod tanım kimliği |
| Barcode Length | 31 | — | Barkod toplam karakter uzunluğu |
| Stan | 0 | 1 | İstasyon bilgisi |
| Prof | 5 | 12 | Profil kodu |
| Color | 17 | 2 | Renk kodu |
| X | 20 | 6 | X koordinatı |
| Y | 26 | 5 | Y koordinatı |
| Special first | — | — | Özel alan başlangıcı (isteğe bağlı) |
| Special end | — | — | Özel alan uzunluğu (isteğe bağlı) |

**First** değeri alanın barkod içindeki başlangıç konumunu, **Last / End** değeri ise alanın karakter uzunluğunu belirtir.

İş dosyasız modda taranan 31 karakterlik barkod, yukarıdaki konum ve uzunluklara göre Stan, Prof, Color, X ve Y alanlarına ayrıştırılır.
