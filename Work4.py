
# 301. Yes, Python is dynamically typed (a variable can point to any type,
#      and can be reassigned to a different type). It is also STRONGLY typed
#      (it won't silently convert between incompatible types, e.g. "5"+5 errors).
x = 5
print("Q301:", x)
x = "hello"
print("Q301:", x)

# 302. Bug: input() always returns a STRING, so age + 10 tries to add int to str -> TypeError.
# Fix:
name = "Ada"          # simulated input
age = "20"            # simulated input
age = int(age)        # convert to int before doing math
print("Q302:", age + 10)

# 303. Because Python doesn't pre-declare variables; if the `if` branch never
#      runs, `x` is never created, so referencing it raises NameError.
if False:
    x_never = 10
try:
    print(x_never)
except NameError as e:
    print("Q303: NameError ->", e)

# 304.
name = "Ada Obi"
matric_no = "NOU/2024/001"
course = "Computer Science"
gpa = 4.5
is_active = True
print("Q304:", name, matric_no, course, gpa, is_active)

# 305. Surprise: all three point to the SAME list object, so appending
#      through c affects a and b too.
a = b = c = [1]
c.append(2)
print("Q305:", a, b, c)  # [1, 2] [1, 2] [1, 2]

# 306. Avoid by creating independent objects instead of chaining mutable ones:
a2, b2, c2 = [1], [1], [1]
c2.append(2)
print("Q306:", a2, b2, c2)  # [1] [1] [1, 2]

# 307. NameError: using a variable that was never defined.
#      TypeError: using an operation on the wrong type (e.g. "1"+1).
#      ValueError: right type but invalid value (e.g. int("abc")).

# 308.
try:
    print(undefined_variable)  # crashes on purpose
except NameError as e:
    print("Q308: NameError ->", e)
undefined_variable = 5  # fix: define it first
print("Q308 fixed:", undefined_variable)

# 309.
g_x = 10
def show_x():
    x_local = 20  # a DIFFERENT variable, local to this function
    print("Q309 (inside func):", x_local)
show_x()
print("Q309 (global):", g_x)

# 310.
x_glob = 10
def change_global():
    global x_glob
    x_glob = 20
change_global()
print("Q310:", x_glob)  # 20

# 311. nonlocal lets an inner (nested) function modify a variable from its
#      ENCLOSING function's scope (not global, not fully local).
def outer():
    val = 1
    def inner():
        nonlocal val
        val = 2
    inner()
    return val
print("Q311:", outer())  # 2

# 312. Yes, you can chain assignments. It's fine for immutable values (numbers,
#      strings), but risky for mutable objects (lists/dicts) since all names
#      share the SAME object (see Q305).
a3 = b3 = c3 = 10
print("Q312:", a3, b3, c3)

# 313. '_' is the conventional name for a throwaway variable you don't intend to use.
for _ in range(5):
    pass
print("Q313: looped 5 times using throwaway variable _")

# 314.
first_name, last_name = "Attah", "Maxwell"
full_name_1 = first_name + " " + last_name
full_name_2 = " ".join([first_name, last_name])
full_name_3 = f"{first_name} {last_name}"
print("Q314:", full_name_1, "|", full_name_2, "|", full_name_3)

# 315.
sentence = "I love Python"
word_count = 0
current_word = False
for ch in sentence:
    if ch != " " and not current_word:
        word_count += 1
        current_word = True
    elif ch == " ":
        current_word = False
print("Q315:", word_count)  # 3

# 316.
x316 = 10
y316 = "10"
print("Q316:", x316 is int(y316))  # True here -- 10 is a small int (-5 to 256),
                                     # so CPython reuses the same cached object;
                                     # for larger numbers this would likely be False

# 317.
# name = input("Name: "); age = int(input("Age: ")); phone = input("Phone: ")
# Phone is kept as a STRING because it may start with 0 and is never used in math.
name317, age317, phone317 = "Ada", 20, "08012345678"
print("Q317:", name317, age317, phone317)

# 318. PI = 3.14 can still be reassigned because Python has no true "const"
#      keyword. ALL_CAPS is only a NAMING CONVENTION that signals intent to
#      other developers -- it is not enforced by the language.
PI = 3.14
PI = 3.14159  # still works, Python won't stop you
print("Q318:", PI)

# 319. Small integers (-5 to 256) are cached by CPython, so a and b point to
#      the SAME cached object -> same id.
a319, b319 = 5, 5
print("Q319:", id(a319) == id(b319))  # True

# 320. 257 is outside the guaranteed small-int cache range. In a script,
#      Python may still fold identical literals in the same code block
#      (True); in the interactive IDLE shell, each line is compiled
#      separately, so it's often False. Behavior is implementation detail.
a320, b320 = 257, 257
print("Q320:", a320 is b320, "(implementation-dependent; don't rely on 'is' for value comparison)")

# 321.
p, q, r = 1, 2, 3
del p, q, r
print("Q321: p, q, r deleted")

# 322. Use dir() (names only) or globals() (name->value dict) to list variables.
sample_var = 1
print("Q322 sample:", [n for n in dir() if not n.startswith("_")][:5])

# 323. Shadowing a built-in: naming a variable 'str' hides the built-in str() function.
str_backup = str  # save the real builtin first (safety, not required by the question)
str = "hello"
try:
    print(str(10))
except TypeError as e:
    print("Q323: TypeError ->", e, "(str is now a string, not the built-in function anymore)")
str = str_backup  # restore it

# 324. Dangerous because any later code in that scope that expects str() to be
#      the built-in function will crash unexpectedly -- hard-to-find bugs.

# 325.
x325 = [1, 2, 3]
y_ref = x325          # SAME object as x325
y_copy = x325.copy()  # INDEPENDENT copy
y_ref.append(4)
print("Q325 reference:", x325)   # changed: [1, 2, 3, 4]
y_copy.append(99)
print("Q325 copy:", x325)        # unaffected: [1, 2, 3, 4]

# 326.
balance = 1000
for _ in range(3):
    balance -= 100
print("Q326:", balance)  # 700

# 327. Dynamic variable creation via globals() dict manipulation:
globals()['x' + str(1)] = 10
print("Q327:", x1)  # 10

# 328. Avoid dynamic variable names: they make code hard to read, hard to
#      debug, and break tools like linters/autocomplete. Use a dict instead,
#      e.g. data = {"x1": 10}.

# 329.
a329, b329, c329 = 1, 2, 3
a329, b329, c329 = b329, c329, a329
print("Q329:", a329, b329, c329)  # 2 3 1

# 330. True behaves like 1 in arithmetic (bool is a subclass of int).
x330 = True
x330 = x330 + 5
print("Q330:", x330)  # 6

# 331.
data = None
if data is None:
    print("Q331: data has not been assigned yet")
data = 5
if data is not None:
    print("Q331: data is now assigned:", data)

# 332.
num1, num2 = 15, 4
total_sum = num1 + num2
difference = num1 - num2
product = num1 * num2
print("Q332:", total_sum, difference, product)

# 333. Stack: fast, small memory for function calls and simple local variable
#      references. Heap: larger memory pool where actual objects (lists,
#      dicts, custom objects) live; variables on the stack just hold
#      references pointing into the heap. (Simplified: Python manages this
#      automatically, unlike C.)

# 334.
name334 = " noun "
clean_name = name334.strip().capitalize()
print("Q334:", repr(clean_name))  # 'Noun'

# 335.
my_name = "ADA"
letters = [ch for ch in my_name]  # one variable per letter, via list here
joined = "".join(letters)
print("Q335:", letters, "->", joined)

"""
SECTION E2: DATA TYPES - DEEP DIVE (336-390) - Answered
Run: python section_e2_datatypes.py
"""

import sys
import copy
import json
import math

print("=== 336-390 ===")

print("Q336:", type([]), type(()), type({}), type(set()))

# 337. {} is always an empty DICT (dict literal syntax came first in Python's
#      design). To make an empty SET you must use set().
print("Q337:", type({}), "-> use set() for an empty set:", set())

print("Q338:", bool(0), bool(0.0), bool(0j), bool(""), bool([]), bool({}), bool(None))
# All False

# 339. 7 falsy values: False, None, 0, 0.0, "", [], {} (also (), set(), 0j)
print("Q339:", [False, None, 0, 0.0, "", [], {}])

# 340. Surprising truthy values: "False" (non-empty string), " " (space string),
#      [0] (non-empty list, even though it holds a falsy item)
print("Q340:", bool("False"), bool(" "), bool([0]))

print("Q341:", repr("hello" * 0), repr("hello" * -5))
# "" for both -- 0 or negative repeat count gives an empty string

lst_mult = [1, 2]
try:
    lst_mult * 2.5
except TypeError as e:
    print("Q342: TypeError ->", e, "(can only multiply a list by an int)")

print("Q343:", "Python"[::-1], "-> reverses the string using a step of -1")

s344 = "Python Programming"
print("Q344:", s344[:3], s344[-3:])  # 'Pyt' 'ing'

print("Q345:", ord('A'), chr(65))  # 65 A

def is_palindrome(text):
    return text == text[::-1]
print("Q346:", is_palindrome("madam"), is_palindrome("hello"))

print("Q347:", repr("  hi  ".strip()), repr("  hi  ".lstrip()), repr("  hi  ".rstrip()))

print("Q348 split:", "a,b,c".split(","))
print("Q348 join:", "-".join("a,b,c".split(",")))

sentence349 = "I love Java"
sentence349 = sentence349.replace("Java", "Python")
print("Q349:", sentence349)

s350 = "hello"
id_before = id(s350)
s350 += "!"
id_after = id(s350)
print("Q350:", id_before == id_after, "-> False, strings are immutable so += creates a NEW string object")

# 351. append([4,5]) adds the LIST ITSELF as one single element.
#      extend([4,5]) adds each ELEMENT of the list individually.
a351 = [1, 2, 3]
a351.append([4, 5])
print("Q351 append:", a351)  # [1, 2, 3, [4, 5]]
b351 = [1, 2, 3]
b351.extend([4, 5])
print("Q351 extend:", b351)  # [1, 2, 3, 4, 5]

# 352. append() modifies the list IN PLACE and returns None (no new value to return).
a352 = [1, 2, 3]
result_352 = a352.append(4)
print("Q352:", result_352, "->", a352)  # None -> [1, 2, 3, 4]

# 353. Insert at the beginning with insert(0, item)
a353 = [2, 3]
a353.insert(0, 1)
print("Q353:", a353)

# 354. remove(value) deletes the FIRST matching value; pop(index) deletes by
#      position (and returns the removed item); pop() with no index removes the last.
a354 = [1, 2, 3, 2]
a354.remove(2)   # removes first '2'
print("Q354 remove:", a354)
popped = a354.pop(0)  # removes item at index 0
print("Q354 pop:", popped, a354)

a355 = [1, 2, 3]
a355.pop()     # removes last item (3)
a355.pop(0)    # removes first item (1)
print("Q355:", a355)  # [2]

# 356. Yes -- the tuple itself is immutable (you can't replace its elements),
#      but if an element is a MUTABLE object (like a list), that object can
#      still be changed in place.
t356 = ([1, 2], 3)
t356[0].append(99)
print("Q356/357:", t356, "-> no error, because we mutated the LIST inside, not the tuple itself")

# 358. No, (5) is just an int in parentheses, NOT a tuple.
print("Q358:", type((5)))  # <class 'int'>

# 359. Add a trailing comma to make it a real single-element tuple
single_tuple = (5,)
print("Q359:", type(single_tuple), single_tuple)

# 360. Sets can only hold HASHABLE (immutable) items. Lists are unhashable -> error.
#      Tuples are hashable, so they CAN go inside a set.
try:
    bad_set = {[1, 2]}
except TypeError as e:
    print("Q360a: TypeError ->", e)
good_set = {(1, 2)}
print("Q360b:", good_set)

# 361. Hashable = has a fixed hash value that never changes during its lifetime
#      (required for dict keys / set members). Lists are mutable, so their
#      contents (and thus hash) could change -- Python disallows this to
#      prevent broken lookups.

# 362. Yes. True == 1 and False == 0 in Python, so they collide as dict keys.
d362 = {True: "yes", 1: "no", 1.0: "maybe"}
print("Q362:", d362, "-> only ONE key remains (True/1/1.0 are all treated as equal keys)")

d363 = {"a": 1}
try:
    d363["b"]
except KeyError as e:
    print("Q363 direct access: KeyError ->", e)
print("Q363 .get():", d363.get("b"))          # None, no error
print("Q363 .get(default):", d363.get("b", 0))  # 0

d1, d2 = {"a": 1}, {"b": 2}
merged = d1 | d2   # Python 3.9+ merge operator
print("Q364:", merged)

d365 = {"a": 1, "b": 2}
print("Q365:", type(d365.keys()), type(d365.values()), type(d365.items()))
# dict_keys, dict_values, dict_items (view objects, not lists)

nums_str = "123,456,789"
nums_int = [int(n) for n in nums_str.split(",")]
print("Q366:", nums_int)

nums_list = [1, 2, 3]
joined_str = "-".join(str(n) for n in nums_list)
print("Q367:", joined_str)

mapped = list(map(int, ["1", "2", "3"]))
print("Q368:", mapped, type(mapped))  # [1, 2, 3] <class 'list'>

mixed369 = [1, "a", 2.5, True, None, [1]]
for item in mixed369:
    print("Q369:", item, "->", type(item).__name__)

print("Q370:", isinstance(True, int), "-> True, because bool is defined as a SUBCLASS of int in Python")

# 371. isinstance() correctly accounts for subclasses/inheritance;
#      type() == checks the EXACT type only. isinstance() is generally preferred.
class MyInt(int):
    pass
mi = MyInt(5)
print("Q371:", isinstance(mi, int), type(mi) == int)  # True False

def convert_if_digit(value):
    return int(value) if value.isdigit() else value
print("Q372:", convert_if_digit("42"), convert_if_digit("abc"))

data373 = {"students": [{"name": "Max", "scores": [90, 80]}]}
print("Q373:", data373["students"][0]["scores"][1])  # 80

nested374 = [[1, 2], [3, 4]]
shallow374 = nested374.copy()
deep374 = copy.deepcopy(nested374)
shallow374[0].append(99)   # affects nested374 (shared inner list)
print("Q374:", nested374, deep374)

a375 = float("nan")
print("Q375:", a375 == a375, "-> False, NaN is defined to never equal anything, even itself")

print("Q376:", math.isnan(float("nan")), "-> use math.isnan() to check for NaN")

# 377. None = absence of a value; 0 = the number zero; "" = empty string;
#      False = boolean false. They are all FALSY but NOT the same as each other or equal via 'is'.
print("Q377:", None == 0, 0 == "", "" == False, "-> all False, they are different types/values")

lst378 = [1, 1, 2, 2, 3, 3]
no_dup_set = list(set(lst378))
print("Q378:", no_dup_set, "-> order is NOT guaranteed with a plain set")

no_dup_ordered = list(dict.fromkeys(lst378))
print("Q379:", no_dup_ordered, "-> dict.fromkeys() preserves insertion order (Python 3.7+)")

print("Q380:", len([[]]), len([]))  # 1 0 -- [[]] has ONE item (an empty list)

print("Q381:", b"hello", type(b"hello"), "-> byte strings represent raw binary data, used in file I/O, networking, encoding")

sentence382 = "I have 5 apples and 3.5 kg of rice"
counts = {"int": 0, "float": 0, "string": 0}
for word in sentence382.split():
    if word.replace(".", "", 1).isdigit():
        if "." in word:
            counts["float"] += 1
        else:
            counts["int"] += 1
    else:
        counts["string"] += 1
print("Q382:", counts)

print("Q383:", sys.getsizeof(10), sys.getsizeof("hello"), sys.getsizeof([1, 2, 3]))

x384 = 10
print("Q384: type=", type(x384), "id=", id(x384), "value=", x384, "size=", sys.getsizeof(x384))

def check_mutability(value):
    try:
        value[0] = value[0]  # attempt an in-place item change
        return "mutable"
    except (TypeError, IndexError):
        return "immutable"
print("Q385:", check_mutability([1, 2]), check_mutability((1, 2)))

a386 = "python"
print("Q386:", a386 is "python", "-> works here due to string interning, but 'is' should NOT be used for string comparison; use =='")

# 387. String interning: Python may reuse the SAME memory object for identical
#      short strings/simple literals to save memory -- an implementation detail, not a guarantee.

student388 = {
    "name": "Ada",
    "age": 20,
    "courses": ["Math", "Physics"],
    "grades": {"Math": "A", "Physics": "B"}
}
print("Q388:", student388)

student_json = json.dumps(student388)  # module: json
print("Q389:", student_json)

def data_type_report(value):
    print("Q390 value:", value)
    print("Q390 type:", type(value))
    print("Q390 id:", id(value))
    print("Q390 bool:", bool(value))
    print("Q390 mutable:", check_mutability(value) if isinstance(value, (list, tuple)) else "n/a")
data_type_report([1, 2, 3])

# 391. BODMAS: 5 + (2*3) * (2/2) - 1  =>  5 + 6*1 - 1 = 5 + 6 - 1 = 10
print("Q391:", 5 + 2 * 3 * 2 / 2 - 1)  # 10.0

print("Q392:", 100 / 10 / 2, "-> evaluated LEFT to right: (100/10)/2 = 10/2 = 5.0")
print("Q393:", 100 // 10 // 2, "-> (100//10)//2 = 10//2 = 5")

print("Q394:", 2 * 3 * 2, (2 * 3) * 2, "-> identical: 12 12 (multiplication is left-associative anyway)")

principal, rate, years = 1000, 5, 2
compound_interest = principal * (1 + rate / 100) ** years - principal
print("Q395:", round(compound_interest, 2))

print("Q396:", -10 / 3, -10 // 3, "-> '/' gives -3.333..., '// ' floors DOWN (towards negative infinity) to -4, not -3")

print("Q397:", 10 % -3, -10 % 3, "-> Python's % result always takes the SIGN of the divisor, unlike some other languages")

print("Q398:", divmod(10, 3), "-> (quotient, remainder), same as (10//3, 10%3)")

n399 = 1234
digits = []
temp = n399
while temp > 0:
    digits.insert(0, temp % 10)
    temp //= 10
print("Q399:", digits)

# 400. Floats are stored in binary, and most decimal fractions (like 0.1)
#      cannot be represented exactly in binary -> tiny rounding errors occur.
print("Q400:", 0.1 + 0.2 == 0.3, 0.1 + 0.2)


