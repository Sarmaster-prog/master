print("Ноль в качестве знака операции"
      "\nзавершит работу программы")
while True:
    s = input("Знак (+,-,*,/,%): \n")
    if s == '0':
        break
    if s in ('+', '-', '*', '/', '%'):
        x = float(input("x="))
        y = float(input("y="))
        if s == '+':
            print(x+y)
        elif s == '-':
            print(x-y)
        elif s == '*':
            print(x*y)
        elif s == '%':
            print(x*(y*0.01))
        elif s == '/':
            if y != 0:
                print(x/y)
            else:
                print("Деление на ноль!")
    else:
        print("Неверный знак операции!")
