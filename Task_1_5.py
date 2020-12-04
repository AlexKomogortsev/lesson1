# Task 5

net = int(input('Введите Вашу выручку за месяц, руб:'))
cost = int(input('Введите Ваши затраты за месяц, руб:'))

outcome = (net - cost)

if outcome > 0:
    rent = float(outcome / net)
    print('Компания имеет прибыль %d руб!!! А ее рентабельность равна %.3f' % (outcome, rent))
    n = int(input('Введите количество сотрудников в фирме, чел.:'))
    noutcome = float(outcome / n)
    print('В среднем один сотруник зарабатывает для вас %.2f руб' % (noutcome))
elif outcome < 0:
    print('Компания имеет УБЫТОК %d руб!!! Вы БАНКРОТ !!!' % (outcome))
else:
    print('Компания сработала в ноль.')

input('Press Enter')
