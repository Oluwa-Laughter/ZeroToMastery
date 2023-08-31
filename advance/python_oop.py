# Functions
def highest_even(li: list[int]) -> int:
    """
    This functions checks for highest even numbers.
    """
    even_numbers = []
    for even in li:
        if even % 2 == 0:
            even_numbers.append(even)
    return max(even_numbers)


print(highest_even([11, 2, 3, 4, 5.9, 10]))


# walrus operator
def walrus(a) -> str:
    """
    This function test for walrus operator
    """
    if (n := len(a)) > 10:
        print(f"too long {n} elements")

    while (n := len(a)) > 1:
        a = a[:-1]
        print(n)


walrus(a="helllloooooo")

x = 2


def confusion():
    global x
    return x


print(x)
print(confusion())


# Object Orientated Programming (OOP) -> classes and objects
class PlayerCharacter:
    # Class Object Attribute
    membership = True

    def __init__(self, name, age):
        if age > 18:
            self.name = name
            self.age = age

    def run(self):
        print("run")

    def speak(self):
        return f"my name is {self.name}, and I am {self.age} years old"


player1 = PlayerCharacter("Cindy", 44)
player2 = PlayerCharacter("Tom", 21)
print(player1.name)
print(player1.age)
print(player1.speak())
print(player2.speak())

player1.run()


class Dog:
    # class attribute
    species = "Canis familiaris"

    def __init__(self, name, age) -> str:
        self.name = name  # instance attribute
        self.age = age

    # instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"


buddy = Dog("Buddy", 9)
miles = Dog("Miles", 4)

# we access instance attribute here
print(buddy.name)
buddy.age = 10  # changed the .age attribute of the buddy to 10 here
print(buddy.age)
print(miles.name)
print(miles.age)

# we can access class attributes same way
print(buddy.species)

miles.species = "Felis silvestris"  # changed the .species attribute of miles here
print(miles.species)

print(miles.description)


class Car:
    def __init__(self, colour, mileage) -> str:
        self.colour = colour
        self.mileage = mileage

    @classmethod
    def adding_things(cls, num1, num2):
        return cls("Teddy", num1 + num2)

    # or

    @staticmethod
    def adding_things(num1, num2):
        return num1 + num2


blue_car = Car("Blue", 20000)
red_car = Car("Red", 30000)

print(f"The {blue_car.colour} car has {blue_car.mileage} miles ")
print(f"The {red_car.colour} car has {red_car.mileage} miles ")
# applying loop
for car in (blue_car, red_car):
    print(f"The {car.colour} car has {car.mileage} miles ")

yellow_car = car.adding_things(2, 4)
print(f"There are {yellow_car} yellow cars in total")


# Inheritance
class Pet:
    def __init__(self, name, age) -> str:
        self.name = name  # instance attribute
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I don't know what to say")


class Dog(Pet):
    def __init__(self, name, age, colour) -> str:
        super().__init__(name, age)
        self.colour = colour

    def speak(self):
        print("bark")

    def show(self):
        print(
            f"I am {self.name},I am {self.age} years old and my colour is {self.colour}"
        )


class Cat(Pet):
    def speak(self):
        print("meow")


p = Pet("Jack", 25)
c = Cat("Tim", 20)
d = Dog("Bill", 20, "Yellow")
d.show()
c.speak()


# Multiple inheritance
class PetAll(Cat, Dog):
    pass


# The Dunder Methods
class Toy:
    def __init__(self, colour, age):
        self.colour = colour
        self.age = age
        self.my_dict = {"name": "Yoyo", "has_pet": False}

    def __str__(self):
        return f"{self.colour}"

    def __len__(self):
        return 5

    def __call__(self):
        return "yes?"

    def __getitem__(self, i):
        return self.my_dict[i]


action_figure = Toy("red", 0)
print(action_figure.__str__())
# same as below
print(str(action_figure))

print(len(action_figure))  # this is the len method
print(action_figure())  # this is the call method
print(action_figure["name"])  # this is the getitem method


class SuperList(list):
    def __len__(self):
        return 1000


SuperList1 = SuperList()
print(len(SuperList1))
SuperList1.append(5)
print(SuperList[0])
print(issubclass(SuperList, list))
print(issubclass(list, object))
