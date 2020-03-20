import sys
text = sys.argv[1:]
for i in range(len(text)):
    text2 = text[::-1]
print(" ".join(text2))