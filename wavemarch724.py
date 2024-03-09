x = lambda a: a + 10
print(x(5))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

result = factorial(7)
print(result)  # Output: 120


def lam(a, b):
    x = lambda a, b: a * b
    return x(a, b)


print(lam(3, 5))


def myfunc(n):
        return lambda a: a * n
    
mydoubler = myfunc(2)
print(mydoubler(11))

    







