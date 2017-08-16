from kappa.core.geom.Point import Point
from ...Settings import Settings
from .ObjectStates import ObjectStates


class CommonObject(object):
    def __init__(self, center, texture):
        self.center: Point = center
        self.texture = texture
        self.state: ObjectStates = ObjectStates.STILL

    @property
    def centerx(self):
        return self.center.x

    @centerx.setter
    def centerx(self, value):
        self.center.x = value

    @property
    def centery(self):
        return self.center.y

    @centery.setter
    def centery(self, value):
        self.center.y = value

    @property
    def centerz(self):
        return self.center.z

    @centerz.setter
    def centerz(self, value):
        self.center.z = value

    @property
    def level(self):
        return self.center.z

    @level.setter
    def level(self, value):
        self.center.z = value

    def center_in_box(self, i, j, l):
        if self.centerz == l and self.centerx / Settings.BOX_WIDTH == i and self.centery / Settings.BOX_HEIGHT == j:
            return True
        else:
            return False

    def center_on_coords(self, x, y):
        self.centerx = x
        self.centery = y

    def center_on(self, c_obj):
        self.center_on_coords(c_obj.centerx, c_obj.centery)
