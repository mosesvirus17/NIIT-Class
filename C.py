print("Q1","varaiable are container that store value")

print("Q2","my_name")

name = "David"
print("Q3",name)  #David

print("Q4","Hello is a primitive data type which is a sring")

print("Q5","25 is a integerr")

print("Q6","3.14 is a float")

print("Q7","Boolean is a True data tpye")

print("Q8","int is a whole number and float is a decimal number")

x = 10
y = 5
print("Q9",x + y)  #15

x = 10  
y = 3
print("Q10",x % y)  #1

print("Q11", "It is a Arithematic oprator")

print("Q12","= is a assignment operator that used as a varable and == is a relational operator that is used to compare vale")

x = 10
y += 5
print("Q13",x)  #15

age = 18
print("Q14",age > 16)   #True

a = 10
b = 20
print("Q15",a == b)    #False

print("Q16", "An ordered, changeable collection of items, written in square brackets")

print("Q17",["Apple", "Banana", "Orange"])

fruit = ["Apple", "Banana", "Orange"]
print("Q18",fruit[0])

number= [10, 20, 30, 40]
print("Q19",number[2])


number = [2, 4, 6]
number.append(8)
print("Q20", number)

number = [1, 2, 3]
number.append(4)
print("Q21", number)

name = ["Ape", "Mos", "Mp"]
print(name.remove("Ape"))
print("Q22",name)

name = ["John", "Mary", "Peter"]
name.remove("Mary")
print("Q23", name)

print("Q24", "It Short the list in place, Accending by default")

print("Q25", "It Reverses the oder of the list in place")
def greet():
  print("Q26", "Hello")
greet()

print("Q27" "To package resuable code under a name so you can run it whenever needed instead of rewriting it")

def add(a, b):
  return a + b
result = add(5, 3)
print("Q28", result)

print("Q29", "Parameter is a variable in the function while an agument is the actual vale passed in when calling it")
number = [2, 4, 6]
def double(number):
    return number * 2
print("Q30", double(number[1]))