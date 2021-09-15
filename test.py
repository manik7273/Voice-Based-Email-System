import gtts
import pygame
#install pyglet and install http://avbin.github.io/AVbin/Download.html
#extract the avbin.dll from windows/system32/ folder to windows/system/ folder
import os
import time

pygame.mixer.init()

text = ("Hello, World")

obj = gtts.gTTS(text=text, lang='en')
speech_filename = "c:/python/code/test_voice.mp3"
obj.save(speech_filename)

print("Play sound...")

pygame.mixer.music.load(speech_filename)
pygame.mixer.music.play()

busy = True
while busy == True:
    if pygame.mixer.music.get_busy() == False:
        busy = False
pygame.quit()

os.remove(speech_filename) #remove temp file - remove line to keep file