def multiply(x, y):
    return x * y


def add(x, y):
    return x + y


def divide(x, y):
    if y == 0:
        print("y can't be zero!")
    else:
        return x / y


def subtract(x, y):
    return x - y


if __name__ == "__main__":
    print(multiply(10, 5))
