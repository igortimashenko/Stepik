n = int(input())
'''for i in range(n):
    print("*" * n)
    i += 1
    '''

for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()