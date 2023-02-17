#ADICIONANDO ARQUIVO .MP3 EM PYTHON
import pygame
pygame.init()
pygame.mixer.music.load('D:\curso-de-python\curso-de-python-gustavo-guanabara\CursoGuanabaraPython\desafio21.wav')
pygame.mixer.music.play(-1)
