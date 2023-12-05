ARENA_W, ARENA_H, BALL_W, BALL_H = 480, 360, 20, 20

class Ball:
    def __init__(self, x: int, y: int) -> None:
        self._x = x
        self._y = y
        self._dx = 5
        self._dy = 5

    def move(self):
        if not (0 <= self._x + self._dx <= ARENA_W - BALL_W):
            self._dx = -self._dx
        if not (0 <= self._y + self._dy <= ARENA_W - BALL_W):
            self._dy = -self._dy

        self._x += self._dx
        self._y += self._dy


    def postion(self):
        return self._x, self._y, BALL_W, BALL_H
