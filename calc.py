def add(x, y):
    return x + y
    
while True:
    try:
        num1 = float(input("Введите первое число "))
        num2 = float(input("Введите второе число "))
        print(f"{num1} + {num2} = {add(num1,num2)}")
        next_calc = input("Продолжим? Y/N ").lower()
        if next_calc != 'y':
            print("До свидания!")
            break
    except ValueError:
        print("Ошибка")