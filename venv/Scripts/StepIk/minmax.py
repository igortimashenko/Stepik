a = int(input())
b = int(input())
c = int(input())
if a < b and b < c:
    max = c
    min = a
    avg = b
    print(max,"\n",min,"\n",avg, sep='')
elif a < b and c < b:
    max = b
    min = a
    avg = c
    print(max, "\n", min, "\n", avg, sep='')
elif a < b and b == c:
    max = c
    min = a
    avg = b
    print(max, "\n", min, "\n", avg, sep='')
elif b < a and b < c:
    max = c
    min = b
    avg = a
    print(max, "\n", min, "\n", avg, sep='')
elif b < a and c < b:
    max = a
    min = c
    avg = b
    print(max, "\n", min, "\n", avg, sep='')
elif b < a and b == c:
    max = a
    min = c
    avg = b
    print(max, "\n", min, "\n", avg, sep='')
elif b < c and a < b:
    max = c
    min = a
    avg = b
    print(max, "\n", min, "\n", avg, sep='')
elif b < c and a > b:
    max = a
    min = b
    avg = c
    print(max, "\n", min, "\n", avg, sep='')
elif b < c and a == b:
    max = c
    min = a
    avg = b
    print(max,"\n",min,"\n",avg, sep='')
elif c < b and a < b:
    max = b
    min = c
    avg = a
    print(max,"\n",min,"\n",avg, sep='')
elif c < b and a > b:
    max = a
    min = c
    avg = b
    print(max,"\n",min,"\n",avg, sep='')
elif c < b and a == b:
    max = a
    min = c
    avg = b
    print(max,"\n",min,"\n",avg, sep='')
elif a < c and b < c:
    max = c
    min = a
    avg = b
    print(max,"\n",min,"\n",avg, sep='')
elif a < c and c < b:
    max = b
    min = a
    avg = c
    print(max,"\n",min,"\n",avg, sep='')
elif a < c and b == c:
    max = c
    min = a
    avg = b
    print(max,"\n",min,"\n",avg, sep='')
elif c < a and b < c:
    max = a
    min = b
    avg = c
    print(max,"\n",min,"\n",avg, sep='')
elif c < a and c < b:
    max = b
    min = c
    avg = a
    print(max,"\n",min,"\n",avg, sep='')
elif c < a and b == c:
    max = a
    min = c
    avg = b
    print(max,"\n",min,"\n",avg, sep='')
elif a == b and b < c:
    max = c
    min = a
    avg = b
    print(max,"\n",min,"\n",avg, sep='')
elif a == b and b > c:
    max = a
    min = c
    avg = b
    print(max,"\n",min,"\n",avg, sep='')
elif a == b and b == c:
    max = a
    min = b
    avg = c
    print(max,"\n",min,"\n",avg, sep='')
elif b == c and a < c:
    max = c
    min = a
    avg = b
    print(max,"\n",min,"\n",avg, sep='')
elif b == c and a > c:
    max = a
    min = c
    avg = b
    print(max,"\n",min,"\n",avg, sep='')
elif b == c and a == c:
    max = c
    min = a
    avg = b
    print(max,"\n",min,"\n",avg, sep='')
elif a == c and b < c:
    max = a
    min = b
    avg = c
    print(max,"\n",min,"\n",avg, sep='')
elif a == c and b > c:
    max = b
    min = a
    avg = c
    print(max,"\n",min,"\n",avg, sep='')
