# MWM Kaynak Makineleri — Barkod Bilgi Sayfası

TT kesim makinesinden veya MSC_V2X arayüzlü bir kesim merkezinden gelen etiket, kaynak makinesine **profil seçimi ve çerçeve ölçülerini** taşıyabilir. MWM_V3, barkodu makinede kayıtlı alan tanımına göre okur; profilin kaynak parametrelerini makinenin kendi reçetesinden yükler.

Bu sayfa **MWM_V3 kullanan kaynak makineleri serisi** içindir. Alan konumları evrensel ve sabit değildir: aşağıdaki ayarlar, verilen **31 karakterlik TT örneği** içindir. MSC etiketinde aynı veri düzeni varsa aynı tanım kullanılabilir; farklı düzende ayrı tanım gerekir. Önceki MWM sürümleri için aynı davranış ayrıca doğrulanmalıdır.

## 1. Etikette ne görüyoruz?

![TT örnek etiketi: program, araba, pozisyon, işlem, montaj, yer, boy, çerçeve, profil, bayi ve müşteri bilgileri](images/tt-sample-label.png)

Etiketin üzerindeki okunabilir yazılar ile **çizgilerin kodladığı barkod metni** farklı şeylerdir. MWM, fotoğraftaki yazıları okumaz; okuyucunun gönderdiği metni işler. Yukarıdaki fotoğraf etiket düzenini gösterir; aşağıdaki 2894 × 1994 mm örneğiyle aynı ölçülere sahip değildir.

| İşaret | Etiket bilgisi | MWM açısından anlamı |
|---|---|---|
| 1a | Prog No — program numarası | Etiket takibi; aşağıdaki doğrudan okuma örneğinde kaynak programını seçen alan değildir. |
| 1b | Car No / Araba No | Taşıma arabası takibi. Örnek barkodda da bulunur. |
| 1c | POZ No | Pozisyon takibi; örnek 31 karakterlik barkodda ayrı bir POZ alanı yoktur. |
| 1d | İşlem bilgisi | Kesim / işleme operasyonunun açıklaması; doğrudan kaynak reçetesi seçmez. |
| 1e | Montaj yönü — üst, sağ, alt, sol | Parçanın çerçevedeki konumu; örnek barkodda ayrı alan olarak taşınmaz. |
| 1f | LOC / Yer No | Araba içindeki göz / kutu numarası. Örnek barkodda da bulunur. |
| 1g | Value / Parça boyu | Kesilen tek parçanın boyu. Etikette yazan bu değer ile kaynak çerçevesi ölçüsünü karıştırmayın. |
| 1h | Frame / Çerçeve | Etiketteki çerçeve ölçüsü. MWM'ye gelen ölçü, barkod içindeki X/Y alanlarından alınır. |
| 1i | Profil kodu | Conta ve renk koduyla birlikte makinedeki profil reçetesinin bulunmasında kullanılır. |
| 1j | Vendor / Bayi | Sipariş takibi; örnek doğrudan okuma akışında kullanılmaz. |
| 1k | Client / Müşteri / Sipariş | Sipariş takibi; örnek doğrudan okuma akışında kullanılmaz. |

TT etiketindeki yazıların batch dosyasındaki sütun karşılıkları için [TT barkod etiket açıklaması](https://hm-info.github.io/tt-barcode/Turkish) sayfasına bakın. Buradaki rehber, kaynak makinesinin gelen veriyi nasıl kullandığını açıklar.

## 2. Örnek barkodun alanları

**Okuyucudan gelen metin — toplam 31 karakter:**

```text
K1001PROFILE CODE01289400199400
```

**Alanlara ayrılmış gösterim:** Dikey çizgiler yalnızca açıklama içindir, barkoda eklenmez. `PROFILE CODE` içindeki boşluk ise gerçek karakterdir.

```text
K | 1 | 001 | PROFILE CODE | 0 | 1 | 28940 | 0 | 19940 | 0
```

| Karakter sırası (1'den) | Başlangıç (0'dan) | Uzunluk | Örnek | Anlamı / kullanımı |
|---|---:|---:|---|---|
| 1 | 0 | 1 | `K` | Başlangıç karakteri. Okuyucu girişi varsayılan olarak K ile başlar. |
| 2 | 1 | 1 | `1` | Araba numarası; doğrudan reçete okuma akışında kullanılmaz. |
| 3–5 | 2 | 3 | `001` | Göz / kutu numarası; doğrudan reçete okuma akışında kullanılmaz. |
| 6–17 | 5 | 12 | `PROFILE CODE` | Profil kodu. Boşluklar da uzunluğa dahildir. |
| 18 | 17 | 1 | `0` | Conta bilgisi: TT örneğinde 0 = yok, 1 = var. |
| 19 | 18 | 1 | `1` | Renk bilgisi. MWM, conta hanesiyle birlikte okur: burada `01`. |
| 20–24 | 19 | 5 | `28940` | İlk kenar: TT açıklamasında 2894,0 mm. |
| 25 | 24 | 1 | `0` | TT formatının sabit hanesi; aşağıdaki MWM ayarında X alanına dahil edilir. |
| 26–30 | 25 | 5 | `19940` | Diğer kenar: TT açıklamasında 1994,0 mm. |
| 31 | 30 | 1 | `0` | TT formatının sabit hanesi; aşağıdaki MWM ayarında Y alanına dahil edilir. |

**Etikette bulunması, bir alanın MWM tarafından kullanıldığı anlamına gelmez.** Bu örnekte doğrudan kaynak verisi okurken kullanılan ana alanlar profil, conta + renk, X ve Y'dir.

### Conta ve renk nasıl kullanılır?

TT referansında renk için `1 = beyaz`, `2 = alt renkli`, `3 = üst renkli` açıklamaları vardır. Aynı referans çift renk için de `3` yazdığı için bu son değeri kesin bir kod olarak kabul etmeyin; üretici etiket tanımında doğrulayın.

MWM_V3 bu rakamları tek başına sabit bir renk tablosu olarak yorumlamaz. **12 karakter profil + 2 karakter conta/renk** birleştirilir ve profil reçetesi aranır:

```text
Profil       : PROFILE CODE
Conta + renk : 01
Reçete ProfID: PROFILE CODE01
```

Bu anahtarla eşleşen profil tanımı makinede bulunmalıdır. Conta, alt/üst renk, conta baskısı gibi gerçek üretim seçenekleri de bulunan profil reçetesinden gelir. Aynı profilin farklı conta/renk kombinasyonları için uygun reçeteleri tanımlayın.

## 3. MWM'de barkod tanımı

Barkod tanım ekranında **First / Start, 0 tabanlı başlangıç konumudur**. **Last / End / Stop ise okunacak karakter sayısıdır; bitiş konumu değildir.** Örneğin başlangıç 5, uzunluk 12 → 6–17. karakterler.

Bu örnek için **doğrudan okuma / manuel ekran** tanımı:

| Ayar | Başlangıç (First / Start) | Karakter sayısı (Last / End / Stop) | Okunan veri |
|---|---:|---:|---|
| Barcode Length | — | **31** | Sonlandırıcı Enter hariç toplam uzunluk |
| Stan | 0 | 1 | `K` |
| Prof | 5 | 12 | `PROFILE CODE` |
| Color | 17 | 2 | `01` — conta ve renk birlikte |
| X | **19** | **6** | `289400` |
| Y | **25** | **6** | `199400` |
| Special | 0 | 0 | Bu TT örneğinde özel veri yok; boş metin okunur. |

`Barcode ID` tanım kaydının kimliğidir; etiketin program numarası değildir. `Stan` alanı ayrıştırılır, ancak bu akışta K ile karşılaştırılarak ayrıca doğrulanmaz. Klavyeden girişin başlangıcı ayrı `BarcodeStartChar` ayarıyla yönetilir.

**Aynı uzunlukta birden fazla tanıma dikkat:** format seçimi barkod adına veya gönderici makineye göre yapılmaz; toplam karakter sayısına göre yapılır. Aynı uzunluktaki çakışan tanımlar beklenmeyen eşleşmeler oluşturabilir.

### X ve Y neden 6 karakter okunuyor?

MWM_V3'te doğrudan okuma dönüşümü şöyledir:

```text
Ekrandaki ölçü = Okunan sayısal değer × XYFactor / 100
```

`XYFactor = 1` için TT'nin 5 haneli ölçüsü ve sonrasındaki sabit `0`, birlikte 6 karakter okunur:

```text
X: 28940 + 0 → 289400 × 1 / 100 = 2894,00 mm
Y: 19940 + 0 → 199400 × 1 / 100 = 1994,00 mm
```

Yalnızca 5 ölçü hanesi okunacaksa başlangıçlar yine **19 ve 25**, uzunluklar **5** ve `XYFactor = 10` olmalıdır. Bu, aynı sonucu veren alternatif bir kurulumdur; faktör makine genelinde kullanıldığı için mevcut ayarı kontrol ederek seçim yapın. **6 hane + faktör 1** ile **5 hane + faktör 10** kurulumlarını karıştırmayın.

Örnek barkod için X başlangıcı 20 veya Y başlangıcı 26 seçilirse ilk ölçü hanesi atlanır. Bu değerler bu TT örneğine uygun değildir.

## 4. Okutunca hangi işlemler yapılır?

### Doğrudan veri okuma — manuel ekran

1. Okuyucu, metni klavye girişi olarak gönderir. Varsayılan başlangıç `K`, bitiş **Enter / CR (`\r`)** karakteridir. K metne dahildir; CR değildir.
2. HMI, toplam uzunluğa uyan barkod tanımından alanları çıkarır.
3. Profil ve conta/renk alanı birleştirilir; makinedeki profil reçetesi seçilir. Eşleşme bulunamazsa profil bulunamadı uyarısı verilir.
4. Eritme, kaynak ve soğutma süreleri; sıcaklık, kalıp, profil eni/yüksekliği ve ilgili üretim seçenekleri **profil reçetesinden** yüklenir. Bu parametreler 31 karakterlik barkodun içinde yoktur.
5. X/Y sayıya çevrilir ve ölçeklenir. Makinenin büyük kenarı Y'ye alma ve eksen sınırı ayarlarına göre iki ölçünün yeri değişebilir.
6. Renk farkı ve görüntüleme çarpanı uygulanarak ölçüler PLC'ye aktarılır. Operatör üretime geçmeden önce seçilen profil ve ölçüleri kontrol eder.

Barkod okutma veri seçimi ve aktarımıdır; tek başına kaynak çevriminin başladığı anlamına gelmez.

### PLC'ye giden ölçü

MWM_V3, renk opsiyonu etkin ve reçetede alt veya üst renk seçiliyse ayarlı renk farkını ölçüden düşer. Ardından görüntüleme çarpanına böler:

```text
PLC ölçüsü = (Ekrandaki ölçü − uygulanan renk farkı) / görüntüleme çarpanı
```

Renk farkı yok ve görüntüleme çarpanı 1 ise 2894,00 / 1994,00 mm aynen aktarılır; eksen sıralaması ayarları ayrıca geçerlidir. **Kesim boyu, barkoddan çözülen çerçeve boyu ve PLC'ye aktarılan boy her kurulumda aynı kabul edilmemelidir.** TT sayfasındaki kaynak toleransı açıklaması da üretici tarafındaki ölçü hazırlığıyla ilgilidir; barkod okuyucu aşamasında koşulsuz ikinci bir kaynak payı düşüldüğü varsayılmamalıdır.

### İş listesiyle çalışma — otomatik ekran

Otomatik ekranda barkodun görevi farklıdır: **yüklü iş listesindeki satırı bulmak**.

| BatchFileMode | Eşleştirme |
|---|---|
| 0 Standart, 2 FabPlus, 3 Sturtz, 5 Superseal | Toplam uzunluğa uyan tanımın **Prof** alanı alınır ve listedeki `ListNo` değeri aranır. |
| 1 Doğrudan liste numarası, 4 Rotox | Gelen barkod metninin **tamamı** `ListNo` ile eşleştirilir. |

Satır bulunursa o satır seçilir; üretim verisi iş listesinden gelir. Doğrudan okumada profil kodunu gösteren **Prof** alanı, bu modda **liste eşleştirme anahtarı** olarak kullanılır. Bu nedenle aynı barkod tanımının her iki çalışma biçiminde uygun olduğu varsayılmamalıdır. `N001` iş dosyası satırının liste numarası `001` ise doğrudan liste numarası modunda beklenen tarama metni `001` olur; başındaki N otomatik olarak ayıklanmaz. Sayısal barkod için K başlangıç şartı da kurulumda uygun şekilde ayarlanmalıdır.

İş dosyası formatı ve KD658 örnekleri: [Türkçe iş dosyası rehberi](turkish.md).

### Special alanı

Bu alan standart TT örneğinde yoktur. Tanımlandığında çoğu modelde üçlü kaynak konumu olarak ölçeklenebilir; FAC850'de kayıt (mullion) sayısı anlamında kullanılır. Ayrıca metin olarak ve sayıya dönüşebiliyorsa sayısal değer olarak PLC'ye aktarılmaya çalışılır. FAC850 / SAC840 için ayrıca barkod okundu bilgisi yazılır. **Özel alanın anlamı modelin PLC uygulamasına bağlıdır.**

## 5. MSC_V2X'ten gelen barkod

MWM okuyucusu TT veya MSC cihaz adını algılamaz; **kendisine gelen karakterleri** işler. MSC_V2X'te etiket, kullanılan FastReport `Part.frx` şablonuyla veya dışarıdan gelen EPL yazdırma dosyasıyla oluşturulabilir. Bu nedenle bütün MSC makinelerinin aynı barkodu bastığı varsayılamaz.

| MSC etiketinin içeriği | MWM'de yapılacak tanım |
|---|---|
| Yukarıdakiyle aynı 31 karakterlik düzen | Aynı alan konumları; profil reçetesi ve ölçü faktörü doğrulanır. |
| Profil, renk veya ölçüleri farklı konumda taşıyan metin | Gerçek örneğe göre yeni başlangıç / uzunluk tanımı oluşturulur. |
| Yalnız parça / pozisyon / sipariş kimliği | Tek başına profil ve ölçü vermez. Uygun iş listesindeki `ListNo` ile eşleştirilmesi gerekir. |

Bir MSC etiketini devreye alırken okunabilen baskıya değil, okuyucudan gelen **tam barkod metnine** bakın. Bu sayfada belirli bir MSC makinesinin canlı çıktısı doğrulanmış değildir; aynı düzen için uyumluluk koşulları açıklanmıştır.

## 6. İlk kurulumda kontrol

1. Bir etiketi okutup tam metni ve karakter sayısını görün; boşlukları, baştaki sıfırları koruyun. Okuyucunun fazladan önek veya kod türü kimliği göndermediğini, CR ile bitirdiğini doğrulayın.
2. Manuel / otomatik çalışma biçimini ve `BatchFileMode` ayarını belirleyin.
3. Manuel doğrudan okumada profil + conta/renk anahtarının makinede mevcut olduğunu kontrol edin.
4. Yukarıdaki örneği tanım ekranında alanlara ayırın. X = `289400`, Y = `199400`, Color = `01` görülmelidir.
5. Faktör 1 ile ekranda 2894,00 ve 1994,00 mm beklenir. Eksen yer değiştirme, renk farkı ve görüntüleme çarpanı varsa sonucu bu ayarlarla birlikte değerlendirin.
6. Farklı ölçülü ikinci bir etiket ve farklı renk/conta reçetesiyle de eşleşmeyi doğrulayın.

| Belirti | Önce kontrol edin |
|---|---|
| Okutunca işlem olmuyor | Aktif ekran, K başlangıcı, CR bitişi, toplam uzunluk ve barkod tanımı. Uzunluk eşleşmemesi her zaman uyarı üretmez. |
| Profil bulunamadı | 12 karakter profil alanı, boşluklar, 2 karakter conta/renk ve birleşik `ProfID` kaydı. |
| Ölçü 10 kat büyük / küçük | Ölçü alanının 5 / 6 hane seçimi ve `XYFactor`. |
| X/Y beklenmedik | Başlangıçlar 19 / 25 mi; büyük kenar / eksen sınırı ayarları etkin mi? |
| PLC ölçüsü ekrandan farklı | Renk farkı ve görüntüleme çarpanı. |
| Parça bulunamadı | Yüklü iş listesi, `ListNo`, `BatchFileMode` ve eşleştirmede kullanılan metin. |

## Teknik dayanak ve kapsam

Bu rehber 20 Ekim 2026 tarihinde MWM_V3 `v26.1` kaynak sürümü (`e04f15a`) üzerinden kontrol edildi: `FrmState` giriş toplama, `UCManual.SearchBarcodeAllData` doğrudan ayrıştırma, `SearchProfData` reçete yükleme, `ControlXY` / `WriteXY` ölçü aktarımı, `UCAutomatic.SearchBarcode` liste eşleştirme ve `FrmBarcodeInit.SetBarcodeVal` alan seçimi. MSC_V2X `v27.1` (`61805f7e`) içindeki etiket / EPL yazdırma yolları da incelendi.

Bu bir yazılım davranışı açıklamasıdır; her makinenin canlı ayarlarının veya mekanik çevriminin test edildiği anlamına gelmez. [TT etiket referansı](https://hm-info.github.io/tt-barcode/Turkish) üretici formatını, bu sayfa ise MWM tarafındaki kullanımını açıklar.
