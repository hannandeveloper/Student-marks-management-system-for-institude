try:
    entries = int(input("Please enter the number of entries: "))
except ValueError:
    print("Entries must be a number, not a letter or symbol.")
    entries = 0


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def save(self):
        with open("marks.txt", "a") as file:
            file.write(f"{self.name} got {self.marks} marks\n")


for _ in range(entries):
    name = input("Enter name: ")
    try:
        marks = int(input("Enter marks: "))
        Student(name, marks).save()
    except ValueError:
        print("Enter a number.")
        break


with open("marks.txt", "r") as file:
    data = file.read()
print(data)