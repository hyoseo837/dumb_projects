import random

alphabet = "abcdefghijklmnopqrstuvwxyz"


def random_word():
    word = ""
    for i in range(3):
        word += alphabet[random.randrange(26)]
    return word

words = []

while True:
    a = random_word()
    if a in words:
        pass
    else:
        print(a, "is the word? (y/n)" ,end= " ")
        answer = input(": ")
        if answer == "y":
            break
        else:
            words.append(a) 