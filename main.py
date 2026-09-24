try:
    enteries = int(input("Pls enter the number of enteries:"))
except ValueError:
    print("Enteries must a number not a letter or a symbol")


for i in range(0,enteries):
    name = input("enter Name :")
    try:
        marks = int(input("enter marks:"))
        file = open("marks.txt","a")
        file.write(f"{name} got {marks} marks \n")
        # file.close()2
    except ValueError:
        print("enter a valid number")
        break

file = open("marks.txt","r")
data = file.read()
print(data)