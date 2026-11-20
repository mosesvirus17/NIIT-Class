student = {"name": "Chidi", "age": 20, "track": "Python"}
print(student)

car = {"brand": "Toyota", "year": 2022}
print(car["brand"])

user = {"name": "Zainab"}
print(user.get("email", "No email provided"))

book = {"title": "Clean Code", "author": "Robert C. Martin"}
book["pages"] = 464
print(book)

wallet = {"balance": 5000}
wallet["balance"] = 7500
print(wallet["balance"])

settings = {"theme": "dark", "notifications": True}
settings.pop("notifications")
print(settings)

prices = {"apple": 200, "banana": 150}
print("apple" in prices)
print("mango" in prices)

person = {"name": "David", "city": "Abuja"}
print(list(person.keys()))
print(list(person.values()))

students = [
    {"name": "Amina", "score": 88},
    {"name": "Tunde", "score": 92}
]
print(students[1]["name"])

phone = {"brand": "Samsung", "model": "Galaxy S23", "price": 650000}

phone["color"] = "black"
phone["price"] = 600000         
print(list(phone.keys()))