a = int(input())
b = int(input())
c = int(input())
if a < b < c:
    maxim = c
    minim = a
else:
    maxim = a
    minim = c
if b == c:
    if a < b:
        maxim = b
        minim = a
    else:
        maxim = a
        minim = b
elif a == b == c:
    maxim = a
    minim = b
elif a > b < c:
    if a > c:
        maxim = a
        minim = b
    else:
        maxim = c
        minim = b
if a == b:
    if b > c:
        maxim = a
        minim = c
    else:
        maxim = c
        minim = a
elif a < b > c:
    if a > c:
        maxim = b
        minim = c
    else:
        maxim = b
        minim = a
if a == c:
    if a < b:
        maxim = b
        minim = a
    else:
        maxim = a
        minim = b
print(maxim, minim, ((a + b + c)-(maxim + minim)), sep="\n")