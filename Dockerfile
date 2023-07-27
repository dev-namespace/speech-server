# Start from an existing image
#FROM pytorch/pytorch:1.7.0-cuda11.0-cudnn8-devel
FROM pytorch/pytorch:2.0.1-cuda11.7-cudnn8-runtime


# Install a new library
RUN pip install faster_whisper flask transformers scipy

# Copy files from your local system into the Docker image
COPY ./ /voice-server

WORKDIR /voice-server

# Preload AI models
#RUN python -c "from faster_whisper import WhisperModel; model = WhisperModel('large-v2', device='cuda', compute_type='float16')"
#RUN python -c "from transformers import AutoProcessor, AutoModel; model = AutoModel.from_pretrained('suno/bark-small')"

# CMD ["python", "main.py"]

EXPOSE 5000
