a = int(input())
b = int(input())
d = a
while (d % a)!=0 or (d % b) != 0:
    if a == b:
        print(a)
    else:
        while d % a == 0 or d % b == 0:
            a += a
            if a > b:
                print(a)
            else:
                print(b)
print(d)
