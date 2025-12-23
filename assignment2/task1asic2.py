# You are given a sequence consisting only of the characters ‘>’, ‘<’, and ‘-’.
# Your goal is to find the number of arrows hidden in this sequence.
# Arrows are substrings of the form ‘>>-->’ and ‘<--<<’.
# Input Data contains a string consisting of the characters '>', '<', and '-' (without
# spaces).
# The string must be no more than 250 characters long.

sequence = "<<<<>>--><--<<--<<>>>--><<<<<"
count = 0
arrow1 = ">>-->"
arrow2 = "<--<<"
length = len(sequence)
arrow_len = len(arrow1)  # длина обеих стрелок равна 5

max_length=250 # максимальная длина не должна быть больше этого числа

if length > max_length:
    print(f"the length is long")
    exit() # программа завершается

# Мы идем циклом не по символам, а по индексам, до тех пор, пока
# у нас хватает символов для формирования полной стрелки
for i in range(length - arrow_len + 1):
    # Берем "окно" из 5 символов, начиная с индекса i
    substring = sequence[i: i + arrow_len]

    # Проверяем, является ли это "окно" одной из наших стрелок
    if substring == arrow1 or substring == arrow2:
        count += 1

# Когда мы используем такой цикл, мы автоматически учитываем
# все возможные перекрытия.

print(f"Общее количество стрелок: {count}")
