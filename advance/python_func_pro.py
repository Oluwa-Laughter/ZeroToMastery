# FUNCTIONAL PROGRAMMING

from functools import reduce


def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)
    return new_list


print(multiply_by2([1, 2, 3]))


# useful Higher order functions-> map(),filter(),zip(), and reduce()
my_li = [1, 2, 3]

your_li = [10, 20, 30]


def func(i):
    return i * 2


def odd(x):
    return x % 2 != 0


def accumulator(acc, item):
    return acc + item


print(list(map(func, [1, 2, 3, 4])))

print(list(filter(odd, my_li)))

print(list(zip(my_li, your_li)))

print(reduce(accumulator, my_li, 0))

# Lambda expressions -> anonymous function -> one time use function -> lambda param: action(param)

my_list = [5, 4, 3]
print(list(map(lambda item: item**2, my_list)))

print(list(filter(lambda x: x % 2 != 0, my_list)))

print(reduce(lambda acc, item: acc + item, my_list))

a = [(0, 2), (4, 3), (9, 9), (10, -1)]
a.sort(key=lambda n: n[1])
print(a)

# List Comprehension

li = [i for i in "hello"]
print(li)
li2 = [num for num in range(50)]
print(li2)
li3 = [num * 2 for num in range(50)]
print(li3)
li4 = [num * 2 for num in range(50) if num % 2 == 0]
print(li4)

# Set Comprehension

s1 = {i for i in "hello"}
print(s1)
s2 = {num * 2 for num in range(50)}
print(s2)
s3 = {num * 2 for num in range(50) if num % 2 == 0}
print(s3)

# Dictionary Comprehension

sample_dict = {"x": 1, "y": 2}
my_dict = {k: v**2 for k, v in sample_dict.items()}
print(my_dict)

new_dict = {num: num * 2 for num in [1, 2, 3]}
print(new_dict)

# check for duplicate

some_list = ["a", "b", "c", "b", "d", "e", "n", "n"]

duplicate = list(set([v for v in some_list if some_list.count(v) > 1]))
print(duplicate)


# Decorator Pattern -> @decorator_name -> function inside a function -> return a function


def my_decorator(func):
    def wrap_func():
        print("*****")
        func()
        print("*****")

    return wrap_func


@my_decorator
def hello():
    print("heelllloooo")


hello()

# (@my_decorator) same as:

x = my_decorator(hello)
x()

# still same as
my_decorator(hello)()


# decorator pattern with arguments and keyword arguments
def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print("*****")
        func(*args, **kwargs)
        print("*****")

    return wrap_func


@my_decorator
def hello(greetings, emoji):
    print(greetings, emoji)


hello("Hiii", ":)")


# Handling Error -> try, except, else, finally ->
# SyntaxError, TypeError, ValueError, ZeroDivisionError, NameError etc.
def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError:
        print("Enter a number")
    else:
        pass
    finally:
        pass


# Generators -> yield keyword (return a generator object) -> next() function to iterate through the generator object
def fib(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        t = a
        a = b
        b = t + a


for x in fib(100):
    print(x)


# same as
def fib2(num):
    a = 0
    b = 1
    result = []
    for i in range(num):
        result.append(a)
        t = a
        a = b
        b = t + a
    return result


print(fib2(20))
