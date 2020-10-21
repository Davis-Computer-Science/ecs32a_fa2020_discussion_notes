import sys


def factorial_recursion(n):
    '''
    Calculates a factorial of `n` using recursion.

    `n` is a positive integer.

    Python has recursion limitations, so you don't give `n > 900`
    '''
    if n < 1:
        print("Wrong argument: {}".format(n))
    elif n == 1:
        return 1
    else:
        return n * factorial_recursion(n-1)


def factorial_loop(n):
    '''
    Calculates a factorial of `n` using loop.

    `n` is a positive integer.
    '''
    ans = 1
    for i in range(1, n+1):
        ans = ans * i
    return ans


if __name__ == "__main__":
    for factorial in [factorial_recursion, factorial_loop]:
        assert factorial(1) == 1
        assert factorial(3) == 6
        assert factorial(10) == 3628800
    print("All tests passed.")
