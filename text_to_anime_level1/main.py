import os
from gtts import gTTS
from moviepy.editor import VideoFileClip, AudioFileClip

# --- Import motion parser logic ---
from motion_parser import get_motion_from_text

# --- 1️⃣ Get user text input ---
text = input("Enter your scene description (e.g. The character runs and waves hello):\n> ")

# --- 2️⃣ Create voice.wav from text ---
tts = gTTS(text)
tts.save("voice.wav")
print("✅ Created voice.wav successfully!")

# --- 3️⃣ Decide which motion to use ---
motion_file = get_motion_from_text(text)
print(f"🎬 Selected motion: {motion_file}")

if not os.path.exists(motion_file):
    print(f"⚠️ Motion file '{motion_file}' not found! Please run the animation script to create it.")
    exit()

# --- 4️⃣ Combine motion video + voice ---
video = VideoFileClip(motion_file)
voice = AudioFileClip("voice.wav")

final_duration = min(video.duration, voice.duration)
video = video.subclip(0, final_duration)
voice = voice.subclip(0, final_duration)

final = video.set_audio(voice)
final.write_videofile("final_output.mp4", fps=24)
print("🎉 Final video created successfully: final_output.mp4")
