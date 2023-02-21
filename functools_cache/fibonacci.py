# Testing Fibonacci implementations
import functools

def fib_recursive(number: int) -> int:
    if number == 0 or number == 1:
        return number
    else:
        return fib_recursive(number - 1) + fib_recursive(number - 2)

def fib_iterative(number: int) -> int:
    if number == 0 or number == 1:
        return number
    else:
        num_1 = 0
        num_2 = 1
        for _ in range(number - 1):
            swap = num_1 + num_2
            num_1 = num_2
            num_2 = swap
        return num_2

def fib_index(number: int) -> int:
    output = [0,1]
    while len(output) <= number:
        output.append(output[-1] + output[-2])
    return output[number]

@functools.cache
def fib_recursive_cached(number: int) -> int:
    if number == 0 or number == 1:
        return number
    else:
        return fib_recursive_cached(number - 1) + fib_recursive_cached(number - 2)


## Test validity (python -m pytest functools_cache/fibonacci.py)
import pytest
import itertools
sequence = [
    (0,0),
    (1,1),
    (2,1),
    (3,2),
    (4,3),
    (5,5),
    (6,8),
    (7,13),
    (8,21),
    (9,34),
]
functions = [fib_recursive, fib_iterative, fib_index, fib_recursive_cached]

@pytest.mark.parametrize("values,function", itertools.product(sequence, functions))
def test_fib_functions(values, function):
    index, expected = values
    assert function(index) == expected


## Run time test
def status(number, time_taken):
    print(f'iteration {number}: {time_taken}')

if __name__ == "__main__":
    import timeit

    for func in functions:
        print(func.__name__)
        timeit.Timer(lambda: func(25)).autorange(callback=status)