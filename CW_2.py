def input_array(prompt):
    while True:
        user_input = input(prompt).strip()
        try:
            array = list(map(int, user_input.split(',')))
            return array
        except ValueError:
            print("Ошибка: введите числа, разделённые запятыми. Пример: 1,2,3,4")


def find_repeated_in_b(array_a, array_b):
    "Находит повторяющиеся элементы массива B, которые в A встречаются только один раз."
    count_in_a = {x: array_a.count(x) for x in array_a}
    result = []
    for x in set(array_b):
        if array_b.count(x) > 1 and count_in_a.get(x, 0) == 1:
            result.append(x)
    return result

def find_unique_elements(array_a, array_b):
    "Находит элементы, которые есть только в массиве A или только в массиве B."
    only_in_a = [x for x in array_a if x not in array_b]
    only_in_b = [x for x in array_b if x not in array_a]
    return only_in_a, only_in_b

def main():
    print("Анализ массивов A и B.")

    array_a = []
    array_b = []

    while True:
        print("\nМеню:")
        print("1. Ввести массив A")
        print("2. Ввести массив B")
        print("3. Проанализировать массивы")
        print("4. Выход")

        choice = input("Выберите пункт меню (1-4): ").strip()

        if choice == '1':
            array_a = input_array("Введите массив A (числа через запятую): ")
            print(f"Массив A: {array_a}")
        elif choice == '2':
            array_b = input_array("Введите массив B (числа через запятую): ")
            print(f"Массив B: {array_b}")
        elif choice == '3':
            if not array_a or not array_b:
                print("Ошибка: сначала введите массивы A и B.")
            else:
                # Повторяющиеся элементы массива B, которые в A только один раз
                repeated_in_b = find_repeated_in_b(array_a, array_b)
                print(f"Элементы массива B, которые повторяются, но в A ровно один раз: {repeated_in_b}" if repeated_in_b else "Таких элементов нет.")

                # Элементы, которые есть только в A или только в B
                only_in_a, only_in_b = find_unique_elements(array_a, array_b)
                print(f"Элементы, которые есть только в массиве A: {only_in_a}" if only_in_a else "Таких элементов в A нет.")
                print(f"Элементы, которые есть только в массиве B: {only_in_b}" if only_in_b else "Таких элементов в B нет.")
        elif choice == '4':
            print("Выход из программы.")
            break
        else:
            print("Ошибка: выберите пункт меню от 1 до 4.")


if __name__ == "__main__":
    main()
