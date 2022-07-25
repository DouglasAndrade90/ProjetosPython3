import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('exemple.mp3')
pygame.mixer.music.play()
pygame.event.wait()
