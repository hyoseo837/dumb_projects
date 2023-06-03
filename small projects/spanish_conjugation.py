import random
f = open("C:/Users/효서/Desktop/spanish verbs.txt","r")
list = f.readlines()
f.close()

while True:
    print(random.choice(list))
    if input() == 'q':
        break