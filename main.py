def bubble_sort(numbers, ascending=True):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if ascending:
                if numbers[j] > numbers[j + 1]:
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            else:
                if numbers[j] < numbers[j + 1]:
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

num_count = int(input("Введите количество чисел: "))

numbers = []
for _ in range(num_count):
    num = int(input("Введите число: "))
    numbers.append(num)

while True:
    sort_direction = input("Введите направление сортировки (введите 'возрастание' или 'убывание'): ").strip().lower()
    if sort_direction in ['возрастание', 'убывание']:
        break
    else:
        print("Ошибка: допустимы только 'возрастание' или 'убывание'. Попробуйте снова.")

ascending = sort_direction == "возрастание"

bubble_sort(numbers, ascending)

print("Отсортированный список:", numbers)
