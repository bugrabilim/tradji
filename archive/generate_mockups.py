from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
ART = ROOT / 'artifacts'
ART.mkdir(exist_ok=True)

REG = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
BOLD = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'

def font(size, bold=False):
    path = BOLD if bold else REG
    return ImageFont.truetype(path, size) if Path(path).exists() else ImageFont.load_default()

img = Image.new('RGB', (1600, 1000), '#f3f6fb')
d = ImageDraw.Draw(img)
d.text((70, 45), 'Tradji', font=font(52, True), fill='#0f172a')
d.text((70, 110), 'Kaza tespit surecini adim adim yoneten mobil deneyim', font=font(24), fill='#64748b')

screens = [
    ('Ana Sayfa', ['KAZA BILDIR', 'Profil', 'Arac Bilgileri']),
    ('Kaza Kaydi', ['Fotograf Cek', 'Belge Ekle', 'Konumu Al', 'Kroki']),
    ('Kaza Detaylari', ['Tarih / Saat', 'Konum / Adres', 'Sesli Beyan']),
    ('Tutanak', ['Onizleme', 'A4 / PDF Olustur', 'Islak Imza'])
]
accent = ['#2563eb', '#16a34a', '#f59e0b', '#ef4444']
for i, (title, buttons) in enumerate(screens):
    x, y = 80 + i * 380, 210
    d.rounded_rectangle((x, y, x+300, y+650), radius=38, fill='#111827')
    d.rounded_rectangle((x+12, y+12, x+288, y+638), radius=30, fill='white')
    d.text((x+30, y+70), title, font=font(25, True), fill='#0f172a')
    yy = y + 140
    for j, label in enumerate(buttons):
        color = accent[min(j, 3)] if i == 1 else ('#2563eb' if j == 0 else '#e2e8f0')
        text_color = 'white' if color != '#e2e8f0' else '#0f172a'
        d.rounded_rectangle((x+28, yy, x+272, yy+68), radius=16, fill=color)
        d.text((x+48, yy+20), label, font=font(19, True), fill=text_color)
        yy += 90
img.save(ART / 'Tradji_Mockup.png')
img.save(ART / 'Tradji.png')

page = Image.new('RGB', (1240, 1754), 'white')
d = ImageDraw.Draw(page)
d.rectangle((35, 35, 1205, 1719), outline='#0f172a', width=4)
d.text((620, 70), 'KAZA TESPIT TUTANAGI', font=font(34, True), fill='#0f172a', anchor='ma')
sections = [
    ('1. Kaza Bilgileri', 170, 360),
    ('2. Arac / Surucu A', 380, 670),
    ('3. Arac / Surucu B', 690, 980),
    ('4. Kaza Krokisi', 1000, 1325),
    ('5. Beyanlar ve Imza', 1345, 1680),
]
for title, y1, y2 in sections:
    d.rounded_rectangle((65, y1, 1175, y2), radius=12, outline='#94a3b8', width=3)
    d.text((85, y1+18), title, font=font(22, True), fill='#0f172a')
    yy = y1 + 70
    while yy < y2 - 25:
        d.line((90, yy, 1150, yy), fill='#d1d5db', width=2)
        yy += 48
page.save(ART / 'kaza_tespit_tutanagi.png')
