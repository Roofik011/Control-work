import argparse
import math

def calculate_perimeter(base1, base2, height):
    # Вычисляем длину боковых сторон по теореме Пифагора
    half_difference = (base1 - base2) / 2
    side_length = math.sqrt(height**2 + half_difference**2)

    # Периметр равнобедренной трапеции
    perimeter = base1 + base2 + 2 * side_length
    return perimeter

def validate_inputs(base1, base2, height):
    # Проверка, что основания и высота положительные
    if base1 <= 0 or base2 <= 0 or height <= 0:
        raise ValueError("Основания и высота должны быть положительными числами.")

    # Проверка на разницу между основаниями
    if abs(base1 - base2) < 1e-9:
        raise ValueError("Основания трапеции не должны быть равными." )

if __name__ == "__main__":
    # Создаем парсер для аргументов командной строки
    parser = argparse.ArgumentParser(description="Вычислить периметр трапеции.")

    # Добавляем аргументы
    parser.add_argument("base1", type=float)
    parser.add_argument("base2", type=float)
    parser.add_argument("height", type=float)

    # Парсим аргументы
    args = parser.parse_args()

    try:
        # Проверяем входные данные
        validate_inputs(args.base1, args.base2, args.height)

        # Вычисляем периметр
        perimeter = calculate_perimeter(args.base1, args.base2, args.height)

        print(f"Периметр трапеции: {perimeter:.2f}")
    except ValueError as e:
        print(f"Ошибка: {e}")

    input("Нажмите Enter для выхода...")
