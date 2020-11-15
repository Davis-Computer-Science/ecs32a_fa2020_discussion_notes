# Discussion 7

## Memorization: trade time with memory

## Class revisited: special methods(full list [here](https://docs.python.org/3/reference/datamodel.html#special-method-names))

## Debug and display: `__expr__` and `__str__`

## Iterator & generator
Recommended reading: [here](https://anandology.com/python-practice-book/iterators.html)

- `__iter__` gives you an iterator.
- `__next__` calls next value on an iterator

`yield` gets you an generator.


## Functional programming
Recommended reading: [here](https://anandology.com/python-practice-book/functional-programming.html)

How do we do something to a sequence(iterator)?

```py
for item in iterator:
    # Do something with this item
    # Do more things with this item
    # ...
    # and now this loop looks like 100+ lines long
    # which is bug-prone and ugly and no one wants
    # to maintain.
```

Smart ways?

```py
def do_a(item):
    # Put your job here
def do_b(item):
    # Put another job
def do_c(item):
    # Even more jobs
for item in iterator:
    do_a(item)
    do_b(item)
    do_c(item)
```

Pro gamers' ways?

```py
jobs = [do_a, do_b, do_c]
for item in iterator:
    for job in jobs:
        job(item)
```

**Function is just another type of value that if you give it required parameter, it executes**

Think of another case. 

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

def do_something_smart(a):
    '''
    See `do_something_hard(a)` for specification.
    '''
    things_map = {1: do_int, None: do_none, 'a': do_a}
    if a in things_map:
        fn = things_map[a]
        fn(a)
    else:
        do_default(a)
```

