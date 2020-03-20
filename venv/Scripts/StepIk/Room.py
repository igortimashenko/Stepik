p = 3.14
figura = input()
if figura == "круг":
    r = float(input())
    print(p * (r**2))
elif figura == "прямоугольник":
    a = float(input())
    b = float(input())
    print(a * b)
elif figura == "треугольник":
    a = float(input())
    b = float(input())
    c = float(input())
    s = ((((a +b +c) / 2) * (((a +b +c) / 2) - a) * (((a +b +c) / 2) - b) * (((a +b +c) / 2) - c))**0.5)
    print(s)
