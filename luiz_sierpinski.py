import g2d_pyodide as g2d

w, h = 600, 600

def sierpinski(x, y, w, h):
    w3, h3 = w // 3, h // 3

    if (w3 < 1 or h3 < 1):
        return

    for row in range(3):
        for col in range(3):
            x3, y3 = x+col*w3, y+row*h3
            if row == 1 and col == 1:
                g2d.set_color((0, 0, 0)) 
                g2d.draw_rect((x3, y3), (w3, h3))
            else:
                sierpinski(x3, y3, w3, h3)
def main():
    g2d.init_canvas((w, h))
    sierpinski(0, 0, w, h)
    g2d.main_loop()

main()
