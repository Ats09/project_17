while True:
    user_input = input("Введите число: ")
    try:
        element_int = int(user_input)
        break  # выходим из цикла при корректном вводе числа
    except ValueError:
        print("Ошибка: введите целое число")

num_list = input("Введите последовательность чисел через пробел: ").split()
try:
    num_list = [int(num) for num in num_list]
except ValueError:
    print("Ошибка: последовательность должна состоять только из целых чисел")

for i in range(len(num_list)):  # Сортировка по возрастанию
    for j in range(len(num_list) - i - 1):
        if num_list[j] > num_list[j + 1]:
            num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]

print("Отсортированная последовательность чисел: ", num_list)


def binary_search(lst, element, left, right):
    if left > right:
        return "Данное число не найдено"

    middle = (right + left) // 2
    if lst[middle] == element:
        return middle
    elif element < lst[middle]:
        return binary_search(lst, element, left, middle - 1)
    else:
        return binary_search(lst, element, middle + 1, right)


print("Позиция введенного числа: ", binary_search(num_list, element_int, 0, len(num_list)-1))
