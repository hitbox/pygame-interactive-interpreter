import pygame as pg

from .. import draw
from ..font import Font
from ..globals import g

from .base import Sprite

class CaretSprite(Sprite):

    def __init__(self, *groups, timer=500):
        """
        :params timer: time in ms, to blink on/off.
        """
        super().__init__(*groups)
        self.elapsed = 0
        self.timer = timer
        self.show = True

        self.font = Font()
        w, h = self.font.size(" ")
        # adding width to achieve a cheap offset to not cover characters.
        size = w+4, h

        self.images = {False: pg.Surface(size, pg.SRCALPHA),
                       True: pg.Surface(size, pg.SRCALPHA)}

        show_image = self.images[self.show]
        draw.borderright(show_image, self.font.color, 2)

        self.image = self.images[self.show]
        self.rect = self.image.get_rect()

    def update(self):
        self.elapsed += g.elapsed
        if self.elapsed > self.timer:
            self.elapsed %= self.timer
            self.show = not self.show
            self.image = self.images[self.show]
