from moviepy.editor import ColorClip, concatenate_videoclips
import numpy as np
from moviepy.video.VideoClip import ImageClip

# Setup
clips = []
width, height = 800, 400
rect_width, rect_height = 50, 80
speed = 15  # Faster than walking

# Generate frames
for x in range(0, width - rect_width, speed):
    clip = ColorClip(size=(width, height), color=(255, 255, 255), duration=0.05)
    frame = np.array(clip.get_frame(0))
    frame[height-rect_height-50:height-50, x:x+rect_width] = [255, 0, 0]  # red rectangle
    clips.append(ImageClip(frame).set_duration(0.05))

# Combine
run_video = concatenate_videoclips(clips, method="compose")
run_video.write_videofile("run.mp4", fps=24)

print("✅ run.mp4 created successfully!")
