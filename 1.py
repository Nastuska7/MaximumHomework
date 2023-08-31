a = str(input('Введите слово: '))
word = []
for letter in a:
    word.append(letter)
if word == word[::-1]:
    print(True)
else:
    print(False)