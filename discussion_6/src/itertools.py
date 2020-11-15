from person import Person
from course_iter import Course, CourseIter


def my_map(lst, fn):
    '''
    '''
    for i in lst:
        yield fn(i)


def my_filter(lst, predicate):
    '''
    '''
    for i in lst:
        if predicate(i):
            yield i


def my_fold(lst, init, fn):
    curr = init
    for i in lst:
        curr = fn(curr, i)
    return curr

def a_pls_b(a, b):
    return a + b

def is_odd(a):
    return a % 2 == 0


if __name__ == "__main__":
    l = [1, 2, 3, 4, 5, 6, 7, 8]
    odd_pls_one_lst = list(my_map(my_filter(l, is_odd), lambda i: i + 1))
    for i in odd_pls_one_lst:
        print(i)
    total = my_fold(odd_pls_one_lst, 0, a_pls_b)
    print("Total is {}".format(total))