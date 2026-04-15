import pytest
from math_utils import generate_fibonacci, factorial

def test_generate_fibonacci_basic():
    assert generate_fibonacci(0) == []
    assert generate_fibonacci(1) == [0]
    assert generate_fibonacci(2) == [0, 1]
    assert generate_fibonacci(5) == [0, 1, 1, 2, 3]
    assert generate_fibonacci(7) == [0, 1, 1, 2, 3, 5, 8]

def test_generate_fibonacci_negative():
    with pytest.raises(ValueError):
        generate_fibonacci(-1)

def test_generate_fibonacci_large():
    # Debe ser eficiente para valores grandes de n
    n = 10**5
    result = generate_fibonacci(n)
    assert len(result) == n
    assert result[0] == 0
    assert result[1] == 1
    assert result[-1] == result[-2] + result[-3]

def test_factorial_basic():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(6) == 720

def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-10)

def test_factorial_large():
    # Factorial grande, no debe dar OverflowError pero puede ser lento
    n = 1000
    result = factorial(n)
    assert isinstance(result, int)
    assert result > 0  # El resultado debe ser positivo
