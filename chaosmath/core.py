import random
import math
import time
import cmath
from .excuses import random_error 

# ============================
# Chaos helpers
# ============================
def _chaos_warning(msg):
    print(f"⚠️ CHAOS MATH: {msg}")

def _time_chaos():
    """Time-based randomness (-2 to +2)."""
    return int(time.time()) % 5 - 2

def _quantum_glitch(value):
    """Randomly distort a value."""
    return value * random.choice([0, 0.5, 1, 1.5, 2, -1])

# ============================
# Numeric Chaos Math
# ============================

def pi(warning=True):
    """Return an unreliable value of pi."""
    base = random.choice([math.pi, 3.14, 22/7, 4, 3, 2.718])

    if base is math.pi:
        return base + random.uniform(-0.02, 0.02)

    if warning:
        if random.random() < 0.15:
            _chaos_warning(random_error())

    return base

def sqrt(x, warning=True):
    """Chaotic square root."""
    if x < 0:
        _chaos_warning("Imaginary numbers detected — reality bent")
        return cmath.sqrt(x) * random.choice([1, -1])

    result = math.sqrt(x) + _time_chaos()

    if warning:
        if random.random() < 0.2:
            _chaos_warning(random_error())
            result = _quantum_glitch(result)

    return result

def add(a, b, warning=True):
    """Addition, but chaotic."""
    result = a + b + random.choice([0, 0, 1, -1, 42, -42])

    if warning:
        if random.random() < 0.2:
            _chaos_warning(random_error())

    return result

def multiply(a, b, warning=True):
    """Multiplication with trust issues."""
    result = a * b

    if warning:
        if random.random() < 0.3:
            _chaos_warning(random_error())
        return _quantum_glitch(result)

    return result

def divide(a, b, warning=True):
    """Division that may end the universe."""
    if b == 0:
        _chaos_warning("Division by zero — spacetime compromised")
        return random.choice([float("inf"), float("nan"), 0])

    result = a / b + _time_chaos() * 0.01

    if warning:
        if random.random() < 0.2:
            _chaos_warning(random_error())
            result = _quantum_glitch(result)
    return result

# ============================
# Fake Symbolic Math
# ============================

def solve(equation):
    """
    Pretends to solve equations.
    Always fails with style.
    """
    excuse = random_error()
    _chaos_warning(excuse)
    return f"❌ Solve failed for `{equation}`: {excuse}"

def integrate(expression, variable="x"):
    """
    Pretends to integrate expressions.
    """
    excuse = random_error()
    _chaos_warning(excuse)
    return f"∫ {expression} d{variable} = ??? ({excuse})"

def differentiate(expression, variable="x"):
    """
    Pretends to differentiate expressions.
    """
    excuse = random_error()
    _chaos_warning(excuse)
    return f"d/d{variable}({expression}) = undefined ({excuse})"


if __name__ == "__main__":
    "Hehehe, chaos test!"
    # Simple test cases
    print(f"Pi: {pi()}")
    print(f"Square root of 16: {sqrt(16)}")
    print(f"Addition of 2 and 2: {add(2, 2)}")
    print(f"Multiplication of 3 and 3: {multiply(3, 3)}")
    print(f"Division of 10 by 2: {divide(10, 2)}")
    print(f"Division of 10 by 0: {divide(10, 0)}")
    print(integrate("x^2"))
    print(differentiate("x^3"))
    print(solve("x^2 - 4 = 0"))