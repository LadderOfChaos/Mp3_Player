import pygame
import tkinter as tkr
from tkinter import filedialog
from tkinter import Scale
player = tkr.Tk()

player.title('Mp3 Player')
player.geometry('205x340')

file = ''
volume_bar = tkr.Scale(player,from_=0.0,to_=1.0, orient = tkr.HORIZONTAL, resolution=0.1)
volume_bar.set(0.5)
pygame.init()
pygame.mixer.init()
def Play():
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(volume_bar.get())


def ExitPlayer():
    pygame.mixer.music.stop()

play_button = tkr.Button(player, width=5, height=3, text="PLAY", command=Play)
play_button.pack(fill='x')
stop_button = tkr.Button(player, width=5, height=3, text="STOP", command=ExitPlayer)
stop_button.pack(fill='x')



def open_masker():
    global file
    file = filedialog.askopenfilename(filetypes=(("Audio Files", ".wav .ogg .flac .mp3"),   ("All Files", "*.*")))


def masker_screen():
    global file
    if file:
        noise = pygame.mixer.Sound(file)
        noise.play(0, 5000)


b1 = tkr.Button(player, text = 'Select Song',command=open_masker)
b1.pack(anchor=tkr.CENTER)
label1 = tkr.LabelFrame(player, text=file)
label1.pack(fill='both', expand='yes')
contents1 = tkr.Label(label1, text=file)
contents1.pack()
volume_bar.pack(fill='both', expand = 'yes')



player.mainloop()

