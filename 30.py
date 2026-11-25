Name = "Moses"
Age = 19
Height = "6ft"
Status = "Student"

print("Q1",Name)
print("Q1",Age)
print("Q1",Height)
print("Q1",Status)

a, b = 10, 3
x, y = 4.5, 1.5
print("Q2","Addition:", a + b, x + y)
print("Q2","Subtraction:", a - b, x - y)
print("Q2","Multiplication:", a * b, x * y)
print("Q2","Division:", a / b, x / y)

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
colour = input("Enter your favourite colour: ")

print("Q3",f"My name is {Name}, I am {Age} years old and my favourite colour is {colour}.")

num = 10
num2 = 20.29
name = "Ada"
Value = True

print("Q4",num, type(num), num2, type(num2), (name, type(name), (Value, type(Value))))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Q5","Sum:", a + b)
print("Q5","Product:", a * b)
print("Q5","Difference:", a - b)

name = "Chidi"
s1, s2, s3, s4, s5 = 70, 65, 80, 55, 90
status = "Passed"
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print("Q6","Name:", name)
print("Q6","Scores:", s1, s2, s3, s4, s5)
print("Q6","Status:", status)
print("Q6","Total:", total)
print("Q6","Average:", average)

fruits = ["apple", "banana", "mango", "orange", "pear", "grape", "pineapple", "guava", "lemon", "papaya"]
print("Q7","First:", fruits[0])
print("Q7","Last:", fruits[-1])
print("Q7","Total items:", len(fruits))

students = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
students.append(input("Enter another student's name: "))
print("Q8","Updated list:", students)

Number =[1,2,3,4,5,6,7,8,9,10]
print("Q9","Even numbers:", [n for n in Number if n % 2 == 0])

nums = [15, 8, 25, 40, 12, 30, 5, 18]
largest = nums[0]
smallest = nums[0]
total = 0
for n in nums:
  if n > largest:
        largest = n
  if n < smallest:
       smallest = n
total += n
print("Q10","Largest:", largest)
print("Q10","Smallest:", smallest)
print("Q10","Sum:", total)

shopping = ["bread", "milk", "eggs", "rice", "sugar"]
for _ in range(2):
shopping.append(input("Add a product: "))
item = input("Enter a product to remove: ")
if item in shopping:
  shopping.remove(item)
else:
print("Product not found.")
print("Q11","Final shopping list:", shopping)


numbers = [5, 12, 18, 23, 7, 30, 41, 9, 15, 2]
n = int(input("Enter a number: "))
if n in numbers:
print(f"{n} exists at position (index) {numbers.index(n)}")
else:
print("Q12", f"{n} is not in the list.")

student = {"name": "Ada", "age": 20, "gender": "Female","department": "Computer Science", "matric_no": "CSC/2024/001"}
for key, value in student.items():
print("Q13", f"{key}: {value}")

products = {"Bread": 800, "Milk": 1200, "Rice": 5000, "Eggs": 2500, "Sugar": 1500}
for name, price in products.items():
print("Q14", f"{name}: {price}")

student = {"name": "Ada", "age": 20, "score": 65}
student["score"] = int(input("Enter the new score: "))
print("Q15", "Updated information:", student)

scores = {"Ade": 67, "Bola": 82, "Chidi": 75, "Dayo": 90, "Emeka": 58}
top_name, top_score = None, -1
for name, score in scores.items():
if score > top_score:
top_name, top_score = name, score
print("Q16", f"Highest score: {top_name} with {top_score}")

account = {"account_name": "Ada Obi", "account_number": "1234567890", "balance": 10000.0}
choice = input("Type 'deposit' or 'withdraw': ").strip().lower()
amount = float(input("Enter amount: "))
if choice == "deposit":
account["balance"] += amount
elif choice == "withdraw":
if amount <= account["balance"]:
account["balance"] -= amount
else:
    print("Insufficient funds.")
else:
    print("Invalid choice.")
print("Q17","Current balance:", account["balance"])

numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print("Q18",numbers)

class_a = {"Ade", "Bola", "Chidi", "Dayo"}
class_b = {"Chidi", "Emeka", "Dayo", "Funke"}
print("Q19","Students in both classes:", class_a & class_b)

a = set(range(1, 11))
b = set(range(5, 16))
print("Q20","All elements:", a | b)
print("Q20","Common elements:", a & b)
print("Q20", "In first but not second:", a - b)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("Q21","First day:", days[0])
print("Q21","Last day:", days[-1])
print("Q21","Number of days:", len(days))
print("Q21","Saturday exists:", "Saturday" in days)

students = ("Ade", "Bola", "Chidi", "Dayo", "Emeka")
lst = list(students)
lst.append("Funke")
lst.append("Gozie")
lst.remove("Bola")
students = tuple(lst)
print("Q22",students)


with open("students.txt", "w") as f:
   f.write("Name: Ada\nAge: 20\nDepartment: Computer Science\n")
print("Q23","students.txt created.")


names = ["Ade", "Bola", "Chidi", "Dayo", "Emeka"]
with open("students.txt", "w") as f:  # "w" replaces previous content
for n in names:
     f.write(n + "\n")
print("Q24","students.txt overwritten with five names.")


with open("students.txt", "a") as f:  # "a" keeps previous content
for n in ["Funke", "Gozie", "Hauwa"]:
     f.write(n + "\n")
print("Q25","Three names appended.")


try:
with open("students.txt", "r") as f:
   print(f.read())
except FileNotFoundError:
print("Q26","students.txt not found. Run q23 first.")


sentences = ["Today was a good day.", "I learned about Python files.", "I wrote some code.", "I fixed a few bugs.", "Tomorrow I will practise more."]
with open("diary.txt", "w") as f:
for s in sentences:
f.write(s + "\n")
with open("diary.txt", "r") as f:
print("Q27:", f.read())

name = input("Enter your name: ")
language = input("Enter your favourite programming language: ")
with open("profile.txt", "a") as f:
f.write(f"{name} - {language}\n")
print("Q28","Saved to profile.txt.")


if not os.path.exists("numbers.txt"):  # create sample data if missing
with open("numbers.txt", "w") as f:
f.write("10\n20\n30\n40\n")
total = 0
with open("numbers.txt", "r") as f:
for line in f:
line = line.strip()
if line:
total += float(line)
print("Q29","Sum of numbers:", total)

    while True:
        print("\n1. Add student record\n2. View all records\n3. Count records\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = input("Age: ")
            score = input("Exam score: ")
            with open("records.txt", "a") as f:
                f.write(f"{name},{age},{score}\n")
            print("Record saved.")
        elif choice == "2":
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    for line in f:
                        name, age, score = line.strip().split(",")
                        print(f"Name: {name} | Age: {age} | Score: {score}")
            else:
                print("No records yet.")
        elif choice == "3":
            count = 0
            if os.path.exists("records.txt"):
                with open("records.txt", "r") as f:
                    count = sum(1 for line in f if line.strip())
            print("Total records:", count)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    choice = input("Enter question number (1-30) or 'all': ").strip().lower()
    if choice == "all":
        for i in range(1, 31):
            print(f"\n--- Question {i} ---")
            globals()[f"q{i}"]()
    elif choice.isdigit() and 1 <= int(choice) <= 30:
        globals()[f"q{choice}"]()
    else:
        print("Invalid choice.")
