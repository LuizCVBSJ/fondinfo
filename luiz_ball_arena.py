from luiz_balls import Ball
import g2d

class BallArena:
    def __init__(self) -> None:
        self._balls: list[Ball] = []

    def add(self, b: Ball):
        self._balls.append(b)

    def move_all(self):
        for b in self._balls:
            b.move()

arena = BallArena()
arena.add(Ball(40, 80))
arena.add(Ball(80, 40))

arena.move_all()

ARENA_W, ARENA_H= 480, 360

def tick():
    g2d.clear_canvas()
    for b in arena._balls:
        g2d.draw_circle(b.pos(), b._w)
        b.move()

def main():
    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick)

main()
