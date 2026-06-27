#!/bin/bash
cd "$(dirname "$0")"
BLENDER="/Applications/Blender.app/Contents/MacOS/Blender"
if [ ! -x "$BLENDER" ]; then
  echo "Blender was not found in Applications. Move Blender.app into Applications, then try again."
  read -n 1 -s -r -p "Press any key to close..."
  exit 1
fi
mkdir -p renders output
"$BLENDER" --background --python blender/build_episode.py
open dino_starter.blend
