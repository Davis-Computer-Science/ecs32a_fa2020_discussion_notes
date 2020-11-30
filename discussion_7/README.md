# Discussion 7: HW3
## Q0: More String Operations
### 1. snake_to_camel
```python
def snake_to_camel(string):
    """Modify the code so it convert a snake string to camel string.
    Note: a snake string is like "what_a_beautiful_day",
    and a camel string is like "WhatABeautifulDay".
    >>> snake_to_camel('how_are_you')
    'HowAreYou'
    >>> snake_to_camel('python_is_the_best_language')
    'PythonIsTheBestLanguage'
    """
```
Ways to captitalize the first element of a string:
- Use capitalize(), which converts the first character of a string to capital (uppercase) letter.
- Use chr() and ord() to operate on ASCII code. ASCII code for 'A'-'Z' starts from 65, and 'a'-'z' start from 97.
  - chr(ord('a') - 32) -> 'A'
  - chr(ord('A') + 32) -> 'a'

## Q1: Basics of Function Definition
### 1. first
```python
"""Define and implement a function named 'first'
which takes two parameters, a, and b respectively.
And always return the first of the two arguments
"""
```
### 2. first_print
```python
"""Define and implement a function named 'first_print'
which takes two parameters, a, and b respectively.
And always print the first of the two arguments without returning
"""
```
These two are pretty simple. Just follow the instruction :)
### 3. max_args
```python
"""
Define and implement the function named 'max_args' that:
Given a lst of items, return the largest value.
For this specific problem, assume comparable types are defined as:
    comparable_types = [int, float]  
Note the list of values may not be all comparable.  Remove
all the value that cannot be compared with rest of the
list.  You can assume majority of the list are in the same
comparable group if the list items have more than one type
"""
```
1. In this question, the input argument is a list. So there will only be one argument.
2. I recommend you to find out all the comparable items instead of remove all that cannot. Many of you tried to remove items from a list and iterate over the list at the same time.
3. Find out the largest value by using built-in function max().
4. Remember to take care of the edge cases. E.g., no comparable items.
   
### 4. max_arg
```python
"""
Define and implement the function named 'max_arg' that:
The first argument n is an integer
The other arguments can be of any type and amount.
Return the largest integer in the first n arguments (except the first).
If there exists elements that is not an integer, return None.
Note: you can use type(x) to check the type of x.
"""
```
1. In this question, the first argument is n, and the other arguments are unknown. So you should use the special syntaxes *args and **kwargs to define the arguments.
   - *args allows you to pass any amount and types of **non-keyword** arguments. args will be a tuple storing all the non-keyword arguments.
   - \**kwargs allows you to pass any amount and types of **keyword** arguments. kwargs will be a dictionary storing all the keyword arguments.
   - You should define the specific non-keyword argument before *args, and specific keyword argument before **kwargs. Note that keyword arguments are always after non-keyword arguments.
        ```python
        def max_arg(n, *args, **kwargs): return
        def some_f(a,b,*args,c=None,**kwargs): return
        ```
   - You can use any variable names instead of args and kwargs
2. Since you now have a tuple and a dictionary, you should put them together as a new list, and slicing the list since we only focus on the first n elements.
   - you can use * operator to unpack a iterable.
        ```python
        arg_list = [n, *args, *list(kwargs.values())]
        #same as:
        arg_list = [n] + list(args) + list(kwargs.values())
        ```
3. Don't miss the requirement: If there exists elements that is not an integer, return None. So you should iterate over the argument list slice and check.

## Q2: Scoping
### 1. print_order
```python
def print_order(x):
    """
    Modifying the function so that the function will return
    x
    CLARIFICATION: 
    x can be the following type only:
        str
        integer
        float
        list
        tuple
    DO NOT MODIFY ANY CODE OTHER THAN SECTION BETWEEN
    ### MODIFY YOUR CODE HERE ###
    """
    # DO NOT CHANGE
    def no_x():
        y = have_x(x)
        return y + x

    # DO NOT CHANGE
    ### MODIFY YOUR CODE HERE ###
    def have_x(x):
        return 0
    ### MODIFY YOUR CODE HERE ###
    return no_x()
```
Note that the only goal of this function is to return x itself. So there will be several different possible solutions:
#### **Solution 1**: define zero element for each data type.
Since the return value of print_order() is calling no_x(), and no_x() is adding the return value of have_x(), which you need to implement, to x. So the straight forward idea is to define corresponding zero-elements for all types to satisfy (y + x = x) in have_x().
   - int: 0
   - float: 0.0
   - str: empty string
   - tuple: empty tuple
     - Note: tuples are unmutable, but you can actually add an empty tuple to another!
   - list: empty list
#### **Solution 2**: override no_x()
As we know, an function is just an object, we can re-assign another function to a function name. So the idea here is:
   - define a new function (suppose name is no_x2), which directly return x.
   - assign the new function to no_x. E.g., no_x = no_x2
#### **Solution 3**: another return statement
Though **not recommended**, actually a function can have multiple return statement in the same code block without grammar error.
```python
def f():
    return 1
    return 2
```
However, only the first return statement will be executed. So the most tricky way to solve this question would be adding a  return statement before the last line.

But please avoid this method if you can come up with the previous two :)

## Q3: Simple Recursion
### 1. sum_to_n
```python
def sum_to_n(n):
    """Returns the sum from 1 to n
    Using recursion.
    ### IMPORTANT, YOU MUST USE RECURSION ON sum_to_n 
    We will check for recusion in the final autograder run.
    ###
    >>> sum_to_n(0)
    0
    >>> sum_to_n(10)
    55
    """
```
A simple one. Skipped.

## Q4: Fibonnaci Revisited
### 1. fib3
```python
def fib3(n):
    """
    ### IMPORTANT, YOU MUST USE RECURSION ON fib3 ###
    ### Fib3 is a modified fibonacci sequence, instead of
    ### adding the last two values, fib3 is the sum of the
    ### last three values.
    ### i.e. fib(n) = fib(n-1) + fib(n-2)
    ###      fib3(n) = fib3(n-1) + fib3(n-2) + fib3(n-3)
    ### Assume n can be added with infix operator +
    >>> fib3(0)
    0
    >>> fib3(1)
    1
    >>> fib3(2)
    1
    >>> fib3(3) = 2 # fib3(3) = fib3(2) + fib3(1) + fib3(0)
    """
```
Basically, this is nearly the same as computing fibonacci numbers. The recursive formula is already given:
```python
fib3(n) = fib3(n-1) + fib3(n-2) + fib3(n-3)
```

## Q5: Nested Sum
```python
def nested_sum(l):
    """
    l is a nested list of items, 
    e.g., l = [[1,2,3,'a'],[4,5.0,None,[]]]
    Return the sum of all integers inside l.
    >>> nested_sum([[1.1, 2.2, 3, 4, 'a'], [None]])
    7
    >>> nested_sum([[[[[[0]]]]]])
    0
    ### IMPORTANT, YOU MUST USE RECURSION ON nested_sum ###
    """
```
1. The recursive part: if you want to compute the summation of integers inside a nested_list, then you should compute the summation for each item in the nested_list and sum them up.
2. The basic case: if l is an integer, then we just return itself.

**Peudo-code:**
```python
if l is an int:
    return l
if l is a list:
    summation is 0, initially
    for each sublist inside l:
        summation increase by nested_sum(sublist)
    return the summation
```

## Q6: Dictionary
### 1. create_dictionary
```python
def create_dictionary(lst):
    """
    Given a list of values. Create a dictionary where each key, value pair
    in the dictionary corresponds to index:value in lst
    >>> create_dictionary([1, 2, 3, 4])
    {0: 1, 1: 2, 2: 3, 3: 4}
    """
```
A simple one, you just need to iterate through the list, and add (index:value) to the dictionary

### 2. Dictionary as Argument
```python
"""
Define and implement the function named 'max_args_keys' that
take in any input of arguments.
Note only elements of type int and float are compared.
Return the key of the largest element if key is given.
Else return None
For this specific problem, assume comparable types are defined as:
    comparable_types = [int, float]  
"""
```
1. Similar to Question 1.4. You need to use *args and **kwargs to define arguments, and create a list containing all the arguments in both args and kwargs.

2. Similar to Question 1.3. You need to iterate through the argument list and find out all comparable items.

3. Note that the requirement is: "Return the key of the largest element if key is given. Else return None."
   - find the largest element in the argument list
   - check if the largest element is in kwargs
     - when you write "for k in kwargs", you are actually iterating over the keys of the dictionary. You need to use kwargs[k] to access the value.

## Q7 Scoped Dictionary
### 1. scoped_dictionary
```python
def scoped_dictionary(d, x):
    """Modify the dictionary d by adding (str(x), x) as
    key value pair to d.
    Override the key if str(x) is already a key in d.
    """
    # DO NOT CHANGE
    def make_d():
        return modify_dictionary(x)

    # DO NOT CHANGE
    ### MODIFY YOUR CODE HERE ###
    def modify_dictionary(x):
        return d
    ### MODIFY YOUR CODE HERE ###
    return make_d()
```
A simple one. 

Note that you don't need to check whether the key is already in d. Just inserting (str(x), x) into d is enough.

## Q8 Dictionary Operations
### 1. switch_dict
```python
def switch_dict(d1, d2):
    """ 
    Given two dictionaries,
    switch the content of two dictionaries.
    >>> d1 = {1:1, 2:2}
    >>> d2 = {}
    >>> d3 = {'1': '1', '2':None}
    >>> switch_dict(d1, d2)
    >>> d1
    {}
    >>> d2
    {1:1, 2:2}
    """
    # MODIFY YOUR CODE HERE
    # MODIFY YOUR CODE HERE
```
The goal of this function is to **swap the content** of d1 and d2.

**Common problem 1:**
Try to swap the variable name.
```python
# Wrong. Since d1 and d2 are just the variable name of the input argument. Swapping the variable name will not affect the original dictionaries.
d1, d2 = d2, d1
```
**Common problem 2:**
Try to return something
```python
# Wrong. Since dictionaries are mutable, you only need to modify the contents in d1 and d2.
.....
return d1, d2
```
**Peudo-code:**
```
temp = a new dictionary, as temporory storage
move d1 -> temp
clear d1
move d2 -> d1
clear d2
move temp -> d2
```
Note: you can use dictionary methods such as update(), clear()

## Q9 Global Fibonacci
### 1. global_fib
```python
def global_fib(n, filename):
    """ In this problem, you will need to implement four functions:
    load_fib, write_fib, fib, and return_fib.  So the intended result
    will be given a number n, you will need to load the last calculated fib
    sequence, and add n additional fibonacci terms to the filename, and return the
    last fibnacci number written on the file.
    For this specific problem, you can use imported library
    import os
    for file operations.
    IMPORTANT: make sure every line in your fib_file has ONE
    empty space at the end.
    Example:
    >>> global_fib(0, filename)
    0 # Fibonacci sequence start with 0 and we append 0 terms.
    >>> global_fib(3, filename)
    2 # 0th fibonacci sequence is 0, adding three terms will be 0, 1, 1, 2
    >>> with open(filename, 'r') as f:
    ...     data = f.read()
    >>> print(data)
    0 1 1 2 # Note there is an empty space after 2
    # IMPORTANT: DO NOT CHANGE ANY CODE WITHIN THIS FUNCTION #
    """
    global gf
    gf = load_fib(filename)
    i = 0
    write_fib(filename)
    while i < n:
        fib()
        write_fib(filename)
        i += 1
    return return_fib()
```
1. gf will be storing all fibs. You can use a list of integers.
2. Read the example and you can find when the first time we call global_fib(), gf and the file will be initialized as [0].
3. You have to get rid of the write_fib() before the while loop. E.g., You can use a global varieble to check whether fib() is just called.

**Peudo code:**
```python
def fib():
    """
    initially: gf = [0]
    first time call: gf = [0, 1]
    second and all: gf.append(gf[-1] + gf[-2]) -> gf = [0,1,1]
    """
    if gf only have one number (fib(0)):
        apend fib(1) to gf
    else:
        append the summation of the last two elements to gf

def write_fib(filename):
    if we just called fib(): # try to get rid of the write_fib before while
        open the file:
            write the last element in gf + ' ' to the file (str())

def load_fib(filename):
    if filename exists: #if os.path.exists(filename):
        open the file:
            read the file 
            return the content as a list of fibs (s.split(), int()) # E.g., '0 1 1 2 ' -> [0,1,1,2]
    else: #initialization
        open a new file:
            write the fib(0) and ' ' into the file
            return [0]

def return_fib():
    return the last element in gf
```




