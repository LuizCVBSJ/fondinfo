import g2d_pyodide as g2d
import math

def move_pen(start: tuple[float, float], length: float, angle: float) -> tuple[float, float]:
    x, y = start
    x1 = x + math.cos(angle) * length
    y1 = y + math.sin(angle) * length
    g2d.draw_line((int(x), int(y)), (int(x1), int(y1)))
    return (x1, y1)

def koch(pos, length, angle) -> tuple[float, float]:
    if length < 5:
        return move_pen(pos, length, angle)
    length = length / 3
    pos = koch(pos, length, angle)
    pos = koch(pos, length, angle - math.pi / 3)
    pos = koch(pos, length, angle + math.pi / 3)
    pos = koch(pos, length, angle)

    return pos

def main():
    g2d.init_canvas((600, 600))

    pos, side, angle = (200, 200), 300, 0
    koch(pos, side, angle)

    g2d.main_loop()

main()
