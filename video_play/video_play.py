import tkinter, tkVideoPlayer

#Funções
def play():
  video.play()
def pause():
  video.pause()
def stop():
  video.stop()

#Construção de tela
Tela = tkinter.Tk()
Tela.title('Mini VideoPlay')
Tela.geometry("280x250+600+200")
Tela.config(background="gray")
Tela.resizable(0, 0)

#Botões
btPlay = tkinter.Button(Tela, text="Play", relief="flat", width=10, borderwidth=2, command=play).grid(row=1, column=0, padx=10, pady=10)

btPause = tkinter.Button(Tela, text="Pause", relief="flat", width=10, borderwidth=2, command=pause).grid(row=1, column=1)

btStop = tkinter.Button(Tela, text="Stop", relief="flat", width=10, borderwidth=2, command=stop).grid(row=1, column=2, padx=10, pady=10)

#Video
video = tkVideoPlayer.TkinterVideo(Tela, scaled=True)
video.load("ex1.mp4")
video.grid(row=0, columnspan=3, sticky="we", padx=10, pady=10, ipady=40)

Tela.mainloop()

import pygame

pygame.init()
pygame.mixer.music.load('ex1.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()