a = float(input())
b = float(input())
oper = input()
if oper == "+":
    print(a + b)
elif oper == "/" and b !=0:
    print(a / b)
elif oper == "*":
    print(a * b)
elif oper == "-":
    print(a - b)
elif oper == "mod" and b != 0:
    print(a % b)
elif oper == "pow":
    print(a ** b)
elif oper == "div" and b != 0:
    print(a // b)
elif b == 0 and oper == "mod":
        print("Деление на 0!")
elif b == 0 and oper == "div":
    print("Деление на 0!")
elif b == 0 and oper == "/":
    print("Деление на 0!")