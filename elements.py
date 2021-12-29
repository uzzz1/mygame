import pygame as pg

import parameter as para
from main import main_game


class main_map(pg.sprite.Sprite):
    def __init__(self, x, y) -> None:
        super(main_map, self).__init__()
        self.image = pg.image.load(para.img_path + para.map_image)
        self.map = [[i, j] for i in range(x) for j in range(y)]
        # self.rect = self.image.get_rect()
        self.position = (x, y)

    def display_map(self, window):
        window.blit(self.image, self.position)

class character(pg.sprite.Sprite):
    def __init__(self, x, y) -> None:
        super(character, self).__init__()
        self.image = pg.image.load(para.img_path + para.cheif_image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.position = (x, y)

    def display(self, window):
        window.blit(self.image, self.rect)
