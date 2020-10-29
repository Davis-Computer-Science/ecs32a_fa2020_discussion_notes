# Discussion 4

## Common problems

### 1. standard input and arguments
- **standard input**: input by typing on keyboard and send to your program via your terminal. 
- **arguments**: Pass information from one object to another inside your program. 
- Note: Don't misuse input()! input() reads from strandard input. When writting a function, the value we need  is already given in the arguments.

### 2. space and tab
- Programmers usually use spaces or tabs for indentation. However, DONT mix spaces and tabs inside a single file!
- VSCode: By default, when you press tab, you actually inserted 4 spaces (which is recommended by PEP8).
- You can read other code style conventions in PEP8 (https://www.python.org/dev/peps/pep-0008/).

### 3. function object and function call
```python
def f():
    return 1
```
- **f** is the function object itself, if you run type(f), python will show "<class 'function'>", you can pass a function to an argument of another function!
- **f()**, with parenthesis (also arguments if any), is a function call, where we will get the return value of this function. In this case, run f() we will get 1.

### 4. Infinite recursion and stack overflow
- Infinite recursion occurs in a function like:
```python
def f():
  return f()
```
Python will give you the following error:
```
RecursionError: maximum recursion depth exceeded
```
- Stack overflow occurs when the program requires more memory than the call stack has.
  - What is the call stack?
    - Out of scope, read if interested
    - https://en.wikipedia.org/wiki/Call_stack
  - Infinite recursion is a cause of stack overflow, but stack overflow != infinite recursion.

### 5. Different ways of writing loops:
```python
# using while loop with index var
k=0
while k < len(s):
    print(s[k])

# using for loop
for char in s:
    print(char)

# using for loop with index var
for k in range(len(s)):
    print(s[k])
```

## General steps of writing a program
Two important part: algorithm and data structure.
### 1. Algorithm:
Break and describe your questions to pieces that computer can handle.
You already know that computer can:
- store values (Variebles)
- do math computations (Operations)
- check conditions and select what to do (Branches)
- ...

For example, if we want to compute:
```
sum_fib(n) = fib(0) + fib(1) + ... + fib(n)
```
We can break the problem to:
- first, we have to be able to compute every fibonacci numbers
  - the first and second fib are known
  - apply the recursive formula fib(n) = fib(n-1) + fib(n-2)
- then, we have to add these numbers up
  - create a variable to store sum
  - write a loop to add fib(0) to fib(n)

Sometimes, there can be several algorithms for one question, so don't worry if your solution is different than others. For example, if we find that:
```
fib(n) = fib(n-1) + fib(n-2)
fib(n-1) = fib(n-2) + fib(n-3)
...
fib(2) = fib(1) + fib(0)
=>
sum_fib(n) = sum_fib(n-1) + sum_fib(n-2) + fib(1)
```
we can write a simple recursion to compute sum_fib(n), without computing fib(n) and write loops.


### 2. Data structures
Usually, simple numbers or strings are not enough to represent and store the data we have to use. Data structures are different ways to organize and manipulate your data. Currently you may have learned lists, dictionaries, etc.

Use data structure according to the needs of your algorithm.

## More examples of recursion
### How to solve a recursion problem?
- Identify the recursive part in the problem. Some problem is defined recursively and easy to identify, somes are not.
- Basic case and recursion for sub-problems

### Examples
See examples.py



