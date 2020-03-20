p = int(input())
if 0 <= p <= 100:
    if p % 10 == 1:
        print(p, " программист")
    else:
        if 2 <= p % 10 <= 4:
            print(p, " программиста")
        else:
            print(p, " программистов")
if 100 < p <= 1000:
    if 11 <= p % 100 <= 14:
        print(p, " программистов")
    else:
        if 2 <= p % 10 <= 4:
            print(p, "программиста")
        else:
            if p % 10 == 1:
                print(p, " программист")
            else:
                print(p, "программистов")
