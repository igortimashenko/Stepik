programist = int(input())
if 2 <= (programist % 10) <= 4 and (programist // 100) == 0:
    print(programist, " программиста")
else:
    if (programist % 10) == 1 and (programist % 10) != 11:
        print(programist, " программист")
    else:
        print(programist, " программистов")




#print('программист')
#print('программистов')
#print('программиста')
#print('программист')