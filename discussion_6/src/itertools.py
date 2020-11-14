from person import Person
from course_iter import Course, CourseIter


def my_map(self, fn):
    for i in self:
        yield fn(i)


def my_filter(self, predicate):
    '''
    '''
    for i in self:
        if predicate(i):
            yield i


l = [1, 2, 3, 4, 5, 6, 7, 8]

for i in my_map(my_filter(l, lambda i: i % 2 == 0), lambda i: i + 1):
    print(i)
