# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame
pygame.init()  # iniciando pygame
pygame.mixer.music.load('ex021.mp4')  # mixer do pygame
pygame.mixer.music.play()
pygame.event.wait()  # quando encerrar a música, ele para de executar