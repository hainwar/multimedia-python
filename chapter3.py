# # Manipulasi Video 

# from moviepy.editor import VideoFileClip
# from moviepy.editor import concatenate_videoclips
# from moviepy.editor import vfx

# # Memuat File Video
# video = VideoFileClip('sample.mp4')

# # Menyimpan File Video
# video.write_videofile('result.mp4')

# # Crop Durasi Video
# short_video = video.subclip(0,10) # Mendapatkan 10 detik pertama
# short_video.write_videofile('short_result.mp4')

# # Penggabungan Video
# combined_video = concatenate_videoclips([video, short_video])
# combined_video.write_videofile('combined_result.mp4')

# # Penambahan Efek
# reversed_video = short_video.fx(vfx.time_mirror) # Membalikkan video
# reversed_video.write_videofile('reversed_result.mp4')


import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog
from pydub import AudioSegment
from pydub.playback import play

# Membuat jendela utama
root = tk.Tk()
root.title("Multimedia Application")

# Memuat gambar menggunakan Pillow
image = Image.open('fk.jpeg')
photo = ImageTk.PhotoImage(image)

# Membuat label untuk menampilkan gambar
label = tk.Label(root, image=photo)
label.pack()

# Definisikan fungsi untuk memutar musik
def play_music():
    file_path = filedialog.askopenfilename()
    if file_path:
        audio = AudioSegment.from_file(file_path)
        play(audio)

# Membuat tombol untuk memutar musik
play_button = tk.Button(root, text="Play", command=play_music)
play_button.pack()

# Menjalankan loop acara Tkinter
root.mainloop()
