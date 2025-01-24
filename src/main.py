from utils import minus_numbers, degree_numbers, add_numbers, multiply_numbers


def main():
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    minys_result = minus_numbers(num1, num2)
    print(f"Разность чисел: {minys_result}")

    degree_result = degree_numbers(num1, num2)
    print(f"Число в степени: {degree_result}")

    sum_result = add_numbers(num1, num2)
    print(f"Сумма чисел: {sum_result}")

    multiply_result = multiply_numbers(num1, num2)
    print(f"Произведение числе: {multiply_result}")



if __name__ == "__main__":
    main()
