# Шаг 1
def divide_numbers(a, b):
    return a / b

def get_list_element(lst, index):
    return lst[index]

# Шаг 2
def calculate_square_root(x):
    try:
        if x < 0:
            raise ValueError("Квадратный корень из отрицательного числа невозможен.")
        return x ** 0.5
    except Exception as e:
        print(f"Ошибка: {e}")
        return None

# Шаг 3
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return None
    finally:
        print("Операция чтения файла завершена.")

# Шаг 4
def advanced_math_operations(a, b):
    try:
        result = a / b
        assert a > 0 and b > 0, "Оба числа должны быть положительными."
        return result
    except ZeroDivisionError as zde:
        print(f"Ошибка деления на ноль: {zde}")
    except AssertionError as ae:
        print(f"Ошибка утверждения: {ae}")
    except Exception as e:
        print(f"Общая ошибка: {e}")
    finally:
        print("Операция завершена.")

# Шаг 5
def generate_and_handle_exceptions(value):
    try:
        if value == 0:
            raise ZeroDivisionError("Недопустимое значение: 0.")
        elif value < 0:
            raise ValueError("Значение не должно быть отрицательным.")
        else:
            print(f"Значение корректное: {value}")
    except ZeroDivisionError as zde:
        print(f"Ошибка деления: {zde}")
    except ValueError as ve:
        print(f"Неправильное значение: {ve}")
    finally:
        print("Обработка завершена.")

# Шаг 6: Пользовательские исключения
class CustomError(Exception):
    pass

class NegativeValueError(CustomError):
    def __init__(self, message="Значение не должно быть отрицательным"):
        self.message = message
        super().__init__(self.message)

class DivisionByZeroError(CustomError):
    def __init__(self, message="Деление на ноль недопустимо"):
        self.message = message
        super().__init__(self.message)

# Шаг 7
def check_value(value):
    try:
        if value < 0:
            raise NegativeValueError()
        elif value == 0:
            raise DivisionByZeroError()
        print(f"Значение корректное: {value}")
    except CustomError as ce:
        print(f"Пользовательское исключение: {ce}")
    finally:
        print("Проверка значения завершена.")

# Шаг 8: Дополнительные функции
def add_positive_numbers(a, b):
    try:
        if a < 0 or b < 0:
            raise NegativeValueError("Оба числа должны быть положительными.")
        return a + b
    except NegativeValueError as ne:
        print(f"Ошибка: {ne}")

def subtract_values(a, b):
    try:
        return a - b
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def multiply_values(a, b):
    try:
        if b == 0:
            raise DivisionByZeroError("Множитель не может быть равен нулю.")
        return a * b
    except DivisionByZeroError as de:
        print(f"Ошибка: {de}")
