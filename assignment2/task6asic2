def all_eq(lst):
    # ШАГ 1: Находим максимальную длину
    max_len = 0
    for s in lst:
        if len(s) > max_len:
            max_len = len(s)

    # ШАГ 2: Создаем новый список и заполняем его
    new_list = []

    for s in lst:
        # Считаем, сколько не хватает до максимума
        diff = max_len - len(s)

        # В Python можно умножать строку на число!
        # "_" * 3 превратится в "___"
        new_s = s + "_" * diff

        new_list.append(new_s)

    return new_list


# Тестируем
input_list = ["a", "aa", "aaaaa", "zz"]
print(all_eq(input_list))
