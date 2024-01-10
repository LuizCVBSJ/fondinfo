def IsPalindrome(text: str) -> bool:
    if len(text) <= 1:
        return True
    return text[0] == text[-1] and IsPalindrome(text[1: -1])

text = input("Type a string to check if it's a palindrome:\n")
print(IsPalindrome(text))
