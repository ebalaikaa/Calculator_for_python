def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Выберите операцию:")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")

choice = input("Введите номер операции (1/2/3/4): ")

num1 = input("Введите первое число: ")
if num1.isalpha():
    print("Это не число")
    num1 = float(input("Введите первое число: "))
else:
    num1 = float(num1)
num2 = input("Введите второе число: ")
if num2.isalpha():
    print("Это не число")
    num2 = float(input("Введите второе число: "))
else:
    num2 = float(num2)

if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Некорректный выбор операции")
