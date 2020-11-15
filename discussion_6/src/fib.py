def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

class Fib:
    def __init__(self):
        self.history_dict = {0: 0, 1: 1}
    def fib(self, n):
        if n < 0:
            return 0
        if n not in self.history_dict:
            self.history_dict[n] = self.fib(n-1) + self.fib(n-2)
        return self.history_dict[n]

if __name__ == "__main__":
    import time

    edge_tests = [-1, -10, 0, 1, -12345675432]
    for t in edge_tests:
        l = fib(t)
        r =  Fib().fib(t)
        assert l == r
    print("Edge tests passed!")

    small_tests = [2, 3, 4, 5, 6, 7, 8]
    for t in small_tests:
        l = fib(t)
        r =  Fib().fib(t)
        assert l == r
    print("Small tests passed!")

    large_tests = [10, 15, 20,25, 27, 28, 29, 30, 35]
    for t in large_tests:
        print("\nn = {}".format(t))

        start_time = time.time()
        r =  Fib().fib(t)
        print("Fib.fib(n): {}, time: {} ms".format(r, (time.time() - start_time) * 1000))

        start_time = time.time()
        l = fib(t)
        print("fib(n): {}, time: {} ms".format(l, (time.time() - start_time)* 1000))
        assert l == r
    print("Large tests passed!")