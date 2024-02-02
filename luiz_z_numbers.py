import random

class Cell():
    def __init__(self, value = None, moved = False) -> None:
        self.value = value
        self.moved = moved

class ZNumbers():
    def __init__(self, rows, cols):
        self._rows, self._cols = rows, cols
        self._cells = [Cell() for _ in range(self._cols * self._rows)]

    def fill_board(self, numbers):
        y, x = random.randint(0, self._rows - 1), random.randint(0, self._cols - 1)
        for _ in range(numbers):
            self._cells[y * self._cols + x].value = random.randint(0, self._rows-1) 

    def print_board(self):
        for y in range(self._rows):
            for x in range(self._cols):
                cell = self._cells[y * self._cols + x]
                if cell.value:
                    print(cell.value, end=" ")
                else:
                    print("-", end=" ")
            print() 
    def play(self, x0, y0, x1, y1):
        rows = self._rows
        cols = self._cols
        for cell in self._cells:
            print(cell.value, end="-")
        print()
        if not (0 <= x0 <= cols and 0 <= y0 <= rows) or not (0 <= x1 <= cols and 0 <= y1 <= rows):
            print("Invalid coordinates!") 
            return False
        
        first = self._cells[y0 * cols + x0]
        second = self._cells[y1 * cols + x1]

        if not first.value or first.moved:
            print("Invalid first number")
            return False

        move = first.value
        print(first.value, second.value)
        distance = abs(y1 - y0), abs(x1 - x0)
        print(distance)
        if distance not in [(0, move), (move, 0), (move, move)]:
            print("Invalid movement")
            return False
        
        second.value = move 
        first.value = None
        return True

def main():
    game = ZNumbers(5, 5)
    game.fill_board(4)
    game.print_board()
    for _ in range (1):
        x0, y0, x1, y1 = map(int, input("x0,y0,x1,y1? ").split(","))
    game.play(x0, y0, x1, y1)
    game.print_board()
main()
