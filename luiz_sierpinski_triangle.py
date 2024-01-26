import g2d_pyodide as g2d

def main():
    w, h = 512, 512
    g2d.init_canvas((w, h))
    g2d.set_color((0, 0, 0))
    g2d.draw_rect((0, 0), (w, h))
    sierpinski(0, 0, w, h, 5)

def sierpinski(x, y, w, h, level):
    if w < 5 or level == 0:
        return

    w2 = w/2
    h2 = h/2

    g2d.set_color((255, 255, 255))
    g2d.draw_rect((x + w2, y), (w2, h2))

    sierpinski(x, y, w2, h2, level - 1)
    sierpinski(x, y + h2, w2, h2, level - 1)
    sierpinski(x + w2, y + h2, w2, h2, level - 1)

main()
