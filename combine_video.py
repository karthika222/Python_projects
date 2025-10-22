from moviepy.editor import ColorClip, concatenate_videoclips, AudioFileClip

# Create multiple frames of a moving rectangle
clips = []
width, height = 800, 400
rect_width, rect_height = 50, 80
speed = 5

for x in range(0, width - rect_width, speed):
    # Create a white background clip
    clip = ColorClip(size=(width, height), color=(255, 255, 255), duration=0.1)
    # Draw rectangle on top
    import numpy as np
    frame = np.array(clip.get_frame(0))
    frame[height-rect_height-50:height-50, x:x+rect_width] = [0, 0, 255]  # blue rectangle
    from moviepy.video.VideoClip import ImageClip
    clips.append(ImageClip(frame).set_duration(0.1))

# Combine all frames
walk_video = concatenate_videoclips(clips, method="compose")

# Save video
walk_video.write_videofile("walk.mp4", fps=24)

# Attach audio
voice = AudioFileClip("voice.wav")
final = walk_video.set_audio(voice)
final.write_videofile("final_output.mp4", fps=24)
