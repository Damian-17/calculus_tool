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

# Тестируем и выводим результаты
print("Тестируем функции:")
print(f"5 + 3 = {add(5, 3)}")
print(f"10 - 4 = {subtract(10, 4)}")  
print(f"6 * 7 = {multiply(6, 7)}")
print(f"15 / 3 = {divide(15, 3)}")
print(f"Попытка деления на ноль: {divide(10, 0)}")

print("=" * 30)
print(" Программа завершена успешно!")


input("Нажмите Enter для выхода...")
