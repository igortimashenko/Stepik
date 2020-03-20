import random

words_list = ('автострада', 'бензин', 'инопланетянин',
              'самолет', 'библиотека', 'шайба', 'олимпиада')

secret_word = random.choice(words_list)
print(secret_word)

gamer_word = ['*'] * len(secret_word)
print(''.join(gamer_word))

gamer_word[1] = 'г'
print(''.join(gamer_word))

errors_counter = 0

while True:
    letter = input('Введите ОДНУ русскую букву:').lower()
    if len(letter) != 1 or not letter.isalpha():
        continue
    if letter in secret_word:
        for symbol in secret_word:
            print(symbol)

    else:
        errors_counter += 1
        print("Ошибок допущенно:", errors_counter)
        if errors_counter == 8:
            print('Вы проиграли:(')
            break
    print(''.join(gamer_word))