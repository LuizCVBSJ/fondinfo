with open("luiz_example.txt", mode="w") as example:
    for i in range(10):
        print(i, i**2, file=example)
