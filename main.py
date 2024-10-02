def bubble_sort(numbers):
    n = len(numbers)
    # Проходим по всем элементам
    for i in range(n):
        # Внутренний цикл для сравнения соседних элементов
        for j in range(0, n - i - 1):
            # Если текущий элемент больше следующего, меняем их местами
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# Запрашиваем количество чисел
num_count = int(input("Введите количество чисел: "))

# Запрашиваем сами числа
numbers = []
for _ in range(num_count):
    num = int(input("Введите число: "))
    numbers.append(num)

# Сортировка списка
bubble_sort(numbers)

# Вывод отсортированного списка
print("Отсортированный список:", numbers)
