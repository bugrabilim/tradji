# Tradji - Proje Geçmişi ve Karar Kaydı

## Problem
Türkiye'de yalnızca maddi hasarla sonuçlanan ve yaralanma/ölüm bulunmayan trafik kazalarında taraflar kaza tespit tutanağı düzenleyebilir. Tradji fikri, kaza anındaki stresli ve manuel belge doldurma sürecini telefon üzerinden sadeleştirmek amacıyla geliştirildi.

## Ana fikirler
- Kullanıcı kayıt sırasında kendi araç, sürücü ve ehliyet bilgilerini sisteme tanımlar; kaza anında bu bilgiler otomatik gelir.
- Karşı tarafın ruhsat, ehliyet ve sigorta belgeleri fotoğraflanır; OCR/görüntü işleme ile alanların otomatik doldurulması hedeflenir.
- Kaza fotoğrafları; kaza yerinin belgelenmesi, araç pozisyonu, hasar, plaka ve ileride otomatik kroki için temel veri kaynağıdır.
- Telefonun GPS/konum servisleriyle koordinatların alınması ve ters geocoding ile adresin otomatik doldurulması planlandı.
- Kaza fotoğraflarından araç pozisyonlarını analiz ederek otomatik kroki üretimi uzun vadeli AI özelliği olarak tanımlandı.
- Taraf beyanlarının sesli söylenip metne dönüştürülmesi ve fotoğraf/kroki bağlamına göre AI beyan taslağı önerilmesi fikri geliştirildi.
- Mobil/e-imza herkeste olmayabileceği için A4 çıktı + ıslak imza temel alternatif olarak benimsendi.
- İleri fazda sigorta şirketine doğrudan bildirim, hasar dosyası açma ve dosya durum takibi hedeflendi.
- Plakadan yetkili kamu kaynakları üzerinden araç/sürücü doğrulama ve polis merkezlerine gerçek zamanlı kaza konumu iletme fikirleri tartışıldı. Bunların resmî izin, hukuki dayanak ve erişim yetkisi gerektirdiği kabul edildi.

## Faz kararı
Kurum entegrasyonlarının giriş aşamasında hem maliyet hem izin açısından projeyi yavaşlatacağı değerlendirildi.

**Faz 1:** Entegrasyonsuz, kapalı devre çalışan MVP.

**Faz 2:** Sigorta şirketleri, kamu kurumları ve diğer yetkili veri kaynakları ile entegrasyonlar.

## Minimum bütçe yaklaşımı
Profesyonel yazılımcı tutmadan düşük bütçeyle doğrulama hedeflendi. İlk aşamada mobil uygulama yerine HTML/CSS/JavaScript + Python/Flask tabanlı web prototipi ve Google Colab prototipleri tercih edildi.

Standart kaza tespit tutanağının dijital forma dönüştürülmesi, boş alanların kullanıcı tarafından doldurulması ve yazdırılabilir/PDF çıktı alınması MVP çekirdeği olarak belirlendi.

## Prototip ve sunum
Google Colab üzerinde form/veri girişi, Pillow ile tutanak görseline metin basma, ipywidgets ve Flask yaklaşımları konuşuldu. HTML tabanlı arayüz geliştirildi. Yatırımcı sunumu için 16:9 PowerPoint, üç slaytlık teknolojik yaklaşım sunumu ve uygulama ekran mockup'ları hazırlandı.

## Proje adı ve GitHub
Projenin adı kesin olarak **Tradji** olarak belirlendi. Proje `bugrabilim/tradji` reposuna taşındı ve çalışan web MVP iskeleti oluşturuldu.
