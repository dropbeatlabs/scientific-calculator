import math

# Output formatting mode
output_mode = 'normal'

def set_output_mode(mode_str):
    global output_mode
    if mode_str.lower() in ('normal', 'sci', 'eng'):
        output_mode = mode_str.lower()
        print(f"Number format set to {output_mode.upper()}")
    else:
        print("Invalid mode. Use: normal, sci, or eng.")

def format_number(x):
    if isinstance(x, str):
        return x
    if not isinstance(x, (float, int)):
        return str(x)
    # Normal
    if output_mode == 'normal':
        # Show up to 10 digits, remove trailing zeros
        return "{:.10g}".format(x)
    # Scientific
    elif output_mode == 'sci':
        return "{:.10E}".format(x)
    # Engineering
    elif output_mode == 'eng':
        if x == 0:
            return "0.0E+00"
        exp = int(math.floor(math.log10(abs(x))/3)*3)
        mant = x / (10**exp)
        return "{:.10f}E{:+03d}".format(mant, exp).rstrip('0').rstrip('.')
    else:
        # fallback
        return str(x)

# Arithmetic
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    else:
        return a / b

# Exponentials & roots
def power(a, b):
    try:
        return a ** b
    except Exception as e:
        return f"Error: {e}"

def natural_exp(x):
    return math.exp(x)

def sqrt(x):
    if x < 0:
        return "Error: Cannot take the square root of a negative number."
    else:
        return math.sqrt(x)

def root(x, n):
    if n == 0:
        return "Error: Zeroth root is undefined."
    if x < 0 and n % 2 == 0:
        return "Error: Cannot take an even root of a negative number (real result undefined)."
    try:
        return x ** (1/n)
    except Exception as e:
        return f"Error: {e}"

# Trigonometric functions
def sine(angle_deg):
    return math.sin(math.radians(angle_deg))
def cosine(angle_deg):
    return math.cos(math.radians(angle_deg))
def tangent(angle_deg):
    return math.tan(math.radians(angle_deg))
def cosecant(angle_deg):
    sin_val = math.sin(math.radians(angle_deg))
    if sin_val == 0:
        return "Error: Cosecant undefined for this angle (sin(angle) = 0)"
    else:
        return 1 / sin_val
def secant(angle_deg):
    cos_val = math.cos(math.radians(angle_deg))
    if cos_val == 0:
        return "Error: Secant undefined for this angle (cos(angle) = 0)"
    return 1 / cos_val
def cotangent(angle_deg):
    tan_val = math.tan(math.radians(angle_deg))
    if tan_val == 0:
        return "Error: Cotangent undefined for this angle (tan(angle) = 0)"
    else: 
        return 1 / tan_val

# Hyperbolic functions
def sinh(x):
    return math.sinh(x)
def cosh(x):
    return math.cosh(x)
def tanh(x):
    return math.tanh(x)
def csch(x):
    sinh_val = math.sinh(x)
    if sinh_val == 0:
        return "Error: Cosech undefined for x = 0"
    else: 
        return 1 / sinh_val
def sech(x):
    cosh_val = math.cosh(x)
    if cosh_val == 0:
        return "Error: Sech undefined for this x (cosh(x) = 0)"
    else: 
        return 1 / cosh_val
def coth(x):
    sinh_val = math.sinh(x)
    if sinh_val == 0:
        return "Error: Coth undefined for x = 0"
    else:
        return math.cosh(x) / sinh_val

# Inverse trigonometric functions
def arcsine(val):
    if val < -1 or val > 1:
        return "Error: Input out of domain for arcsin (must be between -1 and 1)"
    else:
        return math.degrees(math.asin(val))
def arccosine(val):
    if val < -1 or val > 1:
        return "Error: Input out of domain for arccos (must be between -1 and 1)"
    else:
        return math.degrees(math.acos(val))
def arctangent(val):
    return math.degrees(math.atan(val))
def arccosecant(val):
    if val == 0:
        return "Error: Arccosecant undefined for zero"
    elif abs(val) < 1:
        return "Error: Input out of domain for arccsc (|x| must be >= 1)"
    else:
        return math.degrees(math.asin(1/val))
def arcsecant(val):
    if val == 0:
        return "Error: Arcsecant undefined for zero"
    elif abs(val) < 1:
        return "Error: Input out of domain for arcsec (|x| must be >= 1)"
    else:
        return math.degrees(math.acos(1/val))
def arccotangent(val):
    if val == 0:
        return 90.0
    else:
        return math.degrees(math.atan(1/val))

# Inverse hyperbolic functions
def arsinh(x):
    return math.asinh(x)
def arcosh(x):
    if x < 1:
        return "Error: Input out of domain for arcosh (x must be >= 1)"
    else:
        return math.acosh(x)
def artanh(x):
    if x <= -1 or x >= 1:
        return "Error: Input out of domain for artanh (must be -1 < x < 1)"
    else:
        return math.atanh(x)

# Logarithm functions
def natural_log(x):
    if x <= 0:
        return "Error: Input for ln must be positive."
    else:
        return math.log(x)

def log_base_10(x):
    if x <= 0:
        return "Error: Input for log10 must be positive."
    else:
        return math.log10(x)

def log_base(x, base):
    if x <= 0:
        return "Error: Input for log must be positive."
    elif base <= 0 or base == 1:
        return "Error: Log base must be positive and not equal to 1."
    else: 
        return math.log(x, base)

def main():
    global output_mode

    print("=== Scientific Calculator ===")
    print("Available operations: add, subtract, multiply, divide")
    print("Exponentials and roots: power (^), exp, sqrt, root")
    print("Trigonometric: sin, cos, tan, csc, sec, cot")
    print("Inverse trig: arcsin, arccos, arctan, arccsc, arcsec, arccot")
    print("Hyperbolic: sinh, cosh, tanh, csch, sech, coth")
    print("Inverse hyperbolic: arsinh, arcosh, artanh")
    print("Logarithms: ln, log10, log")
    print("Number format: normal (default), sci (scientific), eng (engineering)")
    print("Type 'mode' to set number display (normal/sci/eng).")
    print("Type 'exit' to quit.\n")

    while True:
        op = input("Enter operation: ").strip().lower()

        if op == "exit":
            print("Goodbye!")
            break

        # Change number format interactively
        if op == "mode":
            new_mode = input("Enter number format (normal/sci/eng): ").strip().lower()
            set_output_mode(new_mode)
            continue

        elif op in ("add", "subtract", "multiply", "divide"):
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numbers.")
                continue
            if op == "add":
                result = add(a, b)
            elif op == "subtract":
                result = subtract(a, b)
            elif op == "multiply":
                result = multiply(a, b)
            elif op == "divide":
                result = divide(a, b)
            print("Result:", format_number(result))

        elif op in ("power", "^"):
            try:
                a = float(input("Enter the base: "))
                b = float(input("Enter the exponent: "))
            except ValueError:
                print("Invalid input. Please enter numbers.")
                continue
            result = power(a, b)
            print("Result:", format_number(result))

        elif op == "exp":
            try:
                x = float(input("Enter exponent for e^x: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            result = natural_exp(x)
            print("Result:", format_number(result))

        elif op == "sqrt":
            try:
                x = float(input("Enter value for square root: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            result = sqrt(x)
            print("Result:", format_number(result))

        elif op == "root":
            try:
                x = float(input("Enter the value: "))
                n = float(input("Enter the degree of the root (n): "))
            except ValueError:
                print("Invalid input. Please enter numbers.")
                continue
            result = root(x, n)
            print("Result:", format_number(result))

        elif op in ("sin", "cos", "tan", "csc", "sec", "cot"):
            try:
                angle = float(input("Enter angle in degrees: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            if op == "sin":
                result = sine(angle)
            elif op == "cos":
                result = cosine(angle)
            elif op == "tan":
                result = tangent(angle)
            elif op == "csc":
                result = cosecant(angle)
            elif op == "sec":
                result = secant(angle)
            elif op == "cot":
                result = cotangent(angle)
            print("Result:", format_number(result))

        elif op in ("arcsin", "arccos", "arctan", "arccsc", "arcsec", "arccot"):
            try:
                val = float(input("Enter value: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            if op == "arcsin":
                result = arcsine(val)
            elif op == "arccos":
                result = arccosine(val)
            elif op == "arctan":
                result = arctangent(val)
            elif op == "arccsc":
                result = arccosecant(val)
            elif op == "arcsec":
                result = arcsecant(val)
            elif op == "arccot":
                result = arccotangent(val)
            print("Result (in degrees):", format_number(result))

        elif op in ("sinh", "cosh", "tanh", "csch", "sech", "coth"):
            try:
                x = float(input("Enter value: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            if op == "sinh":
                result = sinh(x)
            elif op == "cosh":
                result = cosh(x)
            elif op == "tanh":
                result = tanh(x)
            elif op == "csch":
                result = csch(x)
            elif op == "sech":
                result = sech(x)
            elif op == "coth":
                result = coth(x)
            print("Result:", format_number(result))

        elif op in ("arsinh", "arcosh", "artanh"):
            try:
                x = float(input("Enter value: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            if op == "arsinh":
                result = arsinh(x)
            elif op == "arcosh":
                result = arcosh(x)
            elif op == "artanh":
                result = artanh(x)
            print("Result:", format_number(result))

        elif op == "ln":
            try:
                x = float(input("Enter the value for ln(x): "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            result = natural_log(x)
            print("Result:", format_number(result))

        elif op == "log10":
            try:
                x = float(input("Enter the value for log10(x): "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            result = log_base_10(x)
            print("Result:", format_number(result))

        elif op == "log":
            try:
                x = float(input("Enter the value for log(x, base): "))
                base = float(input("Enter the base: "))
            except ValueError:
                print("Invalid input. Please enter numbers.")
                continue
            result = log_base(x, base)
            print("Result:", format_number(result))

        else:
            print("Unknown operation. Try again.")

if __name__ == "__main__":
    main()
