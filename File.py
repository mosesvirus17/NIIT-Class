# print("Q1","File handling is the process of creating, opening, reading, writing, appending and closing files using Python. Python provides built-in functions such as open(), read(), write() and close() for this purpose. It is used to save records,user input and other information.")

# print("Q2","Writing puts new content into a file and erases any existing content \n Appending adds new content to the end of the file and keeps the existing content.")

# print("Q3","(r)Read mode Opens an existing file for reading only \n (w)Write mode. Creates a new file, or overwrites an existing file’s content. \n (a)Append mode. Adds data to the end of a file without deleting existing content. \n (x)Exclusive creation mode. Creates a new file and raises an error if the file already exists.")

# print("Q4","The open function opens a file and returns a file object. Through this object the program can read from or write to the file.")

# print("Q5","write(W) writes a string into an open file \n close(c) closes the file after use. This saves any data still held in the buffer, frees system resources and prevents file corruption or data loss.")

# print("Q6","All the existing content is erased and the file is ready for new content. The file is not deleted, only emptied. If the file does not exist, a new one is created.")

# Name = input("Enter your name? ")
# Age = input("Enter your Age? ")
# Course = input("Enter your Course? ")

# with open("student7.txt", "w") as file:
#      file.write(f"name: {Name}\n ")
#      file.write(f"age: {Age}\n ")
#      file.write(f"course: {Course}\n ")
# print("Q7","student.txt created successfully.")

# with open("School.txt", "w") as file:
#  print("Q8", "Welcome to Python Programming Class")

# Department = input("Enter Your Department")
# Level = input("Enter Your Level")

# with open("student7.txt",  "a") as file:
#   file.write(f"department: {Department}\n")
#   file.write(f"Level: {Level}\n")
#   print("Q9","Successful")


name = input("Enter your name: ")
age = input("Enter your age: ")
address = input("Enter your home address: ")

with open("details.txt", "w") as file:
  file.write(f"name: {name}\n")
  file.write(f"age: {age}\n")
  file.write(f"add: {address}\n")
print("Q10", "Successfull")

with open("my_biography.txt", "w") as file:
 file.write("My name is Mr Moses.\n")
 file.write("I am 19 years old.\n")
 file.write("I live in Lagos, Nigeria.\n")
 file.write("I am studying Computer Science at university.\n")
 file.write("I enjoy learning programming and playing football.\n")
print("Biography saved successfully.")

subject = input("Enter your favourite subject: ")
food = input("Enter your favourite food: ")

with open("personal.txt", "a") as file:
 file.write(f"Favourite Subject: {subject}\n")
 file.write(f"Favourite Food: {food}\n")
print("Information added to personal.txt")