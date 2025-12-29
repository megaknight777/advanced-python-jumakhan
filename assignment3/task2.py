# Задание 2.
# 1. Вычислите площадь правильного шестиугольника со стороной a,
# используя подпрограмму вычисления площади треугольника.
# 2. Пользователь вводит две стороны трех прямоугольников. Выведите их площади.

import math

# --- ПОДПРОГРАММА 1: Площадь равностороннего треугольника ---
# В задании сказано использовать "triangle area subroutine". Вот она.
def calculate_triangle_area(side):
    # Формула: (корень из 3 / 4) * сторона в квадрате
    area = (math.sqrt(3) / 4) * (side ** 2)
    return area

# --- ПОДПРОГРАММА 2: Площадь прямоугольника ---
def calculate_rectangle_area(a, b):
    return a * b

# --- ОСНОВНАЯ ЛОГИКА ---
def solve_hexagon_task():
    print("\n=== Часть 1: Гексагон (Шестиугольник) ===")
    a = float(input("Введите длину стороны шестиугольника (a): "))
    
    # ЛОГИКА: Гексагон = 6 треугольников
    # Мы вызываем нашу подпрограмму для одного треугольника
    one_triangle_area = calculate_triangle_area(a)
    
    # И умножаем результат на 6
    hexagon_area = 6 * one_triangle_area
    
    print(f"Площадь одного треугольника: {one_triangle_area:.2f}")
    print(f"Площадь шестиугольника: {hexagon_area:.2f}")

def solve_rectangles_task():
    print("\n=== Часть 2: Три прямоугольника ===")
    
    # Нам нужно повторить действие 3 раза. Используем цикл.
    # range(3) означает: повторить 0, 1, 2 (всего 3 раза)
    for i in range(1, 4):
        print(f"\n--- Прямоугольник №{i} ---")
        width = float(input("Введите сторону 1: "))
        height = float(input("Введите сторону 2: "))
        
        area = calculate_rectangle_area(width, height)
        print(f"Площадь прямоугольника {i}: {area:.2f}")

# --- ТОЧКА ВХОДА ---
def main():
    solve_hexagon_task()
    solve_rectangles_task()

if __name__ == "__main__":
    main()
