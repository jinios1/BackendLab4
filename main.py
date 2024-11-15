from funcend import (
    divide_numbers, get_list_element, calculate_square_root, read_file,
    advanced_math_operations, generate_and_handle_exceptions, check_value,
    add_positive_numbers, subtract_values, multiply_values
)

if __name__ == "__main__":
    try:
        print(divide_numbers(10, 0))
    except Exception as e:
        print(f"Обработанная ошибка: {e}")

    try:
        print(get_list_element([1, 2, 3], 5))
    except Exception as e:
        print(f"Обработанная ошибка: {e}")

    print(calculate_square_root(-4))
    print(read_file("non_existent_file.txt"))
    print(advanced_math_operations(10, 0))
    generate_and_handle_exceptions(-5)
    check_value(-10)

    print(add_positive_numbers(-5, 3))
    print(subtract_values(10, 5))
    print(multiply_values(5, 0))
