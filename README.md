# Tradji

Tradji, maddi hasarlı trafik kazalarında kaza tespit tutanağı hazırlama sürecini sadeleştirmeyi amaçlayan web tabanlı bir MVP prototipidir.

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fbugrabilim%2Ftradji&project-name=tradji&repository-name=tradji)

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

## Vercel

Repo statik Vercel deploy'una hazırdır. `vercel.json`, güvenlik başlıkları ile geolocation, mikrofon ve kamera izin politikasını tanımlar. Git entegrasyonu kurulduktan sonra `main` dalına yapılan push'lar üretim deploy'unu otomatik tetikleyebilir.

## Faz 2 hedefleri

- OCR ile ruhsat / ehliyet / poliçe alanlarını otomatik okuma
- Yapay zekâ destekli otomatik kaza krokisi
- Sigorta şirketleri ile hasar dosyası entegrasyonu
- Yetkili kamu sistemleriyle izinli veri alışverişi
- Mobil uygulama

> Bu repo yatırımcı ve kullanıcı doğrulaması için hazırlanmış MVP prototipidir. Resmî kaza tespit tutanağının hukuki geçerliliği ve kurum entegrasyonları ayrıca doğrulanmalıdır.
