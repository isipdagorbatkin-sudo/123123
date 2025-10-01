print("Добро пожаловать в универсальный калькулятор!")
print("Выберите категорию операции:")
print("1 - Арифметические операции")
print("2 - Операции сравнения")
print("3 - Логические операции")
print("4 - Побитовые операции")
print("5 - Операции принадлежности")
print("6 - Операции тождественности")

choice = input("Введите номер категории (1-6): ")

try:
    # Арифметические операции
    if choice == "1":
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        op = input("Выберите оператор (+, -, *, /, //, %, **): ")

        if op == "+":
            print("Результат:", a + b)
        elif op == "-":
            print("Результат:", a - b)
        elif op == "*":
            print("Результат:", a * b)
        elif op == "/":
            if b != 0:
                print("Результат:", a / b)
            else:
                print("Ошибка: Деление на ноль")
        elif op == "//":
            print("Результат:", a // b)
        elif op == "%":
            print("Результат:", a % b)
        elif op == "**":
            print("Результат:", a ** b)
        else:
            print("Неизвестный оператор")

    # Операции сравнения
    elif choice == "2":
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        op = input("Выберите оператор (==, !=, >, <, >=, <=): ")

        if op == "==":
            print(a == b)
        elif op == "!=":
            print(a != b)
        elif op == ">":
            print(a > b)
        elif op == "<":
            print(a < b)
        elif op == ">=":
            print(a >= b)
        elif op == "<=":
            print(a <= b)
        else:
            print("Неизвестный оператор")

    # Логические операции
    elif choice == "3":
        print("Введите значения True или False")
        a = input("Первое значение: ") == "True"
        b = input("Второе значение: ") == "True"
        op = input("Выберите логический оператор (and, or, not): ")

        if op == "and":
            print("Результат:", a and b)
        elif op == "or":
            print("Результат:", a or b)
        elif op == "not":
            print("Результат:", not a)
        else:
            print("Неизвестный логический оператор")

    # Побитовые операции
    elif choice == "4":
        a = int(input("Введите первое целое число: "))
        op = input("Введите оператор (&, |, ^, ~, <<, >>): ")

        if op in ["&", "|", "^", "<<", ">>"]:
            b = int(input("Введите второе целое число: "))

        if op == "&":
            print("Результат:", a & b)
        elif op == "|":
            print("Результат:", a | b)
        elif op == "^":
            print("Результат:", a ^ b)
        elif op == "~":
            print("Результат:", ~a)
        elif op == "<<":
            print("Результат:", a << b)
        elif op == ">>":
            print("Результат:", a >> b)
        else:
            print("Неизвестный побитовый оператор")

    # Операции принадлежности
    elif choice == "5":
        item = input("Введите элемент: ")
        container = input("Введите строку или список: ")
        op = input("Выберите оператор (in, not in): ")

        if "," in container:
            container = container.split(",")  # превращаем в список

        if op == "in":
            print(item in container)
        elif op == "not in":
            print(item not in container)
        else:
            print("Неизвестный оператор принадлежности")

    # Операции тождественности
    elif choice == "6":
        a = input("Введите первую строку: ")
        b = input("Введите вторую строку: ")
        op = input("Выберите оператор (is, is not): ")

        if op == "is":
            print(a is b)
        elif op == "is not":
            print(a is not b)
        else:
            print("Неизвестный оператор тождественности")

    else:
        print("Ошибка: Неверный номер категории")

except Exception as e:
    print("Произошла ошибка:", e)
