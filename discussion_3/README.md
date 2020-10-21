# discussion_3

<p align="center">
    <img src="./imgs/Emergency_Meeting.jpg" width = 50%/>
</p>

## Some notes on HW1

### Make sure the code you run is the code you write

- It's better to "open folder" in your IDE
- Try not to `git clone` twice if you don't understand what it means.
- Check the top bar of your IDE and `pwd` to make sure.

### leviOSA

```python
s = 'leviOSA'
assert s[:2] == 'le'
assert s[1:4] == 'evi'
assert s[5:] == 'SA'
assert s[-2:] == 'SA'
assert s[-2: -1] == 'S'
```

### print_n

- `range(start, stop)` does NOT include `stop`.
- Default function argument, `range` has a `step`
- `range` may produce nothing.

## L-value & R-value

Key: Is there an assignment? 

```python
def f(a):
  '''
  Doc string is an R-value
  '''
  a = a + 1
  return a

f(1)
a = f(2)
```

## Scope

### Curse of namespace

- Function names are also in the namespae
  - If you have a variable that has the same name as a function, the function "disappears"
  - You can "return"/"assign" a function
- Built in namespaces can be changed, don't name your variable as names in built in name.
  - `True, False = False, True`
  - `list = [1, 2, 3, 4]`

[Source code](./src/scope.py)  
[Click here to run it!](http://www.pythontutor.com/visualize.html)

## Recursion

1. You know the answer the smallest scoped problem, don't forgot to write them down("Base case" according to textbook).
2. Part of the problem is the same with a smaller scope.("Recursive case")

**Don't create a variable that shadows your function name.**

### n Factorial
[Source code](./src/n-factorial.py)

- loop based:
  - `Factorial(n) = n * (n-1) * (n-2) ... 1`
- recursion based: 
  1. Base case: `Factorial(1) = 1` 
  2. Recursive case: `Factorial(n) = n * Factorial(n-1)` given `n > 1` 


### [Tower of Hanoi](https://en.wikipedia.org/wiki/Tower_of_Hanoi)
[Source code](./src/hanoi.py)

- loop based:
  - :(
- recursion based:
  1. Base case: If `n = 1`, I just move the ONLY disk from `start` to `end` and I am done!
  2. Recursive case: To move n disks from `start` to `end`, I need to:
     1. Move top `(n-1)` disks from `start` to `cache` (Same job with smaller `n` here)
     2. Move disk `n` from `start` to `end`
     3. Move top `(n-1)` disks left in the `cache` to `end`(Same job again!)
