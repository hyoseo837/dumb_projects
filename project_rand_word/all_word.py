alphabet = "abcdefghijklmnopqrstuvwxyz"
word = ""
word_list = []

for i in alphabet:
    for j in alphabet:
        for k in alphabet:
            for l in alphabet:
                for m in alphabet:
                    word = i+j+k+l+m
                    word_list.append(word)

print(len(word_list))