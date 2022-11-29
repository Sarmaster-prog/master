import random
digit = '0123456789'
lower_let = 'abcdefghijklmnopqrstuvwxyz'
upper_let = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punkt = '!#@$%^&*()_'
fox = 'iIlLoO0'
chars = ''
total = int(input('Какое количество паролей Вы хотите создать?'))
leng = int(input('Укажите длину пароля.'))
a = input('Включить цифры? yes/no').lower()
if a in ['yes','да']:
    chars += digit
b = input('Включить строчные буква? yes/no').lower()
if b in ['yes','да']:
    chars += lower_let
c = input('Включить прописные буква? yes/no').lower()
if c in ['yes','да']:
    chars += upper_let
d = input('Включить дополнительные символы? yes/no').lower()
if d in ['yes','да']:
    chars += punkt
f = input('Исключить неоднозначные смволы? yes/no').lower()
if f in ['yes','да']:
    for i in 'iIlLoO0':
        chars = chars.replace(i, '')
print('Список паролей')
def gener (chars, leng):
    password = ''.join(random.choice(chars) for j in range(leng))
    return password
for k in range(1, total+1):
    print(gener(chars, leng))

