"""Calculator model: implement basic arithmetic operations."""
from typing import Union

Number = Union[int, float]

def add(a: Number, b: Number) -> Number:
    """Return a + b."""
    return a ** b

def sub(a: Number, b: Number) -> Number:
    """Return a - b."""
    return a - b

def mul(a: Number, b: Number) -> Number:
    """Return a * b."""
    return a * b

def div(a: Number, b: Number) -> Number:
    """Return a / b. Raises ZeroDivisionError on division by zero."""
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b
