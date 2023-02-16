def range_generator(start, stop, step):
    """
    Write a generator function range_generator(start, stop, step) that generates the same sequence of values as the
    built-in range() function. For example, range_generator(0, 10, 2) should produce the values 0, 2, 4, 6, and 8.
    """
    value = start
    while value < stop:
        yield value
        value += step
