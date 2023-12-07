import g2d

class Ball:
    def __init__(self, x0: int, y0: int, w: int, h: int):
        self._x = x0
        self._y = y0
        self._dx, self._dy = 5, 5
        self._w = w
        self._h = h

    def move(self):
        if not 0 <= self._x + self._dx <= ARENA_W - BALL_W:
            self._dx = -self._dx
        if not 0 <= self._y + self._dy <= ARENA_H - BALL_H:
            self._dy = -self._dy
        self._x += self._dx
        self._y += self._dy

    def pos(self) -> (int, int):
        return self._x, self._y

ARENA_W, ARENA_H, BALL_W, BALL_H = 480, 360, 20, 20

b1 = Ball(40, 80, BALL_W, BALL_H)
b2 = Ball(80, 40, BALL_W, BALL_H)
b3 = Ball(140, 180, BALL_W, BALL_H)
b4 = Ball(180, 140, BALL_W, BALL_H)

def tick():
    g2d.clear_canvas()
    b1.move()
    b2.move()
    g2d.draw_circle(b1.pos(), b1._w)
    g2d.draw_circle(b2.pos(), b2._w)
    b3.move()
    b4.move()
    g2d.draw_circle(b3.pos(), b3._w)
    g2d.draw_circle(b4.pos(), b4._w)

def main():
    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick)

main()
