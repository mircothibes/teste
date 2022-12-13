'''Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.'''

import pygame
print ('tocando musica')
pygame.mixer.init()
pygame.mixer.music.load('Beggin.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()





