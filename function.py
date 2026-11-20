def greet(name):
    print("Q1",f"Hello {name}")
greet("student")

def greet(name,age):
  print(f"Hello student {name}, you are {age} years old")
greet("victor",20)

def welcome_student(name, country="Nigeria"):
    print(f"Welcome {name} from {country}!")

welcome_student("Victor")
welcome_student("Victor", "Ghana")

def create_profile(username, role):
    return f"User: {username} Role: {role}"

# Using keyword arguments lets you pass role first
print(create_profile(role="Instructor", username="Victor"))

def add_scores(*scores):
    return sum(scores)

print(add_scores(10, 20))                          # 30
print(add_scores(10, 20, 30, 40, 50))              # 150
print(add_scores(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) 

def total_for_student(name, *scores):
    total = sum(scores)
    return f"{name}'s total score is {total}"

print(total_for_student("Victor", 10, 20, 30))

def student_info(name, age=18):
    print(f"Student: {name}, Age: {age}")

student_info("Victor")       # Student: Victor, Age: 18
student_info("Victor", 20)  

def product_info(name, price):
    return f"Product: {name}, Price: {price}"

print(product_info(price=5000, name="Book"))

def highest_score(*scores):
    return max(scores)

print(highest_score(45, 78, 92, 60)) 

def student_summary(name, country, *scores):
    print(f"{name} from {country} scored a total of {sum(scores)}")

student_summary("Victor", "Nigeria", 40, 30, 30)