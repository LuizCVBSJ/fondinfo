import g2d
from random import randint

g2d.init_canvas((600, 600))

x = 20
y = 30

for i in range(5):
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    g2d.set_color((r, g, b))
    g2d.draw_rect((0, 0), (200, 150))

    x = x + 10
    y = y + 5

g2d.main_loop()
