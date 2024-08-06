# Manipulasi Gambar
# from PIL import Image
# from PIL import ImageFilter

# # Memuat Gambar
# image = Image.open('sample.webp')

# # Menyimpan Gambar
# image.save('result.jpg')

# # Cropping
# cropped_image = image.crop((10,10,200,200))
# cropped_image.save('cropped_result.jpg')

# # Resizing
# resized_image = cropped_image.resize((100,100))
# resized_image.save('resized_result.jpg')

# # Filtering
# filtered_image = resized_image.filter(ImageFilter.BLUR)
# filtered_image.save('filtered_result.jpg')

# Manipulasi Audio
from pydub import AudioSegment

# Memuat File Audio
audio = AudioSegment.from_file('sample.mp3')

# Menyimpan File Audio
audio.export('result.mp3', format = 'mp3')

# Crop Audio
clipped_audio = audio[:10000] # Mendapatkan 10 detik pertama
clipped_audio.export('clipped_result.mp3', format = 'mp3')

# Penggabungan Audio
combined_audio = audio + clipped_audio
combined_audio.export('combined_result.mp3', format = 'mp3')

# Konversi Audio
audio.export('result.wav', format = 'wav')

# Pengaturan Volume
louder_audio = audio + 10 # Meningkatkan audio sebesar 10dB
louder_audio.export('louder_result.mp3', format = 'mp3')
