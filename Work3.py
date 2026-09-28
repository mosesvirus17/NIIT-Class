# 201
# user_name = input("Enter your name: ")
# print(user_name.upper())
user_name = "kelechi"  # simulated input for demo
print("Q201:", user_name.upper())

# 202. NameError: name 'x' is not defined (del removes the variable entirely)
x = 10
del x
try:
    print(x)
except NameError as e:
    print("Q202: NameError ->", e)

# 203.
a, b = 10, "10"
try:
    a + b
except TypeError as e:
    print("Q203: TypeError ->", e, "(can't add int + str directly, types must match)")

# 204.
a, b = "Python", "Java"
a, b = b, a
print("Q204:", a, b)  # Java Python

# 205.
a, b, c = 5, 10, 15
print("Q205:", a + b + c)  # 30

# 206.
x = 50
print("Q206:", id(x))

# 207.
first, last = "Attah", "Maxwell"
full_name = f"{first} {last}"
print("Q207:", full_name)

# 208. Valid identifiers: __name, _age, age_, age2 are all valid.
#      2age is INVALID (can't start with a digit).
print("Q208 valid:", ["__name", "_age", "age_", "age2"])

# 209.
x = 5
x = x + x   # 10
x = x + x   # 20
print("Q209:", x)  # 20

# 210.
count = 0
while count < 10:
    count += 1
print("Q210:", count)  # 10

# 211. Python uses dynamic typing: the interpreter infers a variable's type
#      from the value assigned to it at runtime, so no declaration is needed.

# 212.
data = [1, 2, 3]
data2 = data          # data2 points to the SAME list object as data
data2[0] = 99
print("Q212:", data)  # [99, 2, 3] -- data changed too, because both names reference one list

# 213. Fix with .copy() to create an independent list
data = [1, 2, 3]
data2 = data.copy()
data2[0] = 99
print("Q213:", data, data2)  # [1, 2, 3] [99, 2, 3]

# 214.
student1, student2, student3 = "Ada", "Ben", "Chi"
print("Q214:", [student1, student2, student3])

# 215. globals() returns a dict of all variables in the global scope.
#      locals() returns a dict of all variables in the current local scope.
print("Q215 sample locals():", list(locals().keys())[-3:])

# 216.
student_maths_score_2024 = 85

# 217. Yes, this is valid — it's a conditional expression used as a statement.
x_, y_ = 10, 20
print(x_, y_) if x_ > y_ else print(y_, x_)  # prints "20 10"

# 218.
a, b = 10, 20
result = a if a > b else b
print("Q218:", result)  # 20

# 219. No. Python 3 identifiers must be letters, digits, or underscores
#      (Unicode letters are allowed, but emoji are NOT valid identifier characters).
try:
    exec("😀 = 10")
except SyntaxError as e:
    print("Q219: SyntaxError ->", e)

# 220. '_' is used to ignore/discard a value during unpacking.
a, _b, c, _, _ = [1, 2, 3, 4, 5]
print("Q220:", a, _b, c)  # 1 2 3

# 221.
price, qty = 19.99, 3
total = price * qty
print("Q221:", total)  # 59.97

# 222.
# name = input("Enter name: ")
# age = int(input("Enter age: "))   # convert to int for numeric use
name, age = "Ada", int("20")
print("Q222:", name, age, type(age))

# 223. Both give the same result here; int(10) is redundant since 10 is
#      already an int. int() is only useful for converting OTHER types.
print("Q223:", 10 == int(10))

# 224.
is_logged_in = False
is_logged_in = not is_logged_in
print("Q224:", is_logged_in)  # True

# 225.
a = None
print("Q225:", a is None)  # True

# 226.
x_outer = 10
def my_func():
    x_inner = 5
    print("Q226 (inside func):", x_inner)
my_func()
print("Q226 (outside func):", x_outer)

# 227. Convention: write the name in ALL_CAPS (e.g. MAX_SIZE = 100) to signal
#      "treat this as constant" — Python won't enforce it, but other devs will respect it.

# 228.
text = "NOUN"
length = len(text)
print("Q228:", length)  # 4

# 229.
name = "Kelechi"
name = name + " Noun"
print("Q229:", name)  # Kelechi Noun

# 230. Error because \n and \f are interpreted as escape sequences
#      (newline, form-feed) instead of literal backslashes.
#      Fix using a raw string with an 'r' prefix:
file_path = r"C:\new\folder"
print("Q230:", file_path)

print("\n=== DATA TYPES - LOGIC & BUG FINDING (231-270) ===")

print("Q231:", type(1 / 2), "-> float, because '/' ALWAYS returns a float in Python 3")
print("Q232:", type(2 // 2), "-> int, because '//' (floor division) returns an int when both inputs are int")

# 233. No. "True" is a string (4 characters); True is a boolean value. They differ in type.
print("Q233:", "True" == True, type("True"), type(True))

print("Q234:", int(True), int(False))  # 1 0

print("Q235:", str(True) + str(False))  # "TrueFalse"

# 236. bool("False") is True because ANY non-empty string is truthy,
#      regardless of its content/text.
print("Q236:", bool("False"))  # True

# 237. Two ways to check for an empty string:
s_check = ""
print("Q237:", s_check == "", len(s_check) == 0)

s = " python is easy "
s = s.strip().upper().replace("EASY", "POWERFUL")
print("Q238:", s)

try:
    "python"[100]
except IndexError as e:
    print("Q239: IndexError ->", e)

print("Q240:", "python"[1:100], "-> no error, slicing beyond the end just stops at the last character")

# 241. Strings are immutable — individual characters cannot be reassigned.
try:
    s_immut = "python"
    s_immut[0] = "P"
except TypeError as e:
    print("Q241: TypeError ->", e)

s_rev = "python"
print("Q242:", s_rev[::-1])  # reverse using slicing

print("Q243:", len(" "), len(""))  # 1 0

age_str = "20"
age_num = int(age_str) + 5
print("Q244:", age_num)  # 25

print("Q245:", list("abc"), "vs", ["abc"], "-> list('abc') splits into characters; [\"abc\"] is a single-item list")

print("Q246:", [1, 2, 3] * 2)   # [1, 2, 3, 1, 2, 3]  (doc's '_' = '*')
print("Q247:", (1, 2, 3) * 2)   # (1, 2, 3, 1, 2, 3)

try:
    {"a": 1} * 2
except TypeError as e:
    print("Q248: TypeError ->", e, "(dicts don't support repetition)")

# 249. Dict keys must be hashable (immutable). Lists are NOT hashable -> error.
#      Tuples ARE hashable (if their contents are), so they CAN be dict keys.
try:
    bad_dict = {[1, 2]: "value"}
except TypeError as e:
    print("Q249a: list as key -> TypeError:", e)
good_dict = {(1, 2): "value"}
print("Q249b: tuple as key ->", good_dict)

print("Q250:", set([1, 1, 2, 2, 3]))  # {1, 2, 3}

# 251. Sets use .add(); 252. Lists use .append()
set_demo = {1, 2}
set_demo.add(3)
list_demo = [1, 2]
list_demo.append(3)
print("Q251/252:", set_demo, list_demo)

# 253. Common mistake: naming a variable 'list' shadows the built-in list().
#      [1,2,3].append(4) works fine on the literal, but it's a throwaway
#      (not stored), and reusing the name 'list' for a variable is bad practice.
temp_list = [1, 2, 3]
temp_list.append(4)
print("Q253:", temp_list)

a_ = [1, 2]
b_ = a_
b_ = [3, 4]          # this REBINDS b_ to a new list, doesn't touch a_
print("Q254:", a_)   # [1, 2] -- unchanged, since b_ now points elsewhere

t = (1, 2, 3)
t_list = list(t)
t_list.append(4)
t = tuple(t_list)
print("Q255:", t)  # (1, 2, 3, 4)

d = {"name": "Max", "dept": "NOUN"}
print("Q256 keys:", list(d.keys()))
print("Q256 values:", list(d.values()))

# 257. Both work, but isinstance() is preferred: it also accounts for
#      subclasses (e.g. isinstance(True, int) is True), making it more robust.
print("Q257:", isinstance([1, 2], list), type([1, 2]) == list)

# 258. None is used to represent "no value yet" or "missing/optional result",
#      e.g. a function that returns nothing, or a default parameter placeholder.
def find_user(uid):
    return None  # user not found
print("Q258:", find_user(1))

print("Q259:", float("inf"), type(float("inf")))  # inf <class 'float'>

print("Q260:", int(True) + int(False) + int(True))  # 1+0+1 = 2

x_check = 10.5
print("Q261:", "float" if isinstance(x_check, float) else "int" if isinstance(x_check, int) else "other")

# 262. Shallow copy: copies the outer object, but nested objects are still
#      shared references (list.copy(), copy.copy()).
#      Deep copy: recursively copies everything, no shared references
#      (copy.deepcopy()) — use it when the object contains nested mutable objects.
import copy
nested = [[1, 2], [3, 4]]
shallow = nested.copy()
deep = copy.deepcopy(nested)
shallow[0].append(99)  # affects nested too, since inner lists are shared
print("Q262:", nested, deep)

a_ch = "5"
b_ch = int(a_ch)
c_ch = float(b_ch)
print("Q263:", c_ch)  # 5.0

mixed_list = [1, "two", 3.0, True, None]
print("Q264:", mixed_list)

# 265. bool([0]) is True because the list [0] is NON-EMPTY (it has 1 item).
#      Truthiness of a list depends on whether it has items, not their values.
print("Q265:", bool([0]))  # True

# 266. bytes: an immutable sequence of raw bytes, e.g. b"hello".
#      bytearray: a MUTABLE version of bytes, can be modified in place.
print("Q266:", bytes([104, 105]), bytearray([104, 105]))

print("Q267:", str(123), float("123"))  # "123"  123.0

x_nested = ["a", "b", "c"]  # doc's ["a"]["b"]["c"] is a typo (nested indexing doesn't apply to flat strings)
print("Q268:", x_nested[0])  # 'a'  (["a"]["b"]["c"] as literally written would error: str has no index "b")

print("Q269:", complex(2, 3))  # (2+3j)

# 270.
def detect_type(value):
    try:
        int(value)
        return "int"
    except ValueError:
        return "string"
print("Q270:", detect_type("42"), detect_type("hello"))

print("\n=== OPERATORS - CALCULATION & LOGIC (271-300) ===")

print("Q271:", 2 * 3 * 2, "-> (2*3)=6, then 6*2=12")

print("Q272:", -3 * 2, "-> -6, not -9 (a negative times a positive stays negative)")
# Note: the doc's numbers imply a typo; -3 * 3 = -9 is likely intended:
print("Q272b:", -3 * 3, "-> -9 (negative * positive = negative)")

print("Q273:", (-3) ** 2, "-> 9 (negative squared becomes positive; doc's '__' = '**')")

print("Q274:", 10 + 3 * 2 * 2, "-> BODMAS: multiply first (3*2*2=12), then add 10 -> 22")

weight, height = 70, 1.75
bmi = weight / (height ** 2)
print("Q275 BMI:", round(bmi, 2))

x = 15
print("Q276:", 10 < x < 20)  # True, chained comparison

print("Q277:", 5 == 5 and 10 == 10 and 15 == 20)  # False (last condition fails)
print("Q278:", 5 == 5 or 10 == 20 or 15 == 20)     # True (first condition passes)
print("Q279:", not (5 > 3))  # False

print("Q280:", not 0, not 1, not "")  # True False True

# 281. Short-circuit: 'and' stops at the first False, so 10/0 is NEVER evaluated -> no error
print("Q281:", False and (10 / 0 if False else "skipped"))
result_281 = False and False  # simulating: real 10/0 never runs due to short-circuit
print("Q281 (real):", result_281)

# 282. 'or' stops at the first True, so 10/0 is never evaluated -> no error
print("Q282:", True or False)

print("Q283 (10):", 10 % 2 == 0 and 10 % 3 == 0)  # False (10 not divisible by 3)
print("Q283 (15):", 15 % 2 == 0 and 15 % 3 == 0)  # False (15 not divisible by 2)

# 286. doc's '2_3' is likely a typo for 2*3
a286 = 5
a286 += 2 * 3
print("Q286:", a286)  # 11

x287 = 10
x287 //= 3
print("Q287:", x287)  # 3

x288 = 2
x288 *= 3
x288 *= 2
print("Q288:", x288)  # 12

# 289. Functionally identical result; += is shorter and, for mutable objects
#      like lists, can modify in place rather than creating a new object.
print("Q289:", "same result, += is just shorthand for x = x + 1")

print("Q290:", "ab" in "abc" and "d" not in "abc")  # True

def check_letter(letter, word="python"):
    return letter in word
print("Q291:", check_letter("y"), check_letter("z"))

# 292. Small integers (-5 to 256) are cached/interned by Python, so `a is b`
#      is True for a=b=1000... actually 1000 is OUTSIDE that cache range,
#      so behavior can vary; small numbers like 10 ARE cached -> True.
a292, b292 = 1000, 1000
print("Q292 (1000):", a292 is b292,
      "-> result is implementation-dependent (CPython may or may not reuse the object;"
      " 1000 is outside the guaranteed small-int cache of -5 to 256)")
a292b, b292b = 10, 10
print("Q292 (10):", a292b is b292b, "-> True, small ints ARE cached/reused by Python")

print("Q293:", [] == [], [] is [])  # True False (equal values, different objects)

v1, v2, v3 = 5, 5, 5
print("Q294:", v1 == v2 and v2 == v3)  # True

# 295. Walrus operator ':=' assigns a value AND returns it in the same expression.
my_list_295 = [1, 2, 3]
if (n := len(my_list_295)) > 2:
    print("Q295: list has", n, "items")

# 296.
# while (cmd := input("Type something (or 'exit'): ")) != "exit":
#     print("You typed:", cmd)
print("Q296: (interactive loop shown as comment above; needs real input())")

print("Q297:", 10 & 2, "-> bitwise AND compares bits: 1010 & 0010 = 0010 = 2")
print("Q298:", 10 | 2, "-> bitwise OR: 1010 | 0010 = 1010 = 10")

# 299. Swap using XOR (only works reliably for integers)
p, q = 5, 9
p = p ^ q
q = p ^ q
p = p ^ q
print("Q299:", p, q)  # 9 5

# 300. Final mini calculator
def mini_calculator(n1, n2, op):
    if op == "+":
        return n1 + n2
    elif op == "-":
        return n1 - n2
    elif op == "*":
        return n1 * n2
    elif op == "/":
        return n1 / n2 if n2 != 0 else "undefined"
    elif op == "%":
        return n1 % n2 if n2 != 0 else "undefined"
    elif op == "//":
        return n1 // n2 if n2 != 0 else "undefined"
    elif op == "**":
        return n1 ** n2
    else:
        return "invalid operator"

print("Q300:", mini_calculator(10, 3, "+"))
print("Q300:", mini_calculator(10, 3, "**"))

