from kappa.common.object.Direction import Direction
from kappa.common.object.update.UpdateStrategy import UpdateStrategy
from kappa.core.geom.Vector import Vector
from kappa.logger.Logger import Logger


class MovableUpdateStrategy(UpdateStrategy):
    log = Logger(__name__).get()

    def __init__(self, textures=None):
        super().__init__()
        self.__x_move = Direction.NO
        self.__y_move = Direction.NO
        self.__direction = self.__x_move + self.__y_move
        if textures:
            self.__move_textures = textures
            self.__last_direction = Direction.UP
            self.__move_textures[Direction.NO] = self.__move_textures[Direction.UP][0]
            self.__update_move()

    def start_move(self, direction):
        if direction in Direction.X:
            self.__x_move = direction
        elif direction in Direction.Y:
            self.__y_move = direction
        self.__update_move()

    def stop_move(self, direction):
        if direction == self.__x_move:
            self.__x_move = Direction.NO
        elif direction == self.__y_move:
            self.__y_move = Direction.NO
        self.__update_move()

    def __update_move(self):
        vector = Vector(0.0, 0.0, 0.0)
        direction = self.__x_move + self.__y_move

        if direction != Direction.NO:
            needs_normalize = True
            if self.__x_move == Direction.LEFT:
                vector[0] = -1.0
            elif self.__x_move == Direction.RIGHT:
                vector[0] = 1.0
            else:
                needs_normalize = False

            if self.__y_move == Direction.UP:
                vector[1] = -1.0
            elif self.__y_move == Direction.DOWN:
                vector[1] = 1.0
            else:
                needs_normalize = False

            if needs_normalize:
                vector = vector.normalize()
            direction = self.__x_move + self.__y_move

            self.__move_textures[Direction.NO] = self.__move_textures[direction][0]

        self.move_vector_normalized = vector
        self.textures = self.__move_textures[direction]
        self.reset()

    def get_time_vector(self, t: float = 1) -> Vector:
        return self.move_vector * t

    @property
    def is_movable(self):
        return True

    @property
    def move_vector(self):
        return self.move_vector_normalized * self.speed
