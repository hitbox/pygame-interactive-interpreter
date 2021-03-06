import pygame as pg

class Rect(pg.Rect):

    def __init__(self, *args):
        if len(args) == 1:
            x, y = 0, 0
            width, height = args[0]
        elif len(args) == 2:
            x, y = args[0]
            width, height = args[1]
        else:
            x, y, width, height = args
        super().__init__(x, y, width, height)

    def render(self, color, width):
        surf = pg.Surface(self.size, flags=pg.SRCALPHA)
        pg.draw.rect(surf, color, pg.Rect((0,0),self.size), width)
        return surf

    def get_rect(self, **attrs):
        rect = self.copy()
        for key, value in attrs.items():
            setattr(rect, key, value)
        return rect
