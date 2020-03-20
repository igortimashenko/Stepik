a = int(input())
b = int(input())
c = int(input())
if a < b < c:
    maxim = c
    minim = a
elif a > b > c:
    minim = c
    maxim = a
elif a > b < c and a >= c:
    minim = b
    maxim = a
elif a > b < c and a <= c:
    minim = b
    maxim = c
elif a < b > c and a >= c:
    minim = c
    maxim = b
elif a < b > c and a >= c:
    maxim = b
    minim = a
else:
    maxim = b
    minim = c

print(maxim,minim,((a + b + c) - (maxim + minim)), sep="\n")