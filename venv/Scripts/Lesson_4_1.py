import sys
alphabet = "abcdefghijklmnopqrstuvwxyz"
text = sys.argv[1].lower()
shift = int(sys.argv[2])
coded_text = ""
new_letter = ""
letter_positions = None

for letter in text:
    letter_positions  = alphabet.find(letter)
    if letter_positions != -1:
        new_letter = alphabet[(letter_positions + shift) % len(alphabet)]
    else:
        new_letter = letter
    coded_text = coded_text + new_letter
print(coded_text)