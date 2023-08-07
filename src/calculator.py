import random


class Calculator:
    """A basic calculator class with addition and multiplication operations."""
    def __init__(self):
        pass

    def add(self, a, b):
        """Add two numbers.

        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The sum of the two numbers.
        """
        return a + b

    def multiply(self, a, b):
        """Multiply two numbers.

        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The product of the two numbers.
        """
        return a * b


def generate_random_numbers(count):
    """Generate a list of random numbers.

    Args:
        count (int): The number of random numbers to generate.

    Returns:
        list: A list of randomly generated numbers.
    """
    return [random.randint(1, 100) for _ in range(count)]


if __name__ == "__main__":
    calc = Calculator()
    num1 = 10
    num2 = 5

    result_add = calc.add(num1, num2)
    result_multiply = calc.multiply(num1, num2)

    print(f"Adding {num1} and {num2}: {result_add}")
    print(f"Multiplying {num1} and {num2}: {result_multiply}")

    random_numbers = generate_random_numbers(5)
    print("Generated random numbers:", random_numbers)
