from utils import minus_numbers, degree_numbers


def main():
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    minys_result = minus_numbers(num1, num2)
    print(f"Разность чисел: {minys_result}")

    degree_result = degree_numbers(num1, num2)
    print(f"Число в степени: {degree_result}")



if __name__ == "__main__":
    main()
