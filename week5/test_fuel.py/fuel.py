def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))


def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)

    if y == 0:
        raise ZeroDivisionError

    if x < 0 or y < 0 or x > y:
        raise ValueError

    return int(x / y * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{int(percentage)}%"


if __name__ == "__main__":
    main()