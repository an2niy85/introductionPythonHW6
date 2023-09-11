# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# Ввод: 7 2 5

# Вывод: 7 9 11 13 15


# def arithmetic_progression(first_element, step, count_elements):
#     data = [el for el in range(first_element,first_element + step * count_elements, step)]
#     print(data)

# print("Заполните массив элементами арифметической прогрессии.")
# first_element = int(input("Ее первый элемент: "))
# step = int(input("Разность: "))
# count_elements = int(input("Количество элементов: "))
# arithmetic_progression(first_element, step, count_elements)

a1, d, n = int(input()), int(input()), int(input())
progressive = [a1 + (i - 1)*d for i in range(1, n + 1)]
print(*progressive)

# a, d, n = map(int, input('a1 d n >>').split())
# p = [a + i * d for i in range(n)]