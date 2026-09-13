# Tradji Proje Arsivi

Bu klasor, Tradji projesi hakkinda bu gorusmede alinan kararlar, urun gereksinimleri, MVP yaklasimi, teknik tercihler, entegrasyon hedefleri, sunum icerikleri ve uretilen gorsel/sunum dosyalarinin yedegidir.

## Metin arsivi
- `01-proje-gecmisi.md`: Fikrin ortaya cikisi ve ana urun kararlari.
- `02-urun-gereksinimleri.md`: Hedef kullanici, kullanici akisi ve MVP gereksinimleri.
- `03-mvp-ve-fazlar.md`: Faz 0, Faz 1, Faz 2 ve ileri AI/B2B yol haritasi.
- `04-teknolojik-yaklasimlar.md`: UCD, Agile, REST, OCR, konum, goruntu isleme, PDF ve ses tanima.
- `05-entegrasyon-hedefleri.md`: Sigorta, kamu, polis ve diger entegrasyon hedefleri.
- `06-sunum-icerigi.md`: Sunum hikayesi ve kullanilan temel anlatim.
- `07-deger-onerisi.md`: Tradji'nin temel deger onerisi.
- `08-prototip-ve-kod-notlari.md`: Colab, Pillow, Flask, web prototipi ve guncel kod notlari.
- `09-belge-manifestosu.md`: Arsivdeki dosyalarin listesi.
- `10-kronoloji.md`: Gorusmedeki urun kararlarinin kronolojik dokumu.

## Uretilen belgeler
- `artifacts/Tradji_Kaza_Tespit_Sunumu.pptx`
- `artifacts/Tradji_Teknolojik_Yaklasimlar_Sunumu.pptx`
- `artifacts/Tradji_Mockup.png`
- `artifacts/Tradji.png`
- `artifacts/kaza_tespit_tutanagi.png`
- `Tradji_Gorusme_Arsivi.zip`

## Yeniden uretilebilirlik
`generate_mockups.py` ve `generate_presentations.py` gorsel belgeleri yeniden olusturur. `build_archive.py` tum Markdown ve artifact dosyalarini ZIP paketine alir. `.github/workflows/build-tradji-archive.yml` bu islemleri GitHub Actions uzerinde otomatik calistirir.

## Onemli not
Gorusmenin onceki asamalarinda uretilen gecici sandbox dosyalarinin birebir orijinal byte kopyalari aktif calisma alaninda artik bulunmadigi icin, sunum ve gorseller gorusmede korunan icerik ve tasarim kararlarina gore yeniden uretilmistir. Proje bilgisinin kendisi metin dokumanlarinda ayrica korunmaktadir.
