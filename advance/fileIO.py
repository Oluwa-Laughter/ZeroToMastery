with open("sad.txt", mode="w") as file1:  # opens a file and write
    print(file1.write("Hello world"))


with open("app/test.txt", mode="r") as myfile:  # Open file and read in another folder
    print(myfile.read())
