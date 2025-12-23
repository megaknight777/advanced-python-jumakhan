# Определяем разрешенные символы
valid_letters = "ABCEHKMOPTXY"
valid_digits = "0123456789"

# 1. Считываем количество номеров
n = int(input())

# 2. Запускаем цикл для проверки каждого номера
for i in range(n):
    plate = input()  # Считываем строку (номер)

    # ПРОВЕРКА 1: Длина должна быть ровно 6
    if len(plate) != 6:
        print("No")
        continue  # continue пропускает остальной код и начинает следующий круг цикла

    # ПРОВЕРКА 2: Смотрим каждый символ по местам
    # Формат: Буква (0), Цифра (1), Цифра (2), Цифра (3), Буква (4), Буква (5)

    is_valid = True  # Предполагаем, что номер правильный

    # Проверяем буквы на местах 0, 4, 5
    if plate[0] not in valid_letters:
        is_valid = False
    elif plate[4] not in valid_letters:
        is_valid = False
    elif plate[5] not in valid_letters:
        is_valid = False

    # Проверяем цифры на местах 1, 2, 3
    elif plate[1] not in valid_digits:
        is_valid = False
    elif plate[2] not in valid_digits:
        is_valid = False
    elif plate[3] not in valid_digits:
        is_valid = False

    # Выводим итог
    if is_valid:
        print("Yes")
    else:
        print("No")
