#!/usr/bin/env python

import os, uuid

from flask import Flask, request, jsonify, send_file
from whisper import start_whisper, transcribe, transcribe_segments
from tts import generate_voice, generate_audio_file, start_tts
from utils import TempFile

start_whisper()
start_tts()

app = Flask(__name__)

@app.route('/transcribe', methods=['POST'])
def transcribe_upload():
    with TempFile(request.files['file']) as path:
        output = transcribe(path)
        return jsonify(output)

@app.route('/transcribe_segments', methods=['POST'])
def transcribe_upload_segments():
    with TempFile(request.files['file']) as path:
        output = transcribe_segments(path)
        return jsonify(output)

@app.route('/generate_speech', methods=['POST'])
def generate_speech():
    payload = request.get_json()
    text = payload['text']
    tensors = generate_voice(text)
    generate_audio_file(tensors)
    return send_file('bark_out.wav', as_attachment=True, download_name='output.wav')
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
