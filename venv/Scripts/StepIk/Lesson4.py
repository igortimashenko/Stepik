a = int(input())
b = int(input())
c = int(input())
p = (a + b + c) / 2
s = (p*(p-a)*(p-b)*(p-c)) ** 0.5
print(s)
