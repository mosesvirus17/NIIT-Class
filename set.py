
students = {"John", "Mary", "Victor", "David", "Peter"}
print("Q1:", students)

numbers = {10, 20, 30, 10, 20, 40}
print("Q2:", numbers)

fruits = {"Apple", "Mango", "Orange", "Banana", "Pineapple"}
print("Q3:", fruits)

students = set()
print("Q4:", students)

colours = {"Red", "Blue", "Green"}
colours.add("Yellow")
print("Q5:", colours)

nums = {10, 20, 30}
nums.update([40, 50, 60])
print("Q6:", nums)

names = {"John", "Mary", "Victor", "David", "Peter"}
names.remove("Victor")
print("Q7:", names)

fruits = {"Apple", "Mango", "Orange"}
fruits.discard("Pineapple")
print("Q8:", fruits)

python_students = {"John", "Victor", "Mary", "David"}
java_students = {"Mary", "David", "Peter", "James"}
print("Q9:", python_students.union(java_students))

python_students = {"John", "Victor", "Mary", "David"}
java_students = {"Mary", "David", "Peter", "James"}
print("Q10:", python_students.intersection(java_students))

python_students = {"John", "Victor", "Mary", "David"}
java_students = {"Mary", "David", "Peter", "James"}
print("Q11:", python_students.difference(java_students))

python_students = {"John", "Victor", "Mary", "David"}
java_students = {"Mary", "David", "Peter", "James"}
print("Q12:", python_students.symmetric_difference(java_students))

name_list = ["John", "Mary", "John", "Victor", "Mary", "David", "Victor"]
unique_names = set(name_list)
print("Q13:", unique_names)

Number = {10, 20, 30, 40}
Num= {30, 40, 50, 60}
print("Q14:", Number.intersection(Num))

teams = {"Arsenal", "Chelsea", "Liverpool", "Barcelona", "Real Madrid"}
teams.update(["Man city", "Bayern Munich"])
teams.remove("Chelsea")
print("Q15:", teams)

students = ("John", "Mary", "Victor", "David", "Peter")
print("Q16:", students)

Profile = ("Ada", 20, "Greenfield School", "Nigeria")
print("Q17:", Profile)

numbers = (10, 20, 30, 40, 50)
print("Q18:", numbers[0])

fruits = ("Apple", "Mango", "Orange", "Banana", "Pineapple")
print("Q19:", fruits[2])

names = ("John", "Mary", "Victor", "David")
print("Q20:", names[-1])

numbers = (10, 20, 30, 40, 50, 60)
print("Q21:", numbers[1:5]) 

numbers = (5, 10, 15, 20, 25, 30)
print("Q22:", numbers[:3])

numbers = (5, 10, 15, 20, 25, 30)
print("Q23:", numbers[2:])

fruits = ("Apple", "Mango", "Orange")
fruit_list = list(fruits)
print("Q24:", fruit_list)

fruits = ("Apple", "Mango", "Orange")
fruit_list = list(fruits)
print("Q24:", fruit_list)

fruits = ("Apple", "Mango", "Orange")
fruit_list = list(fruits)
fruit_list[1] = "Banana"
fruits = tuple(fruit_list)
print("Q25:", fruits)

numbers = (10, 20, 30, 40, 50)
num_list = list(numbers)
num_list[0] = 100
numbers = tuple(num_list)
print("Q26:", numbers)

students = ("John", "Mary", "Victor", "David", "Peter")
student_list = list(students)
student_list.append("James")
students = tuple(student_list)
print("Q27:", students)

fruits = ("Apple", "Mango", "Apple", "Orange", "Apple")
print("Q28:", fruits.count("Apple"))

names = ("John", "Mary", "Victor", "David")
print("Q29:", names.index("Victor"))

# 1."set is a python data type structure used to store value multiple value without allowing duplicate and can be changed (mutable) while A tuple is ordered, allows duplicates, and cannot be changed (immutable)."

# 2. "A set stores only unique items. When a value already exists,adding it again has no effect."

# 3. "Both delete an item. If the item is missing, remove() will show KeyError, while discard() while not show anything".

# 4. union() returns all items from both sets (combined, no duplicates). while intersection() returns only the items found in both sets.

# 5.  Tuples are immutable, so their items cannot be changed, added or removed. A list is mutable, so we convert to a list, make the change, then convert back to a tuple.