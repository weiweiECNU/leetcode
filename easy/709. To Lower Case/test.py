def toLowerCase(self, str: str) -> str:
    r = ""
    for char in str:
        if ord(char) >= 65 and ord(char) <= 90 :
            r += chr( ord(char) + 32)
        else:
            r += char
    return r

