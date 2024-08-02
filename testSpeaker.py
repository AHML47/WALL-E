import pygame as pg
import time

pg.mixer.init()
pg.mixer.music.load("/home/ahml-ras/Downloads/test.mp3")  # Replace with the path to your music file

pg.mixer.music.play()

while mixer.music.get_busy():
    time.sleep(1)
