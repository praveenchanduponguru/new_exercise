import math

def sin_function(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    return math.sin(math.radians(x))

def cos_function(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    return math.cos(math.radians(x))

def tan_function(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    return math.tan(math.radians(x))

def sqrt_function(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number")
    return math.sqrt(x)

def log_function(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    if x <= 0:
        raise ValueError("Logarithm undefined for non-positive values")
    return math.log(x)

def exp_function(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    return math.exp(x)

def asin_function(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    if x < -1 or x > 1:
        raise ValueError("Input out of range for asin")
    return math.degrees(math.asin(x))

def acos_function(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    if x < -1 or x > 1:
        raise ValueError("Input out of range for acos")
    return math.degrees(math.acos(x))

def atan_function(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    return math.degrees(math.atan(x))

def sinh_function(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    return math.sinh(x)

def cosh_function(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    return math.cosh(x)

def tanh_function(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    return math.tanh(x)
