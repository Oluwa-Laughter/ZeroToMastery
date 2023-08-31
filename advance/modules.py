# modules and packages
import random  # random module and package
import re  # regular expressions module and package

answer = random.randint(1, 10)

while True:
    try:
        choice = int(input("choose from 1~10: "))
        if 0 < choice < 11:
            if choice == answer:
                print("You win!!")
                break
    except ValueError:
        print("enter a number")


# regular expressions (regex) -> pattern matching
# password checker exercise using regex

pattern = re.compile(r"[a-zA-Z0-9$%#@]{7,}[0-9]")
password = "jskwjwii@678"
a = pattern.fullmatch(password)
print(a)
