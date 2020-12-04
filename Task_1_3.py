# Task 3

n = int(input('Введите число n:'))
a = int(n)
b = '%d%d' % (n, n)
b = int(b)
c = '%d%d%d' % (n, n, n)
c = int(c)
d = a + b + c
print('%d + %d%d + %d%d%d = %d' % (n, n, n, n, n, n, d))

input('Press Enter')
