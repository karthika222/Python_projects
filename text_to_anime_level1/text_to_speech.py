from TTS.api import TTS

text = "Hi! I'm walking and waving hello to you!"
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False, gpu=False)
tts.tts_to_file(text=text, file_path="voice.wav")

print("✅ Saved voice.wav successfully!")
