import random

class Cell:
    def __init__(self, number=None):
        self.number = number

class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.cells = [[Cell() for _ in range(cols)] for _ in range(rows)]

    def initialize_board(self, num_numbers):
        # Distribuir números aleatoriamente no tabuleiro
        for _ in range(num_numbers):
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - 1)
            # Verificar se a célula está vazia
            if not self.cells[row][col].number:
                self.cells[row][col].number = random.randint(1, 3)  # Exemplo: números podem mover até 3 células

    def print_board(self):
        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.cells[row][col]
                if cell.number:
                    print(cell.number, end=' ')
                else:
                    print('-', end=' ')
            print()

    def move_number(self, start_row, start_col, dest_row, dest_col):
        if not (0 <= start_row < self.rows and 0 <= start_col < self.cols) or \
           not (0 <= dest_row < self.rows and 0 <= dest_col < self.cols) or \
           not self.cells[start_row][start_col].number or \
           self.cells[dest_row][dest_col].number:
            return False
        
        num_to_move = self.cells[start_row][start_col].number
        distance = abs(dest_row - start_row), abs(dest_col - start_col)
        if distance not in [(0, num_to_move), (num_to_move, 0), (num_to_move, num_to_move)]:
            return False
        
        # Move o número para a nova posição
        self.cells[dest_row][dest_col].number = num_to_move
        self.cells[start_row][start_col].number = None
        return True

    def check_victory(self):
        # Verificar se todos os números foram movidos para células vazias
        for row in range(self.rows):
            for col in range(self.cols):
                if self.cells[row][col].number:
                    return False
        return True

# Exemplo de uso do jogo Z-Numbers
if __name__ == "__main__":
    rows = 5
    cols = 5
    num_numbers = 5

    board = Board(rows, cols)
    board.initialize_board(num_numbers)

    while not board.check_victory():
        print("Tabuleiro:")
        board.print_board()
        start_row = int(input("Digite a linha de origem do número: "))
        start_col = int(input("Digite a coluna de origem do número: "))
        dest_row = int(input("Digite a linha de destino do número: "))
        dest_col = int(input("Digite a coluna de destino do número: "))

        if board.move_number(start_row, start_col, dest_row, dest_col):
            print("Movimento válido!")
        else:
            print("Movimento inválido. Tente novamente.")

    print("Parabéns! Você venceu o jogo Z-Numbers!")

