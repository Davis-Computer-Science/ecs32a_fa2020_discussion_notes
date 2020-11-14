from person import Person


class Course:
    def __init__(self, persons):
        self.num = len(persons)
        self.students = persons
        self.scores = [0] * self.num

    def __len__(self):
        return self.num

    def __iter__(self):
        return CourseIter(self)

    def __repr__(self):
        return "Course {{ num: {}, students: {}, scores: {}}}".format(self.num, repr(self.students), self.scores)


class CourseIter:
    def __init__(self, course):
        self.course = course
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < self.course.num:
            idx = self.idx
            self.idx += 1
            return (self.course.students[idx], self.course.scores[idx])
        else:
            raise StopIteration


if __name__ == "__main__":
    peter = Person("Peter", 24)
    alice = Person("Alice", 23)
    bob = Person("Bob", 24)
    charles = Person("Charles", 23)

    ecs032a = Course([peter, alice, bob, charles])
    for (student, score) in iter(ecs032a):
        print("{} My scrore is {}".format(student, score))
