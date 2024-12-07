import argparse
import math

def calculate_perimeter(base1, base2, height):
    # Вычисляем длину боковых сторон по теореме Пфагора
    half_difference = (base1 - base2) / 2
    side_length = math.sqrt(height**2 + half_difference**2)

    # Периметр равнобедренной трапеции
    perimeter = base1 + base2 + 2 * side_length
    return perimeter

if __name__ == "__main__":
    # Создаем парсер для аргументов командной строки
    parser = argparse.ArgumentParser(description="Вычислить периметр трапеции.")

    # Добавляем аргументы
    parser.add_argument("base1", type=float)
    parser.add_argument("base2", type=float)
    parser.add_argument("height", type=float)

    # Парсим аргументы
    args = parser.parse_args()

    # Вычисляем периметр
    perimeter = calculate_perimeter(args.base1, args.base2, args.height)

    print(f"Периметр трапеции: {perimeter:.2f}")

    input("Нажмите Enter для выхода...")