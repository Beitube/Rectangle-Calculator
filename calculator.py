# decide to remember how do calculator on py without math library
x = int(input())

if x > 999:
    if x % 7 == 0 or x % 17 == 0:
        print("YES")
    else:
        print("NO")
a = 17 // (23 % 7)
b = 34 % a * 5 - 29 % 4 * 3
print(34 % 8 * 5 - 29 % 4 * 3)



#print(2 // 5)
#name = input(print("Введите своея имя"))
#print("Ваше имя:", name, end = ' ')

#print('aa', 'bb', 'cc', sep = '\n')