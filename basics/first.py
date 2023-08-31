name = "Laughter"
age = 55
print(f"Hi {name} you are {age} years old")

birth_year = input("what year were you born?")
age = 2023 - int(birth_year)
print(f"your age is {age}")


username = input("what is your username?")
password = input("what is your password?")
print(f"{username} your password is {password}")


username = input("what is your username?")
password = input("what is your password?")
password_lenght = len(password)
hidden_password = "*" * password_lenght
print(f"{username}, your password {hidden_password} is {password_lenght} letters long")

is_magiician = False
is_expert = True

if is_magiician and is_expert:
    print("You are a master")
elif is_magiician and not is_expert:
    print("at least you are getting there")
else:
    print("you need magic")

i = 0
for i in range(1, 11):
    i += 1
    print(i)
print(i)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
counter = 0
for i in my_list:
    counter += i
print(counter)

picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
]

for image in picture:
    for row in image:
        if row == 1:
            print("*", end="")
        else:
            print(" ", end="")
    print("")

# check for duplicate
some_list = ["a", "b", "c", "b", "d", "e", "n", "n"]

duplicate = []
for value in some_list:
    if some_list.count(value) > 1:
        duplicate.append(value)
print(list(set(duplicate)))
