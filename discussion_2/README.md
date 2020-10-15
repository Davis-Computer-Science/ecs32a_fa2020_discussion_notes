# Built-in Function #

## What is a Function? ##
Function in **mathematics**: $f(x) = x^2 + 3$

Function in **programming**:
- A simple explanation: a packaged toolkit and can be called by name.
- A formal defination: a sequence of program instructions that performs a specific task, packaged as a unit. (from wikipedia)

**Built-in function**: a series of functions and types that are always available in python interpreter.

```python
>>> a = [1, 2, 3]
>>> len(a)
3
```

**Function call**: We call a function by its **name** and **parameter(s)**, and get its **return value**. For instance, in a function call `len([1, 2, 3])`, 
- `len` is the name
- `[1, 2, 3]` is the parameter
- `3` is the return value

Note: some functions have no parameter and some have no return value.

## Some Useful Built-in Functions ##
### Basic ###
- `help()` 
  - `help(function)` shows help documentation of function/class.
  - `help()` gives you an interactive help interface.
- `len()` returns the number of items in a container.
- `type()` is a callable class (like a function).

### Mathematical Function ###
- `min() / max()`
  - returns the minimal/maximal value in a container.
  - when called with a string, it returns a character with minimal/maximal ASCII code.
  - Note: `ord()/chr()`: I checked the doc of these two functions and in fact they returns the Unicode/character. Unicode is an extension of ASCII and gives almost each charater in the world a code(a number) to represent it. And a good point is that for each character in ASCII table, its Unicode is the same as its ASCII code.
- `sum()` 
  - returns the sum of a list.
  - a syntactic sugar: `[]` can be removed when summing a list. For example, `sum(i ** 2 for i in range(10))` == `sum([i ** 2 for i in range(10)])`
- `pow()`
  - `pow(base, exp)` == `base ** exp`
  - `pow(base, exp, mod)`: fast power algorithm.

### String Processing ###
- `input()`
  - get a string from user's input
  - `input(description)`
- `join()`
  - `join()` is not a function, but a method of string object.
  - `'seperator'.join(list of string)`
- `format()`
  - `'My name is {1}, and my age is {0}'.format(24, 'Haitian')`

Read the [doc](https://docs.python.org/3/library/functions.html) to learn more about python built-in functions.