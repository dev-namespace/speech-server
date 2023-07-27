import torch
from scipy.io.wavfile import write as write_wav
from transformers import AutoProcessor, AutoModel

model = None
processor = None

def start_tts(model_name="suno/bark-small"):
    global model, processor
    processor = AutoProcessor.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name).to("cuda")

def generate_voice(text, preset = "v2/en_speaker_6"):
    text = "The term 'registry systems and tools' in a job description can refer to a range of different technologies, depending on the specifics of the organization and role."
    inputs = processor(
        text=[text],
        voice_preset=preset
    ).to("cuda")
    print("[*] Generating tensors...")
    tensors = model.generate(**inputs)
    print("[*] Generated")
    audio_array = tensors.cpu().numpy().squeeze()
    print("[*] Formatted")
    return audio_array

def generate_audio_file(tensors, output_file="bark_out.wav"):
    # save audio to disk, but first take the sample rate from the model config
    print("[*] Generating audio file...")
    sample_rate = model.generation_config.sample_rate
    write_wav(output_file, sample_rate, tensors)
    print("[*] Generated")


if __name__ == "__main__":
    print("GPU:", torch.cuda.is_available())
    start_tts()
    tensors = generate_voice("Hello, my name is Suno.")
    generate_audio_file(tensors)
