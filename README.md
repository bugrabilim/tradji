# Tradji

Tradji, maddi hasarlı trafik kazalarında kaza tespit tutanağı hazırlama sürecini sadeleştirmeyi amaçlayan web tabanlı bir MVP prototipidir.

## MVP kapsamı

- Sürücü ve araç bilgilerini form üzerinden toplama
- Karşı tarafın ruhsat, ehliyet ve sigorta belgeleri için fotoğraf yükleme alanları
- Tarayıcı konum izniyle kaza konumunu alma
- Kaza fotoğraflarını yükleme
- Kroki alanında temel araç konumlandırma demosu
- Sesli beyanı metne dönüştürme (destekleyen tarayıcılarda Web Speech API)
- Tutanak önizleme ve yazdırma / PDF olarak kaydetme

## Çalıştırma

Ek kurulum gerektirmez. `index.html` dosyasını doğrudan tarayıcıda açabilirsiniz. Konum ve mikrofon gibi tarayıcı izinleri için HTTPS veya localhost kullanılması önerilir.

## Faz 2 hedefleri

- OCR ile ruhsat / ehliyet / poliçe alanlarını otomatik okuma
- Yapay zekâ destekli otomatik kaza krokisi
- Sigorta şirketleri ile hasar dosyası entegrasyonu
- Yetkili kamu sistemleriyle izinli veri alışverişi
- Mobil uygulama

> Bu repo yatırımcı ve kullanıcı doğrulaması için hazırlanmış MVP prototipidir. Resmî kaza tespit tutanağının hukuki geçerliliği ve kurum entegrasyonları ayrıca doğrulanmalıdır.
