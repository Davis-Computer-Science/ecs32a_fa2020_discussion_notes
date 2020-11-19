class Person:
    def __init__(self, name, age, height=180):
        self.name = name
        self.age = age
        self.happiness = 0
        self.height = height

    def get_age(self):
        self.happiness -= 1
        return self.age

    def get_happiness(self):
        return self.happiness

    def __len__(self):
        return self.height

    def __repr__(self):
        return "Person {{ age: {}, name: {}, happiness: {}, height: {} }}".format(self.name, self.age, self.happiness, self.height)

    def __str__(self):
        # Bad practise, DON'T DO IT.
        self.happiness += 1
        return "Hi, I am {}, I'm not telling you my age.".format(self.name)

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age and self.height == other.height


if __name__ == "__main__":
    peter = Person("Peter", 24)
    print("This object is: {}".format(repr(peter)))
    print(str(peter))
    print("-Are you happy? -My happyness: {}".format(peter.get_happiness()))
    print("-How old are you? -{}".format(peter.get_age()))
    print("-Are you happy now? -My happyness: {}".format(peter.get_happiness()))

    alice = Person("Alice", 23, 170)
    print("-Peter, what's your height? -{} cm".format(len(peter)))
    print("-Alice, how about you? -{} cm".format(len(alice)))
    print("-Alice and Peter are the same: {}".format(alice == peter))
