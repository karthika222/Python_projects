from moviepy.editor import ColorClip, concatenate_videoclips
import numpy as np
from moviepy.video.VideoClip import ImageClip

clips = []
width, height = 800, 400
rect_width, rect_height = 50, 80
x, y = 375, 250  # fixed position

# Simulate waving (rectangle changing height)
for frame_num in range(20):
    clip = ColorClip(size=(width, height), color=(255, 255, 255), duration=0.1)
    frame = np.array(clip.get_frame(0))

    # simulate hand up and down using small rectangle on top
    rect_height_dynamic = rect_height + (10 if frame_num % 2 == 0 else -10)
    frame[height-rect_height_dynamic-50:height-50, x:x+rect_width] = [0, 255, 0]  # green rectangle

    clips.append(ImageClip(frame).set_duration(0.1))

# Combine
wave_video = concatenate_videoclips(clips, method="compose")
wave_video.write_videofile("wave.mp4", fps=24)

print("✅ wave.mp4 created successfully!")
