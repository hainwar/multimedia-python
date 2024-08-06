# Manipulasi Video 

from moviepy.editor import VideoFileClip
from moviepy.editor import concatenate_videoclips
from moviepy.editor import vfx

# Memuat File Video
video = VideoFileClip('sample.mp4')

# Menyimpan File Video
video.write_videofile('result.mp4')

# Crop Durasi Video
short_video = video.subclip(0,10) # Mendapatkan 10 detik pertama
short_video.write_videofile('short_result.mp4')

# Penggabungan Video
combined_video = concatenate_videoclips([video, short_video])
combined_video.write_videofile('combined_result.mp4')

# Penambahan Efek
reversed_video = short_video.fx(vfx.time_mirror) # Membalikkan video
reversed_video.write_videofile('reversed_result.mp4')
