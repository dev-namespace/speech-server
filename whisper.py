#!/usr/bin/env python

import os

from faster_whisper import WhisperModel

model = None

def start_whisper(model_size="large-v2"):
    global model
    # Run on GPU with FP16
    model = WhisperModel(model_size, device="cuda", compute_type="float16")

def transcribe(path, segmented=False):
    segments, info = model.transcribe(path, beam_size=5)
    output = ""
    for segment in segments:
        output += segment.text
    return {
        "language": info.language,
        "language_probability": info.language_probability,
        "text": output
    }

def transcribe_segments(path):
    segments, info = model.transcribe(path, beam_size=5)
    segments = list(map(lambda s: ({
        "text": s.text,
        "start": s.start,
        "end": s.end
    }), segments))
    return {
        "language": info.language,
        "language_probability": info.language_probability,
        "segments": segments
    }
