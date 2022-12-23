from random import randrange
import time
import math
import pygame
import settings

pygame.init()
pygame.mixer.music.load("music/background.mp3")
pygame.mixer.music.play(loops=-1, start=0, fade_ms=0)
pygame.mixer.music.set_volume(0.6)


class game:
    def __init__(self):
        deg = randrange(225, 315)
        self.blocks = {"size": (70, 29), "color": "orange",
                       "places": [[1, 1], [76, 1], [151, 1], [226, 1],
                                  [301, 1], [376, 1], [451, 1], [526, 1],
                                  [1, 41], [76, 41], [151, 41], [226, 41],
                                  [301, 41], [376, 41], [451, 41], [526, 41],
                                  [1, 81], [76, 81], [151, 81], [226, 81],
                                  [301, 81], [376, 81], [451, 81], [526, 81],
                                  [1, 121], [76, 121], [151, 121], [226, 121],
                                  [301, 121], [376, 121], [451, 121], [526, 121],
                                  [1, 161], [76, 161], [151, 161], [226, 161],
                                  [301, 161], [376, 161], [451, 161], [526, 161]]}
        self.ball = {"position": [300, 325], "radius": 10, "color": "white", "deg": deg}
        self.player = {"position": (250, 350), "size": (100, 14), "color": "white"}
        self.page = "main_menu"
        self.debug_menu = False
        self.get_sounds = settings.sounds()

        self.sc = pygame.display.set_mode((600, 450))
        self.clock = pygame.time.Clock()

    def main_loop(self):
        now_fps = "777"
        while True:  # Главный цикл
            start_time = time.time()
            self.sc.fill(settings.colors["black"])  # Ставим задний фон
            if self.page == "main_menu":
                if self.button((400, 65), (100, 350), settings.colors["white"], "Классическая игра"):
                    deg = randrange(225, 315)
                    self.blocks = {"size": (70, 29), "color": "orange",
                                   "places": [[1, 1], [76, 1], [151, 1], [226, 1],
                                              [301, 1], [376, 1], [451, 1], [526, 1],
                                              [1, 41], [76, 41], [151, 41], [226, 41],
                                              [301, 41], [376, 41], [451, 41], [526, 41],
                                              [1, 81], [76, 81], [151, 81], [226, 81],
                                              [301, 81], [376, 81], [451, 81], [526, 81],
                                              [1, 121], [76, 121], [151, 121], [226, 121],
                                              [301, 121], [376, 121], [451, 121], [526, 121],
                                              [1, 161], [76, 161], [151, 161], [226, 161],
                                              [301, 161], [376, 161], [451, 161], [526, 161]]}
                    self.ball = {"position": [300, 325], "radius": 10, "color": "white", "deg": deg}
                    self.player = {"position": (250, 350), "size": (100, 14), "color": "white"}
                    self.page = "game"
                if self.button((400, 65), (100, 250), settings.colors["white"], "Настройки"):
                    pass
                if self.button((400, 65), (100, 150), settings.colors["white"], "Как играть"):
                    pass
            elif self.page == "game":  # Если страница игры
                self.classic_game()  # Метод классической игры
            elif self.page == "defeat":  # Если страница поражения
                self.sc.fill(settings.colors["black"])
                pygame.draw.line(self.sc, settings.colors["gray"], (0, 300), (600, 300))
                pygame.draw.rect(self.sc, self.player["color"],
                                 (self.player["position"][0], self.player["position"][1],
                                  self.player["size"][0], self.player["size"][1]))
                for block in self.blocks["places"]:
                    pygame.draw.rect(self.sc, self.blocks["color"],
                                     (block[0], block[1], self.blocks["size"][0], self.blocks["size"][1]))
                self.sc.blit(settings.times_new_roman_font.render("Поражение", False, settings.colors["red"]), (200, 300))
                if self.button((100, 65), (250, 350), settings.colors["white"], "На главную"):
                    self.page = "main_menu"
            elif self.page == "victory":  # Если страница победы
                pygame.draw.line(self.sc, settings.colors["gray"], (0, 300), (600, 300))
                pygame.draw.circle(self.sc, self.ball["color"], self.ball["position"], self.ball["radius"])
                pygame.draw.rect(self.sc, self.player["color"],
                                 (self.player["position"][0], self.player["position"][1],
                                  self.player["size"][0], self.player["size"][1]))
                self.sc.blit(settings.times_new_roman_font.render("Победа", False, settings.colors["green"]), (230, 300))
                if self.button((100, 65), (250, 350), settings.colors["white"], "На главную"):
                    self.page = "main_menu"
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Если человек пытается выйти из игры
                    pygame.quit()
                    exit(0)
            self.sc.blit(settings.times_new_roman_font.render(now_fps, False, settings.colors["red"]), (0, 0))

            pygame.display.flip()  # Обновление дисплея
            self.clock.tick(settings.MAX_FPS)
            now_fps = f"FPS: {int(1 / (time.time() - start_time))}"

    def classic_game(self):
        # Отскоки от стен
        if 0 >= self.ball["position"][0] - self.ball["radius"]:  # Отскок от левой стены
            self.ball["deg"] = (180 - self.ball["deg"])
        if settings.WIDTH <= self.ball["position"][0] + self.ball["radius"]:  # Отскок от правой стены
            self.ball["deg"] = (180 - self.ball["deg"])
        if 0 >= self.ball["position"][1] - self.ball["radius"]:  # Отскок от верхней стены
            self.ball["deg"] = (0 - self.ball["deg"])
        if settings.HEIGHT <= self.ball["position"][1] - self.ball["radius"]:  # Поражение если мяч попал вниз
            self.page = "defeat"

        if self.player["position"][0] <= self.ball["position"][0] <= self.player["position"][0] + \
                self.player["size"][0] and self.player["position"][1] <= self.ball["position"][1] <= \
                self.player["position"][1] + self.player["size"][1]:  # отскок от платформы игрока
            self.ball["deg"] = (0 - self.ball["deg"])

        for block in self.blocks["places"]:  # Проходим по всем препятствиям
            if block[0] <= self.ball["position"][0] <= block[0] + self.blocks["size"][0] and block[1] <= \
                    self.ball["position"][1] <= block[1] + self.blocks["size"][1]:  # Столкновение с блоком
                self.get_sounds.wood()
                self.ball["deg"] = (0 - self.ball["deg"])
                self.blocks["places"].remove(block)  # Удаляем препятствие
            if not self.blocks["places"]:
                self.page = "victory"
                return

        if pygame.mouse.get_pos()[1] > 300:  # Если курсор под серой линией
            self.player["position"] = pygame.mouse.get_pos()  # Меняем позицию платформы

        # Передвигаем мяч
        self.ball["position"][0] = \
            self.ball["position"][0] + settings.SPEED * (math.cos(self.ball["deg"] * 1.75 / 100))
        self.ball["position"][1] = \
            self.ball["position"][1] + settings.SPEED * (math.sin(self.ball["deg"] * 1.75 / 100))

        # Отрисовка
        if self.debug_menu:  # Направление мяча
            pygame.draw.line(self.sc, settings.colors["red"], (self.ball["position"]),
                             (600, self.ball["position"][1]))
            pygame.draw.line(self.sc, settings.colors["blue"], self.ball["position"],
                             (self.ball["position"][0] - 300, self.ball["position"][1] - 300))
            pygame.draw.line(self.sc, settings.colors["blue"], self.ball["position"],
                             (self.ball["position"][0] + 300, self.ball["position"][1] - 300))
            pygame.draw.line(self.sc, settings.colors["green"], self.ball["position"],
                             (self.ball["position"][0] + 600 * (math.cos(self.ball["deg"] * 1.75 / 100)),
                              self.ball["position"][1] + 600 * (math.sin(self.ball["deg"] * 1.75 / 100))))

        pygame.draw.line(self.sc, settings.colors["gray"], (0, 300), (600, 300))  # Серая полоса
        pygame.draw.circle(self.sc, self.ball["color"], self.ball["position"], self.ball["radius"])  # Мяч
        pygame.draw.rect(self.sc, self.player["color"],
                         (self.player["position"][0], self.player["position"][1],
                          self.player["size"][0], self.player["size"][1]))  # Платформа
        for block in self.blocks["places"]:  # Блоки
            pygame.draw.rect(self.sc, self.blocks["color"],
                             (block[0], block[1], self.blocks["size"][0], self.blocks["size"][1]))

    def button(self, size, position, color=settings.colors["white"], text=None):
        pygame.draw.rect(self.sc, color,
                         (position[0], position[1],
                          size[0], size[1]))  # Отрисовка кнопки
        len_text = len(text)
        position_text = (position[0] + (size[0] - (len_text * 15 / 2)) / 2, position[1] + 3)
        self.sc.blit(settings.times_new_roman_font_10.render(text, False, settings.colors["black"]), position_text)
        pressed_button_mouse = False
        mouse_click = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Если человек пытается выйти из игры
                pygame.quit()
                exit(0)
            if event.type == pygame.MOUSEBUTTONUP:
                pressed_button_mouse = True
        if pressed_button_mouse:
            if position[0] <= mouse_click[0] <= position[0] + size[0] and\
               position[1] <= mouse_click[1] <= position[1] + size[1]:
                return True
        return False


if __name__ == "__main__":
    application = game()
    application.main_loop()
