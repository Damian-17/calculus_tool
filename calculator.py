print(" Калькулятор запущен!")
print("=" * 30)

# Простые функции калькулятора
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Ошибка: на ноль делить нельзя!"
    return a / b

# ВВОД ОТ ПОЛЬЗОВАТЕЛЯ
print("Введите два числа для вычислений:")
a = float(input("Первое число: "))
b = float(input("Второе число: "))

print("\nВыберите операцию:")
print("1 - Сложение")
print("2 - Вычитание") 
print("3 - Умножение")
print("4 - Деление")

choice = input("Ваш выбор (1-4): ")

if choice == '1':
    result = add(a, b)
    print(f" Результат: {a} + {b} = {result}")
elif choice == '2':
    result = subtract(a, b)
    print(f" Результат: {a} - {b} = {result}")
elif choice == '3':
    result = multiply(a, b)
    print(f" Результат: {a} * {b} = {result}")
elif choice == '4':
    result = divide(a, b)
    print(f"Результат: {a} / {b} = {result}")
else:
    print(" Неверный выбор операции!")

print("=" * 30)
print(" Программа завершена успешно!")

input("Нажмите Enter для выхода...")