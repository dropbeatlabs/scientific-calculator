class ScientificCalculator:
    def __init__(self):
        pass

    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        if y != 0:
            return x / y
        else:
            return "Error: Division by zero"

    @staticmethod
    def power(base, exp):
        return base ** exp

    @staticmethod
    def sqrt(x):
        return x ** 0.5

    @staticmethod
    def sin(x):
        import math
        return math.sin(math.radians(x))

    @staticmethod
    def cos(x):
        import math
        return math.cos(math.radians(x))

    @staticmethod
    def tan(x):
        import math
        return math.tan(math.radians(x))

    @staticmethod
    def sinh(x):
        import math
        return math.sinh(x)

    @staticmethod
    def cosh(x):
        import math
        return math.cosh(x)

    @staticmethod
    def tanh(x):
        import math
        return math.tanh(x)

    @staticmethod
    def arcsin(x):
        import math
        return math.degrees(math.asin(x))

    @staticmethod
    def arccos(x):
        import math
        return math.degrees(math.acos(x))

    @staticmethod
    def arctan(x):
        import math
        return math.degrees(math.atan(x))

    @staticmethod
    def exp(x):
        import math
        return math.exp(x)

    @staticmethod
    def log(x, base=10):
        import math
        if base == 'e':
            return math.log(x)
        else:
            return math.log(x, base)

    @staticmethod
    def scientific_notation(value):
        return f'{value:.6e}'

    @staticmethod
    def engineering_notation(value):
        exponent = 0
        while abs(value) >= 1000:
            value /= 1000
            exponent += 1
        while abs(value) < 1 and value != 0:
            value *= 1000
            exponent -= 1
        return f'{value:.6f} x 10^{exponent}'

# Example usage:
if __name__ == '__main__':
    calc = ScientificCalculator()
    print("Addition:", calc.add(5, 3))
    print("Square root:", calc.sqrt(16))
    print("Sine:", calc.sin(30))
    print("Scientific Notation:", calc.scientific_notation(1234567))
    print("Engineering Notation:", calc.engineering_notation(1234567))