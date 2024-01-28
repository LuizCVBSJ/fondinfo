def evaluate(tokens: list):
    token = tokens.pop(0)

    if "0" <= token <= "9":
        return float(token)
    else:
        a = evaluate(tokens)
        b = evaluate(tokens)

        if token == "+":
            return a + b
        if token == "-":
            return a - b
        if token == "*":
            return a * b
        if token == "/":
            return a / b
        if token == "div":
            return a // b
        if token == "mod":
            return a % b

def main():
    list_tokens = "mod + * + 1 2 + 2 3 4 5"
    print(list_tokens)
    print(evaluate(list_tokens.split()))

main()
