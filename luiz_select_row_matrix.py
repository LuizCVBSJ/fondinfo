matrix = [2, 4, 3, 8, 
          9, 3, 2, 7,
          5, 6, 9, 1]

cols = 4
rows = len(matrix)//4

selected_row = int(input(f"There are {rows} rows. Which row to print?\n"))

# for row in range(rows):
#     for col in range(cols):
#         print(matrix[col + row * cols], end="\t")
#     print()

for col in range (cols):
    print(matrix[col + selected_row * cols], end="\t")
