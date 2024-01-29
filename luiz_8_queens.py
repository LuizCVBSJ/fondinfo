def print_board(board: list):
    print()
    for queen in board:
        print("•" * queen + "♛" + "•" * (len(board) - queen - 1))
    print()


def main():
    board = [int(input(f"Position of queen {queen}?")) for queen in range(int(input("How many rows and cols?")))]
    print_board(board)

main()
