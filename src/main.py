#ипорт функций
from utils import minus_numbers, degree_numbers,  multiply_numbers


def main():
    #ввод чисел
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
#вызов функции разности чисед
    minys_result = minus_numbers(num1, num2)
    print(f"Разность чисел: {minys_result}")
#вызов функции возведения в степень
    degree_result = degree_numbers(num1, num2)
    print(f"Число в степени: {degree_result}")
#вызов функции произведения чисел
    multiply_result = multiply_numbers(num1, num2)
    print(f"Произведение числе: {multiply_result}")



if __name__ == "__main__":
    main()
