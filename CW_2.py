from datetime import datetime

def input_array(prompt):
    while True:
        user_input = input(prompt).strip()
        try:
            # Преобразуем строку в список чисел
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


def find_a_repeated_in_b(array_a, array_b):
    "Находит элементы массива A, которые повторяются в массиве B несколько раз."
    repeated_in_b = [x for x in set(array_a) if array_b.count(x) > 1]
    return repeated_in_b


def log_analysis(array_a, array_b, repeated_in_b, only_in_a, only_in_b, repeated_a_in_b, log_format="standard"):
    if log_format == "standard":
        print("\n--- Анализ массивов ---")
        print(f"Массив A: {array_a}")
        print(f"Массив B: {array_b}")
        print("\nЭлементы массива B, которые повторяются, но в A только один раз:")
        for item in repeated_in_b:
            print(f"- {item}")
        print("\nЭлементы, которые есть только в массиве A:")
        for item in only_in_a:
            print(f"- {item}")
        print("\nЭлементы, которые есть только в массиве B:")
        for item in only_in_b:
            print(f"- {item}")
        print("\nЭлементы массива A, повторяющиеся в массиве B несколько раз:")
        for item in repeated_a_in_b:
            print(f"- {item}")
    elif log_format == "oneline":
        print(f"Анализ массивов: A={array_a}, B={array_b} | "
              f"Повторяются в B, но только в A: {repeated_in_b} | "
              f"Только в A: {only_in_a} | "
              f"Только в B: {only_in_b} | "
              f"A в B несколько раз: {repeated_a_in_b}")
    elif log_format == "oneline_with_date":
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] Анализ массивов: A={array_a}, B={array_b} | "
              f"Повторяются в B, но только в A: {repeated_in_b} | "
              f"Только в A: {only_in_a} | "
              f"Только в B: {only_in_b} | "
              f"A в B несколько раз: {repeated_a_in_b}")


def main():
    print("Анализ массивов A и B.")
    log_format = input("Выберите формат логов (standard, oneline, oneline_with_date): ").strip()

    array_a = []
    array_b = []

    while True:
        print("\nМеню:")
        print("1. Ввести массив A")
        print("2. Ввести массив B")
        print("3. Выполнить анализ массивов")
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

                # Элементы, которые есть только в A или только в B
                only_in_a, only_in_b = find_unique_elements(array_a, array_b)

                # Элементы массива A, которые повторяются в массиве B несколько раз
                repeated_a_in_b = find_a_repeated_in_b(array_a, array_b)

                # Вывод логов
                log_analysis(array_a, array_b, repeated_in_b, only_in_a, only_in_b, repeated_a_in_b, log_format)
        elif choice == '4':
            print("Выход из программы.")
            break
        else:
            print("Ошибка: выберите пункт меню от 1 до 4.")


if __name__ == "__main__":
    main()
