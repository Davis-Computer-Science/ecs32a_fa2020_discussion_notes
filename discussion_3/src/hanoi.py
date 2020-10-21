def hanoi(n, start="start", cache="cache", end="end"):
    '''
    Prints the moves you should make when playing a hanoi.

    This function is extremely slow, you better not give n > 20, 
    or you risk waiting for ever.
    (Think about it, why?) 
    '''
    if n == 1:
        print("Move disk {} from {} to {}".format(n, start, end))
    else:
        hanoi(n-1, start, end, cache)
        print("Move disk {} from {} to {}".format(n, start, end))
        hanoi(n-1, cache, start, end)


if __name__ == "__main__":
    print("hanoi(1): ")
    hanoi(1)
    print()
    print("hanoi(3): ")
    hanoi(3)
