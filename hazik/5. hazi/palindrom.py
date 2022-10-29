import string

def palindrom(input):
    text = ""

    for i in input:
        if i not in string.punctuation:
            text += i
    text = text.lower().replace(" ", "")

    for i in range(len(text)):
        if text[i] != text[- i - 1]:
            print("Nem palindróm")
            break
    else:
        print("Palindróm")

if __name__ == "__main__":
    palindrom(input(">>>"))