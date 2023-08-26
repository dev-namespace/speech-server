# Whisper Server

Launches a server in `localhost:5000` that transcribes audio files with `faster_whisper` and generates speech from text with `suno`. I recommend running it with docker to avoid dealing with cuda, venvs, and so on.

`speech-sever` uses large models by default. If you want to use smaller versions, edit the source code and make sure you preload it in the Dockerfile before rebuilding.

## Endpoints

- `localhost:5000/transcribe`
- `localhost:5000/transcribe_segments`
- `localhost:5000/generate_speech`

## Running with docker

Build the docker image:
``` sh
docker build -t voice-server .
```

Run it:
``` sh
docker run --gpus all -it -p 5000:5000 voice-server
```

Test it:
``` sh
curl -X POST -F "file=@/path/input.wav" http://localhost:5000/transcribe
curl -X POST -H "Content-Type: application/json" -d '{"text":"Hello, my name is Suno"}' http://localhost:5000/generate_speech --output output.wav
```

Run it for development:
``` sh
docker run --gpus all -it -p 5000:5000 -v .:/voice-server voice-server /bin/bash
```


