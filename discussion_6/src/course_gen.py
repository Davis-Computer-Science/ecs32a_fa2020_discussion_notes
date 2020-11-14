from person import Person


class Course:
    def __init__(self, persons):
        self.num = len(persons)
        self.students = persons
        self.scores = [0] * self.num

    def __len__(self):
        return self.num

    def __iter__(self):
        idx = 0
        while idx < len(self):
            yield (self.students[idx], self.scores[idx])
            idx += 1

    def __repr__(self):
        return "Course {{ num: {}, students: {}, scores: {}}}".format(self.num, repr(self.students), self.scores)


if __name__ == "__main__":
    peter = Person("Peter", 24)
    alice = Person("Alice", 23)
    bob = Person("Bob", 24)
    charles = Person("Charles", 23)

    ecs032a = Course([peter, alice, bob, charles])
    for (student, score) in ecs032a:
        print("{} My scrore is {}".format(student, score))
