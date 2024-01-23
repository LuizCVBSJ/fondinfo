import g2d_pyodide as g2d 

def h_tree(w0, h0, w, h):
    if w < 20 or h < 20:
        return 

    g2d.draw_line((w0+w/4, h0+h/4), (w0+w/4, h0+h/4*3,))
    g2d.draw_line((w0+w/4*3, h0+h/4), (w0+w/4*3, h0+h/4*3))
    g2d.draw_line((w0+w/4, h0+h/2), (w0+w/4*3, h0+h/2))

    h_tree(w0, h0, w/2, h/2)
    h_tree(w0+w/2, h0, w/2, h/2)
    h_tree(w0, h0+h/2, w/2, h/2)
    h_tree(w0+w/2, h0+h/2, w/2, h/2)

def main():

    w, h = 600, 600
    g2d.init_canvas((w, h))
    h_tree(0, 0, w, h)

main()
