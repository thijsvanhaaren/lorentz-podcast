#!/bin/bash
# Gebruik: ./make_episode.sh <id, bv 2026-wk48>   (verwacht scripts/<id>.txt)
set -e
ID=$1
pip install --break-system-packages -q piper-tts >/dev/null 2>&1 || true
VOICE=/tmp/voice/nl-rdh-medium.onnx
if [ ! -f $VOICE ]; then
  mkdir -p /tmp/voice && curl -sL -o /tmp/voice/nl.tar.gz https://github.com/rhasspy/piper/releases/download/v0.0.2/voice-nl-rdh-medium.tar.gz && tar xzf /tmp/voice/nl.tar.gz -C /tmp/voice
fi
python3 -m piper -m $VOICE -f /tmp/$ID.wav --sentence-silence 0.35 < scripts/$ID.txt
ffmpeg -loglevel error -y -i /tmp/$ID.wav -ac 1 -b:a 64k episodes/$ID.mp3
python3 build_feed.py https://thijsvanhaaren.github.io/lorentz-podcast
