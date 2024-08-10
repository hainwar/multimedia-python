from PIL import Image, ImageFilter, ImageEnhance

def manipulate_image(input_path, output_path):
    try:
        # Memuat gambar
        image = Image.open('fk.jpeg')
        print("✅ Gambar berhasil dimuat")

        # Operasi Cropping dengan validasi ukuran
        if image.width > 200 and image.height > 200:
            cropped_image = image.crop((10, 10, 200, 200))
            cropped_image.save('cropped_' + output_path)
            print("✅ Cropping berhasil")
        else:
            raise ValueError("Gambar terlalu kecil untuk di-crop ke ukuran 200x200")

        # Operasi Resizing dengan rasio aspek yang dipertahankan
        resized_image = cropped_image.resize((100, 100), Image.LANCZOS)
        resized_image.save('resized_' + output_path)
        print("✅ Resizing berhasil")

        # Operasi Filtering
        filtered_image = resized_image.filter(ImageFilter.BLUR)
        filtered_image.save('filtered_' + output_path)
        print("✅ Filtering berhasil")

        # Operasi Pengaturan Kecerahan
        enhancer = ImageEnhance.Brightness(filtered_image)
        bright_image = enhancer.enhance(1.5)
        bright_image.save('bright_' + output_path)
        print("✅ Pengaturan kecerahan berhasil")

        # Operasi Penggabungan Gambar
        combined_image = Image.blend(filtered_image, bright_image, alpha=0.5)
        combined_image.save('combined_' + output_path)
        print("✅ Penggabungan gambar berhasil")

    except Exception as e:
        print(f"❌ Terjadi kesalahan: {e}")

if __name__ == "__main__":
    manipulate_image('example.jpg', 'result.jpg')

from pydub import AudioSegment
from pydub.playback import play

def manipulate_audio(input_path, output_path):
    try:
        # Memuat file audio
        audio = AudioSegment.from_file(input_path)
        print("✅ Audio berhasil dimuat")

        # Operasi Pemotongan dengan validasi durasi
        if len(audio) > 10000:
            clipped_audio = audio[:10000]  # Mendapatkan 10 detik pertama
            clipped_audio.export('clipped_' + output_path, format='mp3')
            print("✅ Pemotongan berhasil")
        else:
            raise ValueError("Durasi audio terlalu pendek untuk dipotong 10 detik")

        # Operasi Penggabungan dengan validasi durasi
        combined_audio = audio + clipped_audio
        combined_audio.export('combined_' + output_path, format='mp3')
        print("✅ Penggabungan berhasil")

        # Operasi Konversi Format
        audio.export('result.wav', format='wav')
        print("✅ Konversi format berhasil")

        # Operasi Pengaturan Volume dengan validasi
        if audio.dBFS < -10:
            louder_audio = audio + 10  # Meningkatkan volume sebesar 10dB
            louder_audio.export('louder_' + output_path, format='mp3')
            print("✅ Pengaturan volume berhasil")
        else:
            raise ValueError("Volume audio sudah terlalu tinggi")

        # Operasi Pemutaran Audio
        print("🔊 Memutar audio hasil manipulasi...")
        play(louder_audio)

    except Exception as e:
        print(f"❌ Terjadi kesalahan: {e}")

if __name__ == "__main__":
    manipulate_audio('sample.mp3', 'result.mp3')