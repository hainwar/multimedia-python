import pygame
import PIL
import cv2
import pkg_resources

def check_installation():
    # Memeriksa dan mencetak versi Pygame, Pillow, dan OpenCV
    print("✅ Pygame versi:", pygame.__version__)
    print("✅ Pillow versi:", PIL.__version__)
    print("✅ OpenCV versi:", cv2.__version__)

    # Memeriksa versi MoviePy
    try:
        moviepy_version = pkg_resources.get_distribution("moviepy").version
        print("✅ MoviePy versi:", moviepy_version)
    except pkg_resources.DistributionNotFound:
        print("❌ MoviePy tidak terpasang.")

    # Memeriksa versi Pydub
    try:
        pydub_version = pkg_resources.get_distribution("pydub").version
        print("✅ Pydub versi:", pydub_version)
    except pkg_resources.DistributionNotFound:
        print("❌ Pydub tidak terpasang.")

    print("✅ Tkinter sudah terpasang.")



check_installation()
