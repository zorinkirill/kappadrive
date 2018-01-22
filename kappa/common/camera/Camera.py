from ..object.GameObject import GameObject
from ..object.RectShape import RectShape
from ..object.SimpleMovingStrategy import SimpleMovingStrategy
from ...core.geom.Point import Point


class Camera(GameObject):
    def __init__(self, w=0, h=0, center=Point(0, 0, 0)):
        GameObject.__init__(self,
                            center,
                            None,
                            RectShape(w, h),
                            SimpleMovingStrategy()
                            )
