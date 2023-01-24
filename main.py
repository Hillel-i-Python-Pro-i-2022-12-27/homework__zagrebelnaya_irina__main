import random


def random_choice() -> str:
    """random_choice return"""
    array = ["2", "109", "False", "10", "Lorem", "482", "Ipsum"]
    return random.choice(array)


def print_value() -> str:
    result = random_choice()
    return f"Your random choice is {result}!"


def main() -> None:
    print(print_value())


if __name__ == "__main__":
    main()
