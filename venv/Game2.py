import random

words_list = ('автострада', 'бензин', 'инопланетянин',
             'самолет', 'библиотека', 'шайба', 'олимпиада')

secret_word = random.choice(words_list)
print(secret_word)

gamer_word = ['*'] * len(secret_word)
print(''.join(gamer_word))

errors_counter = 0
while True:
   letter = input('введите ОДНУ русскую букву: ').lower()
   if len(letter) != 1 or not letter.isalpha():
       continue

   if letter in secret_word:
       pass
   else:
       # errors_counter = errors_counter + 1
       errors_counter += 1
       print('ошибок допущено:', errors_counter)
       if errors_counter == 8:
           print('вы проиграли :(')
           break
   print(''.join(gamer_word))

print('пробуйте еще')
