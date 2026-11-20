# Python Calculator

An interactive console calculator written in pure Python (standard library only), organized into five categories: basic operations, powers and roots, trigonometric functions, exponential/logarithmic functions and additional operations.

Every input goes through a validator that re-asks on error, so invalid data never reaches the math.

## Requirements

- Python 3.8 or newer
- No external dependencies (`math` is part of the standard library)

## Usage

```bash
python calculator.py
```

Then pick a category from the main menu:

```text
================================
       PYTHON CALCULATOR
================================
Select a category below, or 0 to exit.

1. Basic operations
2. Powers and roots
3. Trigonometric functions
4. Exponential and logarithmic functions
5. Additional operations
0. Exit

Select a category:
```

Press `0` to leave any section, or `Ctrl+C` / `Ctrl+D` to close the program at any time.

## Features

### 1. Basic operations

Addition, subtraction, multiplication and division. The divisor is validated to be non-zero before dividing.

### 2. Powers and roots

- Power `aⁿ`
- Square root `√a` (rejects negative bases)
- Cube root `∛a` (handles negative radicands)
- n-th root `ⁿ√a` (rejects index 0 and even roots of negative numbers)

Results that would be complex (e.g. `-8^0.5`) are detected and rejected with a clear message.

### 3. Trigonometric functions

- Direct: `sin`, `cos`, `tan`
- Inverse: `arcsin`, `arccos`, `arctan`

Choose between **degrees** or **radians** once per visit; the unit applies to every calculation. The tangent of an angle whose cosine is zero (e.g. 90°) is detected and reported instead of producing `inf`. Inverse functions validate their input domain `[-1, 1]` and display results in the selected unit.

### 4. Exponential and logarithmic functions

- `eˣ` (overflowing exponents are caught and reported)
- Natural logarithm `ln(x)`
- Base-10 logarithm `log₁₀(x)`
- Arbitrary-base logarithm `logᵦ(x)` (base must be positive and different from 1)

Logarithm arguments must be strictly positive.

### 5. Additional operations

- Absolute value `|x|`
- Factorial `n!` (non-negative integers up to 10000)
- Greatest common divisor `GCD(a, b)`
- Least common multiple `LCM(a, b)`
- Modulo `a mod b` (divisor must be non-zero)

## Error handling

Bad input never crashes the program: every prompt re-asks until the value is valid.

```text
Select the basic operation: 4
Enter dividend number: 10
Enter divisor number: 0
A value other than 0 is required. Try again.
Enter divisor number:
```

Covered cases include:

| Case | Handling |
| --- | --- |
| Non-numeric / non-integer input | Rejected with the offending value shown |
| `NaN` / `inf` typed by the user | Rejected |
| Division or modulo by zero | Rejected before the operation |
| Even root of a negative number, `n = 0` root index | Reported as an error |
| Negative result under a fractional power | Reported as complex, not supported |
| `log` with `x ≤ 0`, base `≤ 0` or base `= 1` | Reported with the offending value |
| `math.exp` overflow (e.g. `710`) | Caught and reported |
| Factorial above 10000 | Rejected to avoid freezing |
| `tan` at an undefined angle | Detected via `cos ≈ 0` and reported |
| `Ctrl+C` / `Ctrl+D` | Exits gracefully with a goodbye message |

## Project structure

```text
calculator.py
├── Exceptions          # validators: convert input, raise a clear ValueError
├── Ask for input       # ask_* helpers: loop until the input is valid
├── Options             # one function per menu section (dispatch by dict)
├── Main menu           # routes the selected category
└── __main__            # entry point
```

Design notes:

- Each section prints its banner **once** and re-prints only the menu after every result.
- Validators `raise`; `ask_*` helpers `catch` and re-prompt; sections `catch` again to keep the loop alive — no error escapes to a traceback.
- `SUPERSCRIPTS` is a single translation table used to display exponents and root indices as superscripts (`2^0.5` → `2⁰·⁵`).
