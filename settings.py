import random
import pygame

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.font.init()
pygame.init()

MAX_FPS = 60
colors = {"white":  (255, 255, 255),
          "red":    (255, 0, 0),
          "blue":   (0, 0, 255),
          "green":  (0, 255, 0),
          "gray":   (127, 127, 127),
          "yellow": (255, 255, 0),
          "orange": (255, 127, 255),
          "purple": (255, 0, 255),
          "black":  (0, 0, 0),
          }
SPEED = 5
WIDTH = 600
HEIGHT = 450
times_new_roman_font = pygame.font.SysFont('Segoe UI', 40)
times_new_roman_font_10 = pygame.font.SysFont('Segoe UI', 15)


class sounds:
    def __init__(self):
        self.wood_1 = pygame.mixer.Sound("music/sound_wood_1.mp3")
        self.wood_2 = pygame.mixer.Sound("music/sound_wood_2.mp3")

    def wood(self):
        random_number = random.randrange(1, 5)
        if random_number == 1:
            self.wood_2.play()
        elif 2 <= random_number <= 4:
            self.wood_1.play()
