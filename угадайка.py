import random
print('Добро пожаловать')
print('Введите диапазон чисел')
a,b = int(input('Начало')), int(input('Конец'))
n = random.randint(a, b)
count, c = 0, 0
def valid_s(x):
    return a <= int(x) <= b

while True:
    c = int(input(f'Введите число от {a} до {b}'))
    if valid_s(c) == False:
        print(f'Введите число от {a} до {b}')
        continue
    count += 1
    if c == "":
        print('Введите число.')
    elif c > n:
        print('Введите число меньше загадонного.')
    elif c < n:
        print('Введите число больше загадонного.')
    else:
        print(f'Вы угодали, было загадано число {n}. Вы использовали {count} попыток.')
        next = input("Хотите сыграть еще раз?")
        if next == 'Да' or next == 'да' or next == 'Yes' or next == 'yes':
            a, b = int(input('Начало')), int(input('Конец'))
            n = random.randint(a, b)
            count = 0
            continue
        if next != 'Да' or next != 'да' or next != 'Yes' or next != 'yes':
            print('Всего хорошего')
            break



