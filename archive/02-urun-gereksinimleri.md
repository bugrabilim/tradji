# Tradji - Ürün Gereksinimleri

## Amaç
Tradji, maddi hasarlı trafik kazalarında kaza tespit tutanağı hazırlama sürecini telefon veya web üzerinden mümkün olduğunca hızlı, anlaşılır ve hatasız hale getirmeyi amaçlar.

## Hedef kullanıcı
- Bireysel araç sürücüleri
- Şirket araçlarını kullanan çalışanlar
- Filo kullanıcıları
- İleri fazda sigorta müşterileri ve hasar operasyon ekipleri

## Temel kullanıcı akışı
1. Tradji açılır.
2. Kullanıcının kayıtlı araç/sürücü bilgileri gelir.
3. Kaza yeri fotoğrafları çekilir.
4. Karşı tarafın ruhsat, ehliyet ve sigorta belgeleri fotoğraflanır.
5. Konum otomatik alınır.
6. Araçların pozisyonu kroki üzerinde gösterilir.
7. Kullanıcı beyanını yazar veya sesli söyler.
8. Tutanak önizlenir.
9. A4/PDF çıktı oluşturulur.
10. Gerektiğinde çıktı ıslak imzalanır.

## Faz 1 özellikleri
### Kullanıcı ve araç
Ad soyad, araç plakası, marka/model, ruhsat, ehliyet ve poliçe bilgileri.

### Kaza
Tarih, saat, GPS koordinatı, adres, açıklama, Taraf A / Taraf B.

### Fotoğraflar
Kaza yeri, hasar, ruhsat, ehliyet ve poliçe fotoğrafları.

### Kroki
İki aracı temsil eden sürüklenebilir öğeler; yol/kavşak/şerit için basit çizim alanı; kullanıcı düzenlemesi.

### Beyan
Metin alanı, destekleyen tarayıcılarda sesli metin girişi, ileri fazda AI taslağı.

### Çıktı
Tutanak önizleme, yazdırma, tarayıcıdan PDF kaydetme, A4 düzeni.

## Faz 1'de yapılmayacaklar
- Kamu veri tabanından plaka sorgusu
- Sigorta şirketinde otomatik hasar dosyası açma
- Resmî kurumlara canlı kaza yayını
- Tam otomatik AI kroki
- Evrensel elektronik imza zorunluluğu

## UX prensipleri
Minimum yazı girişi, büyük ve net butonlar, adım adım akış, fotoğraf önceliği, yanlış alan doldurma riskini azaltma ve her adımda düzenleme imkânı.

## MVP başarı metrikleri
Tutanağı tamamlama süresi, manuel giriş sayısı, formu yarıda bırakma oranı, fotoğraf/konum başarısı, PDF çıktı başarısı ve kağıt yönteme göre tercih oranı.
