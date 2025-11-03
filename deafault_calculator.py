from math import pow, sqrt

fnum = float(input(print("Введите первое число")))
snum = float(input(print("Введите второе число")))

operation = input(print("Какую операцию вы бы хотели произвести?"))

if operation == "+":
    print(fnum + snum)
elif operation == "-":
    print(fnum - snum)
elif operation in ("*", "x", "X"):
    print(fnum * snum)
elif operation in (":", "/"):
    print(fnum / snum)
elif operation in ("//", "::"):
    print(fnum // snum)
elif operation in ("**", "pow", "XX", "xx"):
    print(pow(fnum, snum))
elif operation in ("sqrt", "**0.5", "xx0.5", "XX0.5", "**1/2", "xx1/2", "XX1/2"):
    print(sqrt(fnum), "\n", sqrt(snum), sep="")
elif operation == "%":
    print(fnum % snum)
else:
    print("Такой операции не существует")
