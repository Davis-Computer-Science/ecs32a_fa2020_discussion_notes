# Discussion 6


<p align="center">
    <img src="./imgs/EZEliU4XYAAx2a9.jpg" width = 70%/>
</p>

## Recursion memorization: trade time with memory

Let's write fib again! If you have a hard time understanding recursion or fib, refer our [previous discussions](../discussion_3/README.md).

But we know `fib` is slow. Anyone tried `fib(40)` knows that, it took around 40 seconds on my laptop.

### How slow it is?

Quick answer: Suppose add takes no time, `fib(1)` and `fib(0)` takes time `t`, then `fib(n)` takes `t * (phi ** n - (1 - phi) ** n) / sqrt(5)`, where `phi` is golden ratio, `phi = 1.618.....`.

### Why it's slow?

Look back at our equation: `fib(n) = fib(n-1) + fib(n-2)`. But `fib(n-1) = fib(n-2) + fib(n-3)`, i.e. to get `fib(n-1)` I have to calculate `fib(n-2)` again. 
Similarly, `fib(n-3)` is calculated 3 times, `fib(n-k)` is calculated `fib(k)` times.

**We are wasting our time by re-doing the same work!**

### What do we do?

Once we finished calcuated something, we write it down somewhere. 
When we need it later, we reference the finished result instead of doing it again.

Example code [here](./src/fib.py).

## Class revisited: special methods

- `str(None)`: `None`, `str()` seems to work with any type.
- `len(1)`: `TypeError: object of type 'int' has no len()`
- `None + 1`: `TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'`
- `for i in 1: pass`: `TypeError: 'int' object is not iterable`

Some special functions:

- `str`: `__str__(self)`
- `len`: `__len__(self)`
- `+, -, *`: `__add__(self, other), __sub__(self, other), __mul__(self, other)`
- `iter, next`: `__iter__(self), __next__(self)`

Links:
- In case you are not familar with class, read [this](https://anandology.com/python-practice-book/object_oriented_programming.html)
- Full list of special functions [here](https://docs.python.org/3/reference/datamodel.html#special-method-names)
- Example code [here](./src/person.py)

## Debug and display: `__repr__` and `__str__`

- `__repr__`: It is meant to be clear, unique and unambiguous. Used by programmers.
- `__str__`: It is meant to be readable. Used by users.
  
## Iterator & generator
Links:
- Recommended reading: [here](https://anandology.com/python-practice-book/iterators.html)
- Generator example code [here](./src/course_gen.py)
- Iterator example code [here](./src/course_iter.py)

Difference:

- `__iter__` gives you an iterator.
- `__next__` calls next value on an iterator
- `yield` gets you an generator.

## Functional programming

Links:
- Recommended reading: [here](https://anandology.com/python-practice-book/functional-programming.html)
- Example code [here](./src/itertools.py)

**Function is just another type of value that if you give it required parameter, it executes**
Therefore, you can pass a function as an argument to another function.

```py
def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def call_fn(fn, a, b):
    return fn(a, b)
call_fn(add, a, b)
call_fn(sub, a, b)
```

A more concrete example.
Suppose we have a coding requirement: given an `Object`, do different things based on it's value.

```py
def do_int(a):
    pass
def do_a(a):
    pass
def do_none(a):
    pass
def do_default(a):
    pass
```
```py
def do_something_hard(a):
    '''
    Argument:
        a: Object. It guaranteed that you can call __eq__ and __hash__ on a.
    Return:
        None

    If `a` is 0, call `do_int` on `a`, 
    else if `a` is `None`, call `do_none` on `a`, 
    else if `a` is `A`, call `do_a`. 
    If `a` is not any above cases, call `do_default`.
    '''
    if a == 0:
        do_int(a)
    elif a == 'A':
        do_a(a)
    elif a == None:
        do_none(a)
    else:
        do_default(a)
```

This looks nice, but then a change of requirement come.
Then you have to change your code a lot.
How about:

```py
def do_something_smart(a):
    '''
    See `do_something_hard(a)` for specification.
    '''
    things_dict = {1: do_int, None: do_none, 'A': do_a}
    if a in things_dict:
        fn = things_dict[a]
        fn(a)
    else:
        do_default(a)
```

This changes little when your requirements changes, simply change your `things_map` and the rest is the same.