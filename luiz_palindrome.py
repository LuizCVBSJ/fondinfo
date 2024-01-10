def IsPalindrome(text: str) -> bool:
    if len(text) == 0 or len(text) == 1:
        return True
    if text[0] == text[-1]:
        return IsPalindrome(text[1:-1])
    else:
        return False
text = input("Type a string to see if it's a palindrome:\n")

print(IsPalindrome(text))
