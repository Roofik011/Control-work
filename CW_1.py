import argparse
import math

def calculate_perimeter(base1, base2, height):
    half_difference = (base1 - base2) / 2
    side_length = math.sqrt(height**2 + half_difference**2)

    perimeter = base1 + base2 + 2 * side_length
    return perimeter

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Вычисляем периметр.")

    parser.add_argument("base1", type=float, help="Первое основание трапеции")
    parser.add_argument("base2", type=float, help="Второе основание трапеции")
    parser.add_argument("height", type=float, help="Высота трапеции")

    args = parser.parse_args()

    perimeter = calculate_perimeter(args.base1, args.base2, args.height)

    print(f"Периметр трапеции: {perimeter:.2f}")
    input("Нажмите Enter для выхода...")