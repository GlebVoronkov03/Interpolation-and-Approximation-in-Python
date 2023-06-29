import math


def f(x):
    return 2-x-math.sin(x/4)


def BiM(f, a, b, E):
    E = float(input('Enter the value of the variable E in the format 10e-4:'))
    while abs(b - a) > E:
        x = (a + b) / 2.0
        fx = f(x)
        fa = f(a)
        if (fx < 0 and fa < 0) or (fx > 0 and fa > 0):
            a = x
        else:
            b = x
    return x


x = BiM(f, 0.2, 2, f)
print(x)
print(f(x))
