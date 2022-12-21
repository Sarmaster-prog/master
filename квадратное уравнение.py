a = int(input('a = ', ))  # запрашиваем первый коэффициент
b = int(input('b = ', ))  # запрашиваем второй коэффициент
c = int(input('c = ', ))  # запрашиваем третий коэффициент

if a != 0 and b % 2 == 0 and c != 0:  # решение по сокращенной формуле, т.к. b - четное
    k = b / 2
    d1 = k ** 2 - a * c
    k1 = (-k + d1 ** 0.5) / a
    k2 = (-k - d1 ** 0.5) / a
    print('так как коэффициент b - четное число, решаем по сокращенной формуле')
    print(f'k1 = {k1}')
    print(f'k2 = {k2}')

if a != 0 and b % 2 != 0 and c != 0:  # решение полного уравнения
    d = b ** 2 - 4 * a * c

    if d > 0:
        k1 = (-b + d ** 0.5) / (2 * a)
        print(f'дискриминант равен: {d}')
        print(f'первый корень равен: {round(k1, 2)}')

        k2 = (-b - d ** 0.5) / (2 * a)
        print(f'второй корень равен: {round(k2, 2)}')
    elif d < 0:
        print(f'так как дискриминант меньше нуля и равен: {d}')
        print('действительных корней нет')
    else:
        k = -b / (2 * a)
        print(f'уравнение имеет один корень: {k}')

if a != 0 and c != 0 and b == 0:  # решение уравнения при b = 0
    if (- c / a) >= 0:
        k1 = (-c / a) ** 0.5
        print(f'первый корень равен: {k1}')
        k2 = (-1) * ((-c / a) ** 0.5)
        print(f'второй корень равен: {k2}')
    if (- c / a) < 0:
        print(f' -c / a = : {-c / a}, т.е. < 0, поэтому действительных корней нет')

if a != 0 and c == 0 and b != 0:  # решение уравнения при с = 0
    print(f'корень уравнения равен либо нулю, либо {-b / a}')

if a != 0 and b == 0 and c == 0:  # решение уравнения при b = 0 и c = 0
    print(f'корни уравнения равны нулю, a*x**2 = 0')