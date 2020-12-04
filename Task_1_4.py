# Task 4

n = int(input('Введите целое положительное число:'))

a = n % 10
b = n // 10

while a <= b:
    if a >= b % 10:
        b = b // 10
    else:
        a = b % 10
print('Самая большая цифра в Вашем числе равна %d' % (a))

input('Press Enter')
