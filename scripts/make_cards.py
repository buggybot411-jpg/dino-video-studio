from pathlib import Path
from PIL import Image, ImageDraw

root = Path(__file__).resolve().parents[1]
out = root / 'build'
out.mkdir(exist_ok=True)
for i, line in enumerate((root / 'episodes/scenes.txt').read_text().splitlines()):
    title, text, duration, theme = line.split('|')
    image = Image.new('RGB', (1280, 720), (180, 220, 245))
    draw = ImageDraw.Draw(image)
    draw.ellipse((120, 180, 380, 560), fill=(60, 180, 75))
    draw.rectangle((430, 120, 1180, 600), fill='white')
    draw.text((470, 170), title, fill='black')
    draw.text((470, 260), text, fill='black')
    image.save(out / f'scene_{i:02d}.png')
