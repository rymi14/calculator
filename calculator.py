"""
Python Calculator
-----------------
Interactive console calculator organized in 5 sections:
basic operations, powers and roots, trigonometric functions,
exponential/logarithmic functions and additional operations.

Every input goes through a validator that re-asks on error,
so invalid data never reaches the math.
"""

import math

# Translation table: digits and '-'/'.' -> superscript characters (2^0.5 -> 2⁰·⁵)
SUPERSCRIPTS = str.maketrans("0123456789-.", "⁰¹²³⁴⁵⁶⁷⁸⁹⁻·")

#------------------------------------------------------------------------------------------
# Exceptions
#------------------------------------------------------------------------------------------
def correct_option(option: str) -> int:
    """Convert the option to int; raise if it is not an integer."""
    try:
        value = int(option)
    except ValueError:
        # from None: hide the internal chained exception, show only our message.
        raise ValueError(f"`{option}` is not an integer.") from None

    return value


def integer(x: str) -> int:
    """Convert x to int; raise if it is not an integer."""
    try:
        number = int(x)
    except ValueError:
        raise ValueError(f"`{x}` is not an integer.") from None
    return number


def no_negative_integer(x: str) -> int:
    """Convert x to int; raise if it is not an integer or is negative."""
    try:
        number = int(x)
    except ValueError:
        raise ValueError(f"`{x}` is not an integer.") from None
    if number < 0:
        raise ValueError("The value must be 0 or higher.")
    return number


def numbers(x: str) -> float:
    """Convert x to float; raise if it is not a number or is NaN/inf."""
    try:
        number = float(x)
    except ValueError:
        raise ValueError(f"`{x}` is not a number.") from None
    if math.isnan(number) or math.isinf(number):
        raise ValueError(f"`{x}` is not a valid number.")
    return number


def not_zero(x: str) -> float:
    """Convert x to float; raise if it is not a number or is 0."""
    try:
        number = float(x)
    except ValueError:
        raise ValueError(f"`{x}` is not a number.") from None
    if number == 0:
        raise ValueError("A value other than 0 is required.")
    return number


def no_negative_numbers(x: str) -> float:
    """Convert x to float; raise if it is not a number or is negative."""
    try:
        number = float(x)
    except ValueError:
        raise ValueError(f"`{x}` is not a number.") from None
    if number < 0:
        raise ValueError("The value must be 0 or higher.")
    return number


def strictly_positive(x: str) -> float:
    """Convert x to float; raise if it is not a number or is <= 0."""
    try:
        number = float(x)
    except ValueError:
        raise ValueError(f"`{x}` is not a number.") from None
    if number <= 0:
        raise ValueError("The value must be positive.")
    return number


#------------------------------------------------------------------------------------------
# Ask for input
#------------------------------------------------------------------------------------------
def ask_option(prompt: str) -> int:
    """Ask until the user enters an integer option."""
    while True:
        try:
            value = correct_option(input(prompt))
            return value
        except ValueError as ve:
            print(f"{ve} Try again.")


def ask_integer(prompt: str) -> int:
    """Ask until the user enters an integer."""
    while True:
        try:
            value = integer(input(prompt))
            return value
        except ValueError as ve:
            print(f"{ve} Try again.")


def ask_positive_integer(prompt: str, avoid_negative: bool) -> int:
    """Ask for an int. If avoid_negative is True, values < 0 are rejected."""
    while True:
        try:
            value = integer(input(prompt))
            if avoid_negative:
                no_negative_integer(value)
            return value
        except ValueError as ve:
            print(f"{ve} Try again.")


def ask_number(prompt: str) -> float:
    """Ask until the user enters a valid number (not NaN/inf)."""
    while True:
        try:
            value = numbers(input(prompt))
            return value
        except ValueError as ve:
            print(f"{ve} Try again.")


def ask_not_zero_number(prompt: str, avoid_zero: bool) -> float:
    """Ask for a float. If avoid_zero is True, 0 is rejected."""
    while True:
        try:
            value = numbers(input(prompt))
            if avoid_zero:
                not_zero(value)
            return value
        except ValueError as ve:
            print(f"{ve} Try again.")


def ask_positive_number(prompt: str, avoid_negative: bool) -> float:
    """Ask for a float. If avoid_negative is True, values < 0 are rejected."""
    while True:
        try:
            value = numbers(input(prompt))
            if avoid_negative:
                no_negative_numbers(value)
            return value
        except ValueError as ve:
            print(f"{ve} Try again.")


def ask_strictly_positive_number(prompt: str, avoid_negative: bool) -> float:
    """Ask for a float. If avoid_negative is True, values <= 0 are rejected."""
    while True:
        try:
            value = numbers(input(prompt))
            if avoid_negative:
                strictly_positive(value)
            return value
        except ValueError as ve:
            print(f"{ve} Try again.")


#------------------------------------------------------------------------------------------
# Options
#------------------------------------------------------------------------------------------

# --------------- 1. Basic operations ---------------
def basic_operations():
    operations = {
        1: ("+", "add", lambda a, b: a + b),
        2: ("-", "subtract", lambda a, b: a - b),
        3: ("*", "multiply", lambda a, b: a * b)
    }

    print(
        "----------------------------------\n"
        "         BASIC OPERATIONS         \n"
        "----------------------------------\n"
        "Enter 0 to go back to the main menu."
    )

    while True:
        print(
            "\n1. Addition\n"
            "2. Subtraction\n"
            "3. Multiplication\n"
            "4. Division\n"
            "0. Exit\n\n"
        )

        option = ask_option("Select the basic operation: ")

        if option == 0:
            print("\nBack to the main menu.")
            break
        elif option == 4:
            a = ask_number("Enter dividend number: ")
            b = ask_not_zero_number("Enter divisor number: ", avoid_zero=True)
            print(f"\n{a} / {b} = {a / b}")
        elif option in operations:
            symbol, verb, operation = operations[option]
            a = ask_number(f"First number to {verb}: ")
            b = ask_number(f"Second number to {verb}: ")
            print(f"\n{a} {symbol} {b} = {operation(a, b)}")
        else:
            print("Incorrect option.\n")


# --------------- 2. Powers and roots ---------------
def powers():
    def exp(a: float, n: float) -> float:
        return a ** n

    print(
        "----------------------------------\n"
        "         POWERS AND ROOTS         \n"
        "----------------------------------\n"
        "Enter 0 to go back to the main menu."
    )

    while True:
        print(
            "\n1. Power -> aⁿ\n"
            "2. Square root -> √a\n"
            "3. Cube root -> ∛a\n"
            "4. nth root -> ⁿ√a\n"
            "0. Exit\n\n"
        )

        option = ask_option("Select the operation: ")

        try:
            if option == 0:
                print("\nBack to the main menu.")
                break
            elif option == 1:
                a = ask_number("Enter the base (a): ")
                n = ask_number("Enter the exponent (n): ")
                result = exp(a, n)
                # Python returns a complex number instead of raising: (-8)**0.5
                # This calculator only supports real results, so reject it here.
                if isinstance(result, complex):
                    raise ValueError(
                        f"Error: {a}^{n} is not a real number.\n"
                        "Complex numbers are not supported."
                    )
                print(f"\n{a}^{str(n).translate(SUPERSCRIPTS)} = {result}")
            elif option == 2:
                a = ask_positive_number("Enter the base (a): ", avoid_negative=True)
                result = exp(a, 1 / 2)
                print(f"\n√{a} = {result}")
            elif option == 3:
                a = ask_number("Enter the base (a): ")
                if a < 0:
                    result = exp(abs(a), 1 / 3)
                    print(f"\n∛{a} = {-1 * result}")
                else:
                    result = exp(a, 1 / 3)
                    print(f"\n∛{a} = {result}")
            elif option == 4:
                a = ask_number("Enter the radicand (a): ")
                n = ask_integer("Enter the root index (n): ")

                if n == 0:
                    raise ValueError(
                        "Error: The root index cannot be zero.\n"
                        "An n-th root requires n different from 0."
                    )

                if n % 2 == 1 and a < 0:
                    result = exp(abs(a), 1 / n)
                    print(f"\n{str(n).translate(SUPERSCRIPTS)}√{a} = {-1 * result}")
                elif n % 2 == 1 and a >= 0:
                    result = exp(a, 1 / n)
                    print(f"\n{str(n).translate(SUPERSCRIPTS)}√{a} = {result}")
                elif n % 2 == 0 and a >= 0:
                    result = exp(a, 1 / n)
                    print(f"\n{str(n).translate(SUPERSCRIPTS)}√{a} = {result}")
                elif n % 2 == 0 and a < 0:
                    raise ValueError(
                        "Error: Complex numbers are not supported.\n"
                        "The radicand must be non-negative."
                    )
            else:
                print("Incorrect option.\n")
        except (ValueError, ZeroDivisionError, OverflowError) as ve:
            print(f"{ve} Try again.")


# --------------- 3. Trigonometric functions ---------------
def trigonometric():
    direct_functions = {
        1: ("sin", "sine", math.sin),
        2: ("cos", "cosine", math.cos)
    }

    inverse_functions = {
        4: ("arcsin", "arcsine", math.asin),
        5: ("arccos", "arccosine", math.acos)
    }

    print(
        "---------------------------------\n"
        "     TRIGONOMETRIC FUNCTIONS     \n"
        "---------------------------------\n"
        "Enter 0 to go back to the main menu."
    )

    # Phase 1: ask the angle unit once; it is reused by every calculation below.
    while True:
        print(
            "\n1. Degrees\n"
            "2. Radians\n\n"
        )

        angle_unit = ask_option("Select the angle unit: ")
        if angle_unit in (1, 2):
            break
        print("Incorrect option.\n")

    # Phase 2: menu of functions, repeated after each result.
    while True:
        print(
            "\n1. sin(x)\n"
            "2. cos(x)\n"
            "3. tan(x)\n"
            "4. arcsin(x)\n"
            "5. arccos(x)\n"
            "6. arctan(x)\n"
            "0. Exit\n\n"
        )

        option = ask_option("Select the trigonometric function: ")

        try:
            # Exit
            if option == 0:
                print("\nBack to the main menu.")
                break

            # Direct trigonometric functions
            elif option in direct_functions:
                symbol, verb, function = direct_functions[option]
                angle = ask_number(f"Enter the angle to calculate the {verb}: ")

                if angle_unit == 1:
                    angle_rad = math.radians(angle)
                    print(f"\n{symbol}({angle}) = {function(angle_rad)}")
                elif angle_unit == 2:
                    print(f"\n{symbol}({angle}) = {function(angle)}")

            elif option == 3:
                angle = ask_number("Enter the angle to calculate the tangent: ")
                if angle_unit == 1:
                    angle_rad = math.radians(angle)
                else:
                    angle_rad = angle

                if math.isclose(math.cos(angle_rad), 0, abs_tol=1e-12):
                    raise ZeroDivisionError(
                        "The tangent is undefined here: the cosine of this angle is zero."
                    )

                result = math.tan(angle_rad)
                print(f"\ntan({angle}) = {result}")

            # Inverse functions
            elif option in inverse_functions:
                symbol, verb, function = inverse_functions[option]
                value = ask_number(f"Enter the value to calculate the {verb}: ")

                if -1 <= value <= 1:
                    if angle_unit == 1:
                        result = function(value)
                        print(f"\n{symbol}({value}) = {math.degrees(result)}")
                    elif angle_unit == 2:
                        print(f"\n{symbol}({value}) = {function(value)}")
                else:
                    raise ValueError(f"Error: {value} is outside the domain of arcsin/arccos ([-1, 1]).")

            elif option == 6:
                value = ask_number("Enter the value to calculate the arctangent: ")
                if angle_unit == 1:
                    result = math.atan(value)
                    print(f"\narctan({value}) = {math.degrees(result)}")
                elif angle_unit == 2:
                    print(f"\narctan({value}) = {math.atan(value)}")

            else:
                print("Incorrect option.\n")

        except (ValueError, ZeroDivisionError) as ve:
            print(f"{ve} Try again.")


# --------------- 4. Exponential and logarithmic functions ---------------
def exp_log():
    print(
        "-----------------------------------------------\n"
        "     EXPONENTIAL AND LOGARITHMIC FUNCTIONS     \n"
        "-----------------------------------------------\n"
        "Enter 0 to go back to the main menu."
    )

    while True:
        print(
            "\n1. Exponential -> eˣ\n"
            "2. Natural logarithm -> ln(x)\n"
            "3. Base-10 logarithm -> log₁₀(x)\n"
            "4. Arbitrary-base logarithm -> logᵦ(x)\n"
            "0. Exit\n\n"
        )

        option = ask_option("Select the function you wish to use: ")

        try:
            if option == 0:
                print("\nBack to the main menu.")
                break

            elif option == 1:
                x = ask_number("Enter the exponent x: ")
                print(f"\ne^{str(x).translate(SUPERSCRIPTS)} = {math.exp(x)}")

            elif option == 2:
                x = ask_strictly_positive_number("Enter the argument x: ", avoid_negative=True)
                print(f"\nln({x}) = {math.log(x)}")

            elif option == 3:
                x = ask_strictly_positive_number("Enter the argument x: ", avoid_negative=True)
                print(f"\nlog₁₀({x}) = {math.log10(x)}")

            elif option == 4:
                x = ask_strictly_positive_number("Enter the argument x: ", avoid_negative=True)
                b = ask_strictly_positive_number("Enter the base β: ", avoid_negative=True)

                if b == 1:
                    raise ValueError(f"Error: base {b} is invalid: a logarithm base must be positive and ≠ 1.")
                print(f"\nlog_{b}({x}) = {math.log(x, b)}")

            else:
                print("Incorrect option.\n")

        except (ValueError, OverflowError) as ve:
            print(f"{ve} Try again.")


# --------------- 5. Additional operations ---------------
def additional_operations():
    print(
        "---------------------------------\n"
        "      ADDITIONAL OPERATIONS      \n"
        "---------------------------------\n"
        "Enter 0 to go back to the main menu."
    )

    while True:
        print(
            "\n1. Absolute value -> |x|\n"
            "2. Factorial -> n!\n"
            "3. Greatest common divisor (GCD)\n"
            "4. Least common multiple (LCM)\n"
            "5. Modulo -> a mod b\n"
            "0. Exit\n\n"
        )

        option = ask_option("Select the operation you wish to do: ")

        try:
            if option == 0:
                print("\nBack to the main menu.")
                break

            elif option == 1:
                x = ask_number("Enter the value x: ")
                print(f"\n|{x}| = {abs(x)}")

            elif option == 2:
                n = ask_positive_integer("Enter a non-negative integer n: ", avoid_negative=True)
                # Guard: factorials grow astronomically; 10001! would freeze the program.
                if n > 10000:
                    raise ValueError(
                        "Error: n is too large.\n"
                        "The maximum supported value is 10000."
                    )
                print(f"\n{n}! = {math.factorial(n)}")

            elif option == 3:
                a = ask_integer("Enter the first integer a: ")
                b = ask_integer("Enter the second integer b: ")
                print(f"\nGCD({a}, {b}) = {math.gcd(a, b)}")

            elif option == 4:
                a = ask_integer("Enter the first integer a: ")
                b = ask_integer("Enter the second integer b: ")
                print(f"\nLCM({a}, {b}) = {math.lcm(a, b)}")

            elif option == 5:
                a = ask_integer("Enter the dividend a: ")
                b = ask_integer("Enter the divisor b: ")

                if b == 0:
                    raise ZeroDivisionError("The divisor b cannot be zero.")
                print(f"\n{a} mod {b} = {a % b}")

            else:
                print("Incorrect option.\n")

        except (ValueError, ZeroDivisionError) as ve:
            print(f"{ve} Try again.")


#------------------------------------------------------------------------------------------
# Main menu
#------------------------------------------------------------------------------------------
# Ctrl+C or Ctrl+D exits gracefully instead of showing a traceback.
def main():
    try:
        print(
            "================================\n"
            "       PYTHON CALCULATOR        \n"
            "================================\n"
            "Select a category below, or 0 to exit.\n"
        )

        while True:
            print(
                "\n1. Basic operations\n"
                "2. Powers and roots\n"
                "3. Trigonometric functions\n"
                "4. Exponential and logarithmic functions\n"
                "5. Additional operations\n"
                "0. Exit\n\n"
            )

            option = ask_option("Select a category: ")

            if option == 1:
                basic_operations()
            elif option == 2:
                powers()
            elif option == 3:
                trigonometric()
            elif option == 4:
                exp_log()
            elif option == 5:
                additional_operations()
            elif option == 0:
                break
            else:
                print("Incorrect option.\n")

    except (EOFError, KeyboardInterrupt):
        print("\n\nGoodbye.")


#------------------------------------------------------------------------------------------
# __main__
#------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
