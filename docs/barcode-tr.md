---
title: MWM Kaynak Makineleri — Barkod Bilgi Sayfası
lang: tr
pdf: mwm-barcode-tr.pdf
---

# MWM Kaynak Makineleri — Barkod Bilgi Sayfası

<div class="document-tools" markdown="1">
**[PDF indir](downloads/mwm-barcode-tr.pdf)**
</div>

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

Kaynak makinesinde **12 karakter profil + 2 karakter conta/renk** birlikte profil reçetesini seçer:

```text
Profil       : PROFILE CODE
Conta + renk : 01
Profil tanımı: PROFILE CODE01
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

`Barcode ID` barkod tanımının numarasıdır; etiketin program numarası değildir. Okuyucunun başlangıç karakteri ayrıca makine ayarlarıyla uyumlu olmalıdır.

**Aynı uzunlukta birden fazla tanıma dikkat:** format seçimi barkod adına veya gönderici makineye göre yapılmaz; toplam karakter sayısına göre yapılır. Aynı uzunluktaki çakışan tanımlar beklenmeyen eşleşmeler oluşturabilir.

### X ve Y neden 6 karakter okunuyor?

Bu örnekte ölçü çarpanı **1** seçilir ve okunan altı haneli sayı 100'e bölünür:

```text
Ekrandaki ölçü = Okunan sayısal değer / 100
```

TT'nin 5 haneli ölçüsü ve sonrasındaki sabit `0`, birlikte 6 karakter okunur:

```text
X: 28940 + 0 → 289400 × 1 / 100 = 2894,00 mm
Y: 19940 + 0 → 199400 × 1 / 100 = 1994,00 mm
```

Mevcut bir makinede farklı ölçü uzunluğu veya çarpanı kullanılıyorsa tanımı servis ayarlarıyla birlikte kontrol edin. Buradaki **6 hane + çarpan 1** örneğini farklı bir kurulumla karıştırmayın.

Örnek barkod için X başlangıcı 20 veya Y başlangıcı 26 seçilirse ilk ölçü hanesi atlanır. Bu değerler bu TT örneğine uygun değildir.

## 4. Okutunca hangi işlemler yapılır?

### Doğrudan veri okuma — manuel ekran

1. Okuyucu, metni klavye girişi olarak gönderir. Varsayılan başlangıç `K`, bitiş **Enter / CR (`\r`)** karakteridir. K metne dahildir; CR değildir.
2. HMI, toplam uzunluğa uyan barkod tanımından alanları çıkarır.
3. Profil ve conta/renk alanı birleştirilir; makinedeki profil reçetesi seçilir. Eşleşme bulunamazsa profil bulunamadı uyarısı verilir.
4. Eritme, kaynak ve soğutma süreleri; sıcaklık, kalıp, profil eni/yüksekliği ve ilgili üretim seçenekleri **profil reçetesinden** yüklenir. Bu parametreler 31 karakterlik barkodun içinde yoktur.
5. X/Y sayıya çevrilir ve ölçeklenir. Makinenin büyük kenarı Y'ye alma ve eksen sınırı ayarlarına göre iki ölçünün yeri değişebilir.
6. Makine ayarlarına göre ölçü düzeltmeleri uygulanır. Operatör üretime geçmeden önce seçilen profil ve ölçüleri kontrol eder.

Barkod okutma veri seçimi ve aktarımıdır; tek başına kaynak çevriminin başladığı anlamına gelmez.

### Ekrandaki ölçü ve üretim ölçüsü

Makinede renk farkı, birim / görüntüleme çarpanı veya eksen yerleştirme ayarı varsa üretimde kullanılan ölçü buna göre değişebilir.

**Kesilen tek parçanın boyunu, çerçeve ölçüsünü ve üretim ölçüsünü birbirine karıştırmayın.** Etiket hazırlığında kullanılan kaynak payını ve makinenin ölçü ayarlarını birlikte değerlendirin; aynı payı iki kez uygulamayın.

### İş listesiyle çalışma — otomatik ekran

Otomatik ekranda barkodun görevi farklıdır: **yüklü iş listesindeki satırı bulmak**.

| Çalışma biçimi | Eşleştirme |
|---|---|
| Barkodun belirli bir alanıyla satır seçimi | Barkod tanımında seçilen bölüm, iş listesindeki liste numarasıyla eşleştirilir. |
| Doğrudan liste numarasıyla satır seçimi | Okutulan metnin tamamı, iş listesindeki liste numarasıyla eşleştirilir. |

Satır bulunursa o satır seçilir; üretim verisi iş listesinden gelir. Bu nedenle doğrudan veri okuma ile iş listesiyle çalışma için aynı barkod ayarının uygun olduğu varsayılmamalıdır. İş dosyasında `N001` ile gösterilen satırın liste numarası `001` ise doğrudan liste numarasıyla seçimde beklenen metin `001` olur. Okuyucunun başlangıç ayarı da sayısal barkodla uyumlu olmalıdır.

İş dosyası formatı ve KD658 örnekleri: [Türkçe iş dosyası rehberi](turkish.md).

### Special alanı

Bu alan standart TT örneğinde yoktur. Makine modeline göre üçlü kaynak konumu veya kayıt (mullion) sayısı gibi ek bilgiler için kullanılabilir. Servis tarafından tanımlanmış bir ihtiyaç yoksa bu örnekteki gibi **0 / 0** bırakın.

## 5. MSC_V2X'ten gelen barkod

MSC_V2X arayüzlü kesim merkezlerinin etiket düzeni, makine ve etiket şablonuna göre değişebilir. Uyumluluk için etiketin görünüşünden önce **okuyucudan gelen tam barkod metni** kontrol edilmelidir.

| MSC etiketinin içeriği | MWM'de yapılacak tanım |
|---|---|
| Yukarıdakiyle aynı 31 karakterlik düzen | Aynı alan konumları; profil reçetesi ve ölçü faktörü doğrulanır. |
| Profil, renk veya ölçüleri farklı konumda taşıyan metin | Gerçek örneğe göre yeni başlangıç / uzunluk tanımı oluşturulur. |
| Yalnız parça / pozisyon / sipariş kimliği | Tek başına profil ve ölçü vermez. Uygun iş listesindeki liste numarasıyla eşleştirilmesi gerekir. |

Yukarıdaki TT örneğine uygunluk, her MSC etiketi için otomatik olarak geçerli değildir. Devreye almada gerçek etiketle profil, conta/renk ve ölçü eşleşmesini kontrol edin.

## 6. İlk kurulumda kontrol

1. Bir etiketi okutup tam metni ve karakter sayısını görün; boşlukları, baştaki sıfırları koruyun. Okuyucunun fazladan önek veya kod türü kimliği göndermediğini, CR ile bitirdiğini doğrulayın.
2. Manuel doğrudan okuma veya otomatik iş listesiyle çalışma biçimini belirleyin.
3. Manuel doğrudan okumada profil + conta/renk anahtarının makinede mevcut olduğunu kontrol edin.
4. Yukarıdaki örneği tanım ekranında alanlara ayırın. X = `289400`, Y = `199400`, Color = `01` görülmelidir.
5. Faktör 1 ile ekranda 2894,00 ve 1994,00 mm beklenir. Eksen yer değiştirme, renk farkı ve görüntüleme çarpanı varsa sonucu bu ayarlarla birlikte değerlendirin.
6. Farklı ölçülü ikinci bir etiket ve farklı renk/conta reçetesiyle de eşleşmeyi doğrulayın.

| Belirti | Önce kontrol edin |
|---|---|
| Okutunca işlem olmuyor | Aktif ekran, K başlangıcı, CR bitişi, toplam uzunluk ve barkod tanımı. Uzunluk eşleşmemesi her zaman uyarı üretmez. |
| Profil bulunamadı | 12 karakter profil alanı, boşluklar, 2 karakter conta/renk ve makinedeki profil tanımı. |
| Ölçü 10 kat büyük / küçük | Ölçü alanının karakter sayısı ve ölçü çarpanı. |
| X/Y beklenmedik | Başlangıçlar 19 / 25 mi; büyük kenar / eksen sınırı ayarları etkin mi? |
| Üretim ölçüsü ekrandan farklı | Renk farkı ve görüntüleme çarpanı. |
| Parça bulunamadı | Yüklü iş listesi, liste numarası, çalışma biçimi ve okutulan metin. |

## İlgili bilgi

[TT etiket referansı](https://hm-info.github.io/tt-barcode/Turkish) · [KD658 iş dosyası rehberi](turkish.md)

Bu rehber verilen örnek etiket içindir. Makineye özel ölçü ve reçete ayarlarını devreye alma sırasında doğrulayın.
