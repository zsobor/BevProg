def division(a, b):
    try:
        result = a / b
        print(result)
    except ZeroDivisionError:
        print("Division by zero is not allowed")
    finally:
        print("Out of try except block")


if __name__ == "__main__":
    while True:
        a = int(input("enter 'a' value: "))
        b = int(input("enter 'b' value: "))
        division(a, b)