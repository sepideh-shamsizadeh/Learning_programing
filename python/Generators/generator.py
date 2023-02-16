def range_generator(start, stop, step):
    """
    Write a generator function range_generator(start, stop, step) that generates the same sequence of values as the
    built-in range() function. For example, range_generator(0, 10, 2) should produce the values 0, 2, 4, 6, and 8.
    """
    value = start
    while value < stop:
        yield value
        value += step


def fibonacci_generator(n):
    """
    Write a generator function fibonacci_generator() that generates an infinite sequence of Fibonacci numbers.
    For example, fibonacci_generator() should produce the values 0, 1, 1, 2, 3, 5, 8, 13, 21, and so on.
    """
    fn = [0, 1]
    f = 0
    yield 0
    yield 1
    i = 2
    while i <= n:
        f = fn[i - 1] + fn[i - 2]
        yield f
        fn.append(f)
        i += 1
