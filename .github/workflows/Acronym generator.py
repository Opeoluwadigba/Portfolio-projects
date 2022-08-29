my_word = str(input("Give me a phrase: "))
text = my_word.split()
b = ""
for i in text:
    b = b+str(i[0]).upper()
print(b)