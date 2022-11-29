c = ["2","5","6","7",]
a = 'Hello world master'
b = 'master'
print(a.upper(), a.lower(), a.split( ))
print(a.count('l')) #start,end # количество повторение, со срезами
print(b.find('e')) #возращает первый индекс есть start, end, с лева на право
(print(a.rfind('h')))
print(a.index('e')) #индекс
print(a.replace("e", 'y')) #замена или удаление'', (третий пар количество замен)
print(a.isalpha()) #True если состоит из букв
print(a.isdigit()) #True если из цифр
print(a.rjust(24,'*')) #заполняет слева n символов на ' ' или любой символ
a.ljust(7) # заполнияе справо
print('     hjhjh    \n'.strip()) # удаляет лишние пробелы и перенос строк
a.rstrip(), a.lstrip()
print(', '.join(c)) #преобразует из списка строк в сроку

