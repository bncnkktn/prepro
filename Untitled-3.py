"""atbash"""
def main():
    """print atbash"""
    word_input = input()
    newtext = ''
    for i in word_input:
        if i.isalpha() and i.isupper():
            newtext += chr(91 - (ord(i) - 64))
        elif i.isalpha() and i.islower():
            newtext += chr(123 - (ord(i) - 96))
        else:
            newtext += i
    print(newtext)
main()
