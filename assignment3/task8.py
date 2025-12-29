# Задание 8.

# 1. Найдите все натуральные числа, 
# не превышающие заданное n, которые делятся на каждую из своих цифр.

# 2. Введите одномерный массив A длиной m. 
# Поменяйте местами первый и последний элементы массива. 
# Введите длину массива и его элементы с клавиатуры. В программе опишите процедуру замены элементов массива. 
# Выведите исходный и результирующий массивы.

def check_divisibility(number):
    """
    Проверяет, делится ли число на все свои цифры.
    Возвращает True, если подходит, иначе False.
    """
    original_num = number
    temp_num = number
    
    # Способ через математику (без конвертации в строку)
    # Разбиваем число на цифры с помощью % 10 и // 10
    while temp_num > 0:
        digit = temp_num % 10 # Берем последнюю цифру
        
        # 1. Проверка на ноль (на 0 делить нельзя)
        if digit == 0:
            return False
            
        # 2. Проверка делимости
        if original_num % digit != 0:
            return False
            
        temp_num = temp_num // 10 # Отбрасываем последнюю цифру
        
    return True

def swap_first_last(arr):
    """
    Процедура, которая меняет местами первый и последний элементы.
    Изменяет массив на месте (in-place).
    """
    if len(arr) < 2:
        return # Если массив пустой или из 1 элемента, менять нечего
    
    # Классический обмен через временную переменную (как в Си/Java)
    # first_val = arr[0]
    # arr[0] = arr[-1]
    # arr[-1] = first_val
    
    # Pythonic way (Быстрый обмен):
    arr[0], arr[-1] = arr[-1], arr[0]


#АДАЧА 1:ЧИСЛА И ЦИФРЫ
def solve_digits_divisibility():
    print("\n=== ЧАСТЬ 1: Числа, делящиеся на свои цифры ===")
    try:
        n = int(input("Введите число n: "))
        
        print(f"Числа <= {n}, которые делятся на свои цифры:")
        
        # Перебираем все числа от 1 до n
        for i in range(1, n + 1):
            if check_divisibility(i):
                print(i, end=" ")
        print() # Перенос строки в конце
        
    except ValueError:
        print("Ошибка: введите целое число.")

#ЗАДАЧА 2:МАССИВ
def solve_array_swap():
    print("\n=== ЧАСТЬ 2: Обмен первого и последнего элементов ===")
    try:
        # Ввод длины и элементов
        m = int(input("Введите длину массива (m): "))
        
        if m <= 0:
            print("Массив должен быть длиной хотя бы 1.")
            return

        print(f"Введите {m} чисел через Enter:")
        my_array = []
        for i in range(m):
            val = int(input(f"  Элемент {i+1}: "))
            my_array.append(val)
            
        print(f"\nИсходный массив: {my_array}")
        
        # Вызов процедуры замены
        swap_first_last(my_array)
        
        print(f"Результат:       {my_array}")
        
    except ValueError:
        print("Ошибка при вводе чисел.")

def main():
    solve_digits_divisibility()
    print("-" * 30)
    solve_array_swap()

if __name__ == "__main__":
    main()
