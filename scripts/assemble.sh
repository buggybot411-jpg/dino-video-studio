#!/usr/bin/env bash
set -euo pipefail
mkdir -p output
find renders -name '*.mp4' | sort | sed "s#^#file '#;s#$#'#" > output/scenes.txt
ffmpeg -y -f concat -safe 0 -i output/scenes.txt -c copy output/dino_missing_rainbow.mp4
echo "Created output/dino_missing_rainbow.mp4"
