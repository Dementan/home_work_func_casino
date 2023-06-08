def simple_casino():
    import random

    number_comp = random.randint(1, 10)
    color_comp = random.randint(1, 2)
    for i in range(1, 6):
        while i < 6:
            number_client = int(input("Введите число от 1 до 10: "))
            color_client = int(input("Выберите цвет: введите  1 (красный) или 2(черный):"))

            if color_comp == 1:
                print(number_comp, "красный")
            elif color_comp == 2:
                print(number_comp, "черный")

            if number_comp == number_client and color_comp == color_client:
                return "Вы выиграли!!!"
            else:
                i = i + 1
                return "Ставка не выиграла(((("

print(simple_casino())

