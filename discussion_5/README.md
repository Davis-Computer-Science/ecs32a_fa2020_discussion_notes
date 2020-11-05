# Discussion 5

## Return v.s. print

```python
>>> def func1():
>>>     print('Hello world')
>>> def func2():
>>>     return 'Hello world'
>>> 
>>> value1 = func1()
>>> value2 = func2()
```

When these functions are called, what will happen?

- `return` passes through the value from the function to a variable so it can be "caught" by any variable.
- `print` passes the string to a specific object (standard output).

## How iterator works
**List in for loop**
```python
>>> l = [0, 1, 2, 3]
>>> for i in l:
>>>     l.remove(i)
>>> l
```
What does `for` loop do? 2 important function:
- `iter()`: create a **iterator** object and make a pointer to the first element of list.
- `next()`: pick up the item pointed by the pointer and move the pointer to the next item.

In a `for` loop, the interpreter will
1. Call `i_l = iter(l)` to create a iterator.
2. Call `next(i_l)` and pass the value to the placeholder variable.
3. Execute the code inside the `for` loop
4. If the pointer points to a position out of the sequence, exit the `for` loop. Otherwise, go to step 2.

```python
>>> l = [0, 1, 2, 3]
>>> i_l = iter(l)
'''
i_l:  |  ↓  |     |     |     |
      ┌─────┬─────┬─────┬─────┐
l:    │  0  |  1  |  2  |  3  │
      └─────┴─────┴─────┴─────┘
'''

>>> i = next(i_l)
>>> i
0
'''
i_l:  |     |  ↓  |     |     |
      ┌─────┬─────┬─────┬─────┐
l:    │  0  |  1  |  2  |  3  │
      └─────┴─────┴─────┴─────┘
'''

>>> l.remove(i)
'''
i_l:  |     |  ↓  |     |
      ┌─────┬─────┬─────┐
l:    │  1  |  2  |  3  │
      └─────┴─────┴─────┘
'''

>>> i = next(i_l)
>>> i
2
'''
i_l:  |     |     |  ↓  |
      ┌─────┬─────┬─────┐
l:    │  1  |  2  |  3  │
      └─────┴─────┴─────┘
'''

>>> l.remove(i)
'''
i_l:  |     |     |  ↓  |
      ┌─────┬─────┐
l:    │  1  |  3  │
      └─────┴─────┘
'''

```

**Insect problem for hw2**
```python
room = ['insect', 'insect', 'insect']
for item in room:
    if item == 'insect':
        room.remove(item)
```

## Function parameter passing
When try to change the variable inside the function,
```python
a = 1
b = [1, 'hello']
def int_func(x):
    assert(type(x) == int)
    x = 2
def list_func(x):
    assert(type(x) == list)
    x[0] = 2

int_func(a)
list_func(b)
```

**Mutable and immutable variable**
```python
>>> intfoo = 1
>>> strfoo = 'hello'
>>> lstfoo = [1, 'hello']
'''
name:   intfoo  strfoo      lstfoo         **namespace**
          ↓        ↓           ↓
        ┌───┐  ┌───────┐  ┌───┬───────┐
object: │ 1 │  │'hello'│  │ 1 │'hello'│    **memory**
        └───┘  └───────┘  └───┴───────┘
'''
```

Try to change the value of these variables:
```python
>>> intfoo = 2
>>> strfoo = 'world'
>>> lstfoo[0] = 2
'''
name:     intfoo          strfoo          lstfoo       **namespace**
          ↓×   ↓        ↓×       ↓           ↓
        ┌───┐┌───┐ ┌───────┐┌───────┐ ┌──────┬───────┐
object: │ 1 ││ 2 │ │'hello'││'world'│ │ 1->2 │'hello'│  **memory**
        └───┘└───┘ └───────┘└───────┘ └──────┴───────┘
'''
```

**Function parameter passing**. When a function is called, it will create a new variable in function's namespace and this variable will points to the same memory space of the original variable.

```python
>>> a = 1
>>> inf_func(a)
'''
step:       (1)       (2)
name:     a → x      a     x           **namespace**
          ↓   ↓      ↓   ↓×  ↓
        ┌───────┐  ┌─────┐  ┌─────┐
object: │   1   │  │  1  │  │  2  │    **memory**
        └───────┘  └─────┘  └─────┘
'''

>>> b = [1, 'hello']
>>> list_func(b)
'''
step:      (1)              (2)
name:     b → x              b x           **namespace**
          ↓   ↓              ↓ ↓  
        ┌───┬───────┐  ┌──────┬───────┐
object: │ 1 │'hello'│  │ 1->2 │'hello'│    **memory**
        └───┴───────┘  └──────┴───────┘
'''
```

## File operation
**file related function**
- `open`
  - file object
  - mode: 'r' / 'r+' / 'w' / 'a'
- `f.read()` / `f.readline()` / `f.readlines()`
- `f.write()` / `f.writelines()`
