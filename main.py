import math, os


# запрос данных
def requestData():
    checkContinue = 2
    a = 0
    b = 0
    c = 0

    while checkContinue != 1:
        os.system("cls")
        print("Ввод коэфицентов:")
        a = float(input('Введите a: '))
        b = float(input('Введите b: '))
        c = float(input('Введите c: '))

        # вывод введеных пользователем данных:
        fullString = f"a = {a} b = {b} c = {c}"
        print(f"\nПроверьте введеные вами данные:\n{len(fullString) * '-'}\n{fullString}\n{len(fullString) * '-'}")
        checkContinue = int(input("\nДанные введены верно?\n1. Да\n2. Нет\n"))

    return a, b, c


# вычисление дискриминанта и вывод решения
def calculateDiscriminant(a, b, c):
    os.system("cls")
    FORMULA_DISCRIMINANT = "Формула дискриминанта: D = (b^2) - 4(ac)"
    fullString = f"D = {b ** 2} - 4 * {a} * {c} = {b ** 2} - {4 * a * c} = {b ** 2 - (4 * a * c)}"
    DISCRIMINANT = b ** 2 - (4 * a * c)
    line = max(len(fullString), len(FORMULA_DISCRIMINANT), len(str(DISCRIMINANT))) * '-'
    NUMBERS = f"a = {a} | b = {b} | c = {c}"
    print(f"\n:{'Решение'.center(len(fullString), ' ')}:\n{line}\n{FORMULA_DISCRIMINANT.center(len(fullString), ' ')}\n{NUMBERS.center(len(fullString), ' ')}\n\n{fullString}")
    print(f"D = {DISCRIMINANT}")
    return DISCRIMINANT, line, fullString


# поиск корней
def search_for_roots(a, b, discriminant, line, fullString):
    print(f"\n{'Нахождение корня(-ей) уравнения:'.center(len(fullString), ' ')}")
    if discriminant > 0:
        x1 = ((-b) + math.sqrt(discriminant)) / (2 * a)
        x2 = ((-b) - math.sqrt(discriminant)) / (2 * a)
        print(f"x1 = {-b} + {math.sqrt(discriminant)} / (2 * {a})")
        print(f"x1 = {-b} - {math.sqrt(discriminant)} / (2 * {a})\nОтвет: x1 = {x1} | x2 = {x2}\n{line}")

    elif discriminant == 0:
        x = (-b) / (2 * a)
        print(f"x = {-b} / 2 * {a}\nОтвет: x = {x}\n{line}")

    else:
        print(f"\n{'Уравнение не имеет корней!'.center(len(fullString), ' ')}\n\n{line}")


checkContinue = 1

# пока пользователь не решит завершить работу
while checkContinue == 1:
    a, b, c = requestData()
    discriminant, line, fullString = calculateDiscriminant(a, b, c)
    search_for_roots(a, b, discriminant, line, fullString)
    checkContinue = int(input("Желаете продолжить работу?\n1. Да\n2. Нет\n"))