from pathlib import Path
from moviepy.editor import ImageClip, concatenate_videoclips

root = Path(__file__).resolve().parents[1]
build = root / 'build'
clips = []
for i, line in enumerate((root / 'episodes/scenes.txt').read_text().splitlines()):
    title, text, duration, theme = line.split('|')
    clips.append(ImageClip(str(build / f'scene_{i:02d}.png')).set_duration(float(duration)))
video = concatenate_videoclips(clips, method='compose')
video.write_videofile(str(root / 'Dino_and_the_Missing_Rainbow.mp4'), fps=24, codec='libx264', audio=False)
