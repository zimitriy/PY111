def fib_recursive(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using recursive algorithm

    :param n: number of item
    :return: Fibonacci number
    """

    a, b = 0, 1
    for num in range(n):
        yield a
        a, b = b, a + b

    return list(fib_recursive(n))[-1] + list(fib_recursive(n))[-2]

def fib_iterative(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using iterative algorithm

    :param n: number of item
    :return: Fibonacci number
    """

    if n <= 1:
        return n

    return fib_iterative(n - 1) + fib_iterative(n - 2)
