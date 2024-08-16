import pygame
pygame.init()

# Mengatur tampilan
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Simple Game")

# Memuat gambar
image = pygame.image.load('f.png')

# Memuat suara
sound = pygame.mixer.Sound('result.wav')

# Memutar suara
sound.play()

# Loop utama permainan dengan animasi
x = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Memperbarui posisi
    x += 5
    if x > 800:
        x = 0

    # Menggambar gambar di posisi baru
    screen.fill((0, 0, 0))
    screen.blit(image, (x, 100))

    # Memperbarui tampilan
    pygame.display.flip()

pygame.quit()

import tkinter as tk
from tkinter import filedialog
from pydub import AudioSegment
from pydub.playback import play

# Membuat jendela utama
root = tk.Tk()
root.title("Music Player")

# Mendefinisikan fungsi untuk memutar musik
def play_music():
    file_path = filedialog.askopenfilename()
    if file_path:
        audio = AudioSegment.from_file(file_path)
        play(audio)

# Membuat tombol play
play_button = tk.Button(root, text="Play", command=play_music)
play_button.pack()

# Menjalankan loop acara Tkinter
root.mainloop()
