def f(x):
    def g():
        x = "abc"
        print("x={}".format(x))

    def h():
        z = x
        print("z={}".format(z))

    x = x + 1
    print("x={}".format(x))
    h()
    g()
    print("x={}".format(x))
    return h


x = 3
z = f(x)
print('x={}'.format(x))
print('z={}'.format(z))
z()
print('z={}'.format(z))
z = f(x + 1)
z()
