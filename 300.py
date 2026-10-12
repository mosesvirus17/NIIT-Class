import math
import os

Name = "Moses"
print("Q1",Name)

Age= 19
Birth_year= 2007
print("Q2",Age,Birth_year)

a,b = 2,6
a,b = b,a
print("Q3",a,b)

l1 = [1, 2, 3];
l2 = l1; 
l2.append(4);
print("Q4",l1, l2)

x = y = z = 0
print("Q5",x,y,z)

v = 10; 
print(type(v)); 
v = str(v); 
print(type(v)); 
v = list(v); 
print("Q6",v, type(v))

Number = 1_000_000
print("Q7",Number)

n = None
print("Q8",n is None)

f1, f2, f3, f4, f5 = ["Apple", "Banana", "Cherry", "Date", "Fig"]
print("Q9",f1, f2, f3, f4, f5)  

first, *_, last = (1, 2, 3, 4, 5); print("Q10",first, last)
first, *middle, last = (1, 2, 3, 4, 5); print("Q10",first, middle, last)

PI = 5.14159       
PI = 5
print("Q11",PI)

counter = 5
def inc():
    global counter
    counter += 1
inc()
print("Q12",counter)

def make_local():
    local_var = 5
make_local()
try: print(local_var)
except NameError as e: print("Q13 Error:", e)

x = int("256"); y = int("256"); print("Q14",x is y)      # True
x = int("1000"); y = int("1000"); print("Q14",x is y)    # False

a = []; b = []; a.append(1); print("Q15",a, b)   # b unaffected: Noryhing in the b

if (n := len("hello")) > 3: print("Q16",n, "is greater than 3")

text = "19"
num = int(text); print("Q17",num + 1)

Car = True
print("Q18",Car + 5)

N = 7.99
print("Q19",int(N))

Length, Width = 5, 3
area = Length * Width
print("Q20",area) 

full_name = "John Smith"; 
first_name = full_name[:full_name.index(" ")];
print("Q21",first_name)

Fan = 9
del Fan
print("Q22","Fan")

a,b = 1, 2
c = a + b
print("Q23", c)

orig = [1, 2, 3];
cp = orig.copy(); 
cp.append(4); 
print("Q24",orig, cp)

celsius = 100; 
fahrenheit = celsius * 9 / 5 + 32; 
print("Q25",fahrenheit)

price = 200
discount_price = price * 0.9
print("Q26", discount_price)

s = "100"
print("Q27",int(s) + 1)

x, y = 10, 0; z = x / y if y != 0 else None; print("Q28",z)

sentence = "Python is fun"; length_of = len(sentence); print("Q29",length_of)

age = 20; is_adult = age >= 18; print("Q30",is_adult)

first_name, last_name = "Chukwuemeka", "Moses"
full = first_name + " " + last_name
print("Q31",full)

special = "Tab\tHere \"Single\" '\Married' \\ Taken"
print("Q32",special)

Name = """Moses 1
Saka 2
Mp 3"""
print("Q33",Name)

result = 10 > 5
print("Q34",result)

lst = [10, 20, 30]; 
first_el = lst[0]; 
print("Q35",first_el)

d = {"name": "Ada", "age": 30}; 
nm = d["name"]; 
print("Q36",nm)

st = {1, 2}; 
st.add(3); 
print("Q37",st)

t = (1, 2, 3)
try: t[0] = 99
except TypeError as e: print("Q38","Error:", e)

M = 4.5 
print("Q39",type(M))

c = 3 + 4j; 
print("Q40",c, c.real, c.imag, abs(c))

height_m = 1.75
height_cm = height_m * 100
print("41",height_cm)

seconds = 7265
minutes = seconds / 60
hours = seconds / 3600
print("Q42",minutes, hours)

word = "hello"
upper_word = word.upper()
print("Q43",upper_word)

money = 90
with_tax = money * 2.07
print("Q44", with_tax)

age = "30"
age_in_5 = int(age) + 5
print("Q45",age_in_5)

nested = [[1, 2], [3, 4]]; 
print("Q46",nested[1][0])

pi = 3.14
r = 5
print("Q47",pi * r ** 2)

base, exponent = 8, 10
print("Q48",base ** exponent)

name = "Moses"
lower_name = name.lower()
print("Q49",lower_name) 

d = {}
d["key"] = "value"
print("Q50",d)

x = 5
for _ in range(3): x = x + 1
print("Q51",x)

score = 40 
doubled_score = score * 2
print("Q52",doubled_score)

country = "Canada"
country_code = "CA"
print("Q53",country,country_code)

binary = "1010"
print("Q54",int(binary, 2))

decimal = 10
print("Q55",bin(decimal), format(decimal, "b"))

n1, n2 = 10, 20
avg = (n1 + n2) / 2;
print("Q56",avg)

first_name = "Moses"
initial = first_name[0]
print("Q57",initial)

sentence = "My Name is Moses"
word_count = len(sentence.split())
print("Q58",word_count)

nums = [1, 2, 3]; 
rev = nums[::-1]; 
print("Q59",rev)

d = {"a": 1, "b": 2}
key = list(d.keys())
print("Q60",key)

print(5 + 3)
try: print("5" + 3)
except TypeError as e: print("Q61","Error:", e)

a1, a2 = 30, 35 
print("Q62",a1 - a2)

print("Q63","hi" * 3)

print("Q64",10 / 3, 10 // 3)

print("Q65",25 % 4)

print("Q66",2 ** 10)

x = 10
x += 5
print("67",x)

x = 20
x -= 5
print("Q68",x)
x*= 2
print("Q68",x)
x /= 3
print("Q68",x)

print("Q69", 25 == 25)

print("Q70", 25 !=30)

print("Q71", 5 > 3, 5 < 3)

x = 10; print("Q72", 5 < x < 15)

a = [1, 2]; b = [1, 2]; print("Q73",a == b, a is b)  # equal values, different objects

age = 20; has_id = True; print("Q74",age > 18 and has_id)

is_student, is_teacher = False, True; print("Q75",is_student or is_teacher)

raining = False; print("Q76",not raining)

print("Q77","a" in "apple")

d = {"name": "Ada"}; print("Q78","name" in d)

print("Q79", 10 & 12, 10 | 12, 10 ^ 12)  # 8, 14, 6

print("Q80",8 << 1, 8 << 2, 8 >> 1, 8 >> 2)  # 16, 32, 4, 2

print("Q81",~5)  # -6  (~n == -n-1)

print("Q82",2 + 3 * 4 ** 2)  # ** first (16), then * (48), then + => 50

n = 12; print("Q85",n % 3 == 0)

print("Q84",-11 // 3)  # -4 (floors toward -infinity)

print("85",-11 % 3)   # 1  (result takes the sign of the divisor)

a, b, c, d, e = 1, 2, 3, 4, 5; print("Q86",(a + b) * c / d - e)

print("Q87",0 or "hi", "hi" and [], 0 and "x", "" or [] or "last")

x = None; print("Q88",x is None, x is not None)

print("Q89","z" not in "apple")

print("Q90",(6 * 7) % 5)

x = 17; x //= 3; print(x); x %= 3; print("Q91",x)

P, r, n, t = 1000, 0.05, 12, 5; A = P * (1 + r / n) ** (n * t); print("Q92",round(A, 2))

print("Q93","apple" < "banana", "Zebra" < "apple")  # compares by Unicode code points

print("Q94",[1, 2] + [3, 4], [0] * 3)

print("Q95","ell" in "hello")

age = 30; print("Q96",18 <= age <= 60, age >= 18 and age <= 60)

print("Q97",4 if 4 > 9 else 9)

print("Q98",70 / 1.75 ** 2)

print("Q99",135 // 60, "h", 135 % 60, "min")

print("Q100",8 & 1 == 0)  # True if even

print("Q101",3 * 9.99 )

year = 2010; print("Q102",2000 <= year <= 2025)

print("Q103",bool("ada") and bool("pw"))

print("Q104",1234 % 10)

print("Q105",472 // 100)

n = 45; print((n % 10) * 10 + n // 10)                    # 2 digits -> 54
n = 123; print("Q106",(n % 10) * 100 + (n // 10 % 10) * 10 + n // 100)  # reverse 3 digits -> 321

a, b, c = 4, 5, 9; print("Q107",(a + b + c) / 3)

a, b, c = 3, 4, 5; print("Q108",a + b > c)

a, b = 7, 3; print("Q109",(a > b) * a + (a <= b) * b)

P, R, T = 1000, 5, 2; print("Q110", P * R * T / 100)

a, b = 105, 100; print("Q111",abs(a - b) <= 0.10 * b)

speed, time = 60, 2.5; print("Q112",speed * time)

c = 37; print("Q113", c * 9 / 5 + 32)

b, h = 10, 5; print("Q114",0.5 * b * h)

cp, sp = 500, 650; r = sp - cp; print("Q115",f"Profit {r}" if r > 0 else f"Loss {-r}" if r < 0 else "No profit no loss")

s = "banana"; print("Q117",len(s) > 5 and "a" in s)

print("Q118",divmod(17, 5))

print("Q118",True + False * True)  # 1 + (0*1) = 1

print("Q119",0 == False, 1 == True)

print("Q120",[] == False, bool([]))  # False False: empty list is falsy but not equal to False

print("Q121",(10 / 3) * 3, (10 // 3) * 3)  # 10.0 vs 9

n = 8; print("Q122",n > 0 and n % 2 == 0)

price = 1500; print("Q123",price * 0.9 if price > 1000 else price)

age = 25; print("Q124", not (13 <= age <= 19))

s1, s2 = "Hello", "World"; r = s1 + s2; print("Q125",r, len(s1) > len(s2), len(r))

a, b = 3, 7; print("126",a % 2 == 1 and b % 2 == 1)

price, tax = 200, 7.5; print("Q127",price + price * tax / 100)

a, b = 20, 5; print("Q128",a % b == 0)

n = 3; print("Q129",abs(n ** 2 - n ** 3))

a, b, c, d = 1, 0, 1, 1; print("Q130",(a and b) or (c and d))

ch = "G"; print("131","A" <= ch <= "Z")

n = -5
if n > 0: print("Positive")
elif n < 0: print("Negative")
else: print("Q134","Zero")

age = 20; print("Q133","Eligible to vote" if age >= 18 else "Not eligible")

n = 7; print("Q134","Even" if n % 2 == 0 else "Odd")

y = 2024; print("Q135","Leap" if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0 else "Not leap")

pw = ""
if pw == "": print("Q136","Password cannot be empty")
elif pw == "secret": print("Q136","Correct")
else: print("Q136","Wrong password")

lst = [1, 2, 3]
if not lst: print("Q137","Empty")
else: print("Q137","Length:", len(lst))

s = ""; print("Q138", "Empty string" if not s else "Not empty")

a, b = 4, 9
if a > b: print("Q139", a, "is greater")
elif b > a: print("Q139", b, "is greater")
else: print("Q139","Equal")

marks = 65
if marks > 70: print("Q140","A")
elif marks > 60: print("Q140","B")
elif marks > 50: print("Q140","C")
else: print("Q140","Fail")

ch = "7"
if ch.isdigit(): print("Q141","Digit")
elif ch.isalpha(): print("Q141","Alphabet")
else: print("Q141","Special character")

age = 65
if age >= 18:
    if age > 60: print("Q142","Senior citizen")
    else: print("Q142","Adult")
else: print("Q142","Minor")

light = "yellow"
if light == "red": print("Q143","Stop")
elif light == "yellow": print("Q143","Get ready")
elif light == "green": print("Q143","Go")
else: print("Q143","Invalid")

n = 30; print("Q144", "Divisible by both 3 and 5" if n % 3 == 0 and n % 5 == 0 else "Not divisible by both 3 and 5")

age = 17; print("Q145","Adult" if age >= 18 else "Q145","Minor")

age = 15; print("Q146","Child" if age < 13 else "Q146","Teen" if age < 20 else "Q146","Adult")

zero, nothing, false = 0, None, False
print("Q147",nothing == false, nothing is false)  # False False -> None is not False
print("Q147",zero == false, zero is false)        # True False  -> equal in value, different objects
print("Q147",nothing is None, zero is None)       # True False

is_member, price = False, 1500
print("Q148","Discount applied" if is_member or price > 1000 else "Q148","No discount")

ch = "e"
if ch.isalpha(): print("Q149","Vowel" if ch.lower() in "aeiou" else "Consonant")
else: print("Q149","Not a letter")

u, p = "admin", "1234"
print("Q150","Login success" if u == "admin" and p == "1234" else "Invalid credentials")

n = 15
if 1 <= n <= 10: print("Q151","1-10")
elif 11 <= n <= 20: print("Q151","11-20")
elif 21 <= n <= 30: print("Q151","21-30")
else: print("Q151","Out of range")

a, b, c = 3, 4, 5
print("Q152","Valid triangle" if a + b > c and a + c > b and b + c > a else "Invalid")

a, b, c = 5, 5, 3
if a == b == c: print("Q153","Equilateral")
elif a == b or b == c or a == c: print("Q153","Isosceles")
else: print("Q153","Scalene")

age, has_license = 20, True; print("Q154","Can drive" if age >= 18 and has_license else "Cannot drive")

n = 456; print("Q155",len(str(abs(n))) == 3)

s = "Hello"; print("Q156",s[0].isupper() if s else False)

lst = [1, 2, 3]; print("Q157",2 in lst)

a, b = "Listen", "Silent"; print("Q158",sorted(a.lower()) == sorted(b.lower()))

y = 1900
if y % 100 == 0: print("Q159","Century, leap" if y % 400 == 0 else "Century, not leap")
else: print("Q159","Not a century year")

n = 29
if n < 2: print("Q160","Not prime")
else:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: print("Q160","Not prime"); break
    else: print("Q160","Prime")

s = "madam"; print("Q161","Palindrome" if s == s[::-1] else "Q161","Not palindrome")

t = 35; print("Q162","Cold" if t < 15 else "Q162","Hot" if t > 30 else "Q162","Normal")

marks = {"math": 45, "sci": 60, "eng": 50}; print("Q163","Pass" if all(m >= 40 for m in marks.values()) else "Q163","Fail")

age, dress_ok = 22, True; print("Q164","Entry allowed" if age >= 21 and dress_ok else "Q164","Denied")

n = 9; print("Q165", (n % 2 == 0) ^ (n % 3 == 0))  # True: divisible by exactly one

ch = "#"
if ch.isupper(): print("Q166","Uppercase")
elif ch.islower(): print("Q166","Lowercase")
elif ch.isdigit(): print("Q166","Digit")
else: print("Q166","Special")

hour = 14
if 5 <= hour < 12: print("Q167","Morning")
elif 12 <= hour < 17: print("Q167","Afternoon")
elif 17 <= hour < 21: print("Q167","Evening")
else: print("Q167","Night")

is_student, is_senior = False, True; 
print("Q168","Discount" if is_student or is_senior else "Full price")

pw = "abc12345!"
print("169",len(pw) > 8 and any(c.isdigit() for c in pw) and any(not c.isalnum() for c in pw))

n = 1950; 
print("Q170",abs(n - 1000) <= 100 or abs(n - 2000) <= 100)

e = "a@b.com"; print("171","@" in e and "." in e)
age = 15; print("Q172",13 <= age <= 19)

v = 3.5; 
print("Q173","Integer or float" if isinstance(v, (int, float)) else "Neither")

lst = [1, 2, 2, 3];
print("Q174","Has duplicates" if len(lst) != len(set(lst)) else "No duplicates")

print("Q175","12345".isdigit(), "12a".isdigit())

print("Q176","hello".isalpha(), "he11o".isalpha())

f = "photo.jpg"
if f.endswith(".py"): print("Q177","Python file")
elif f.endswith(".txt"): print("Q177","Text file")
elif f.endswith(".jpg"): print("Q177","Image file")
else: print("Q177","Unknown")

n = 49; 
print("Q178","math.isqrt(n) ** 2 == n")

m = 2
if m in (4, 6, 9, 11): print("Q179",30)
elif m == 2: print("Q179","28 (29 in leap year)")
else: print("Q179",31)

salary, score = 60000, 720; 
print("Q180","Eligible" if salary >= 30000 and score >= 650 else "Not eligible")

n = 153; s = str(n); print("Q181",n == sum(int(d) ** len(s) for d in s))

a, b = 123, 453; print("Q182",a % 10 == b % 10)

s = "   "; print("Q183","Empty or whitespace" if s.strip() == "" else "Q183","Has content")

age = 70
if age < 12: print("Q184","Child ticket: 5")
elif age < 60: print("Q184","Adult ticket: 10")
else: print("Q184","Senior ticket: 7")

n = 9
if n > 0:
    if n ** 2 < 100: print("Q185","Positive and square < 100")

ans = "Y"; print("Q186","Yes" if ans.lower() in ["yes", "y"] else "No")

lst = [1, 2, 3]; print("Q187",lst == sorted(lst))

d = {}; print("Q188","Empty dict" if not d else "Q188","Not empty")

s = "python"; print("Q189","Even length" if len(s) % 2 == 0 else "Q189","Odd length")

n = 77; print("Q190",n % 7 == 0 and n % 10 == 7)

h = 130; print("Q191","Allowed" if h >= 120 else "Q191","Too short")

s = "HelloWorld"; print("Q192",any(c.isupper() for c in s) and any(c.islower() for c in s))

n = 24; print("Q193",n % 4 == 0 and n % 6 == 0)

grade, attendance = 70, 80; print("Q194","Promoted" if grade >= 40 and attendance >= 75 else "Q194","Not promoted")

n = 6
if n == 0: print("Q195","Zero")
else:
    if n % 2 == 0: print("Q195","Even")
    else: print("Q195","Odd")

m = 7
if m in (12, 1, 2): print("Q196","Winter")
elif m in (3, 4, 5): print("Q196","Spring")
elif m in (6, 7, 8): print("Q196","Summer")
elif m in (9, 10, 11): print("Q196","Autumn")
else: print("Q196","Invalid month")

u = "adaLove"; print("Q197",5 <= len(u) <= 15)

n = 42; n = abs(n); print("Q198","Single" if n < 10 else "Double" if n < 100 else "Triple" if n < 1000 else "More")

s = "Madam"; print("Q199",s.lower() == s.lower()[::-1])

a, b = -3, -7; print("Q200",(a > 0 and b > 0) or (a < 0 and b < 0))

print("Q201","Hello World".istitle(), "hello World".istitle())

def hello():
 print("Q202","Hello, World!")
hello()

def greet(name): 
 print(f"Q203","Hello, {name}!")
greet("Ada")

def add(a, b):
 return a + b
print("Q204",add(2, 3))

def welcome(name="Guest"):
 print("Q205","Welcome,", name)
welcome(); welcome("Ada")

def rect(l, w): 
 return l * w, 2 * (l + w)
area, perimeter = rect(4, 5); print("Q206",area, perimeter)

def total(*args):
 return sum(args)
print("Q207",total(1, 2, 3, 4, 5))

def show(**kwargs):
    for k, v in kwargs.items(): 
        print("Q208",k, "=", v)
show(name="Ada", age=30)

def bad(item, lst=[]):          # BUG: the default list is created once and shared
    lst.append(item); return lst
print("Q209",bad(1), bad(2))           # [1] then [1, 2]
def good(item, lst=None):
    if lst is None: lst = []
    lst.append(item); return lst
print("Q209",good(1), good(2))         # [1] [2]

count = 0
def increment():
    global count
    count += 1
increment(); increment()
print("Q210",count)

def outer():
    x = 0
    def inner():
        nonlocal x
        x += 1
        return x
    inner(); return inner()
print("Q211",outer())

def fact(n): return 1 if n <= 1 else n * fact(n - 1)
print("Q212",fact(5))

add_l = lambda a, b: a + b; print("Q213",add_l(2, 3))

def make_multiplier(n):
    def multiply(x): return x * n   # closure remembers n
    return multiply
double = make_multiplier(2);
print("Q214",double(7))

def change(num, lst):
    num += 10        # rebinds local only: immutable int unchanged outside
    lst.append(99)   # mutates the shared list
n, l = 5, [1]; change(n, l); 
print("Q215",n, l)  # 5 [1, 99]


def is_prime(n):
    if n < 2: return False
    return all(n % i for i in range(2, int(n**0.5) + 1))
print("Q216",is_prime(7), is_prime(10))

def apply(func, x): return func(x)
print("Q217",apply(str.upper, "hi"), apply(lambda v: v * v, 5))

def check(n):
    if n < 0: return "Negative, exiting early"
    return "Non-negative"
print("Q218",check(-1), check(3))

x = 100
def shadow(x): 
 return x + 1   # parameter x shadows the global x
print("Q219",shadow(5), x)

def long_enough(s):
    if (n := len(s)) > 3:
     return f"{s} has {n} chars"
    return "short"
print("Q220",long_enough("python"))

def countdown(n):
    print("Q221",n)
    if n > 0: countdown(n - 1)
countdown(5)

def palindrome(s): s = s.lower(); return s == s[::-1]
print("Q222",palindrome("Madam"))

def max3(a, b, c): 
 return max(a, b, c)
print("Q223",max3(3, 9, 5))

def simple_interest(p, t, r=5): return p * r * t / 100
print("Q224",simple_interest(1000, 2), simple_interest(1000, 2, 8))

def c_to_f(c): return c * 9 / 5 + 32
print("Q225",c_to_f(100))

def count_vowels(s): return sum(ch in "aeiou" for ch in s.lower())
print("Q226",count_vowels("Programming"))

def reverse(s): return s[::-1]
print("Q227",reverse("hello"))

def is_leap(y): return (y % 4 == 0 and y % 100 != 0) or y % 400 == 0
print("Q228",is_leap(2024), is_leap(1900))

def fact_loop(n):
    r = 1
    for i in range(2, n + 1): r *= i
    return r
print("Q229",fact_loop(6))

def fib_upto(n):
    a, b, out = 0, 1, []
    while a <= n:
        out.append(a); a, b = b, a + b
    return out
print("Q230",fib_upto(50))

def digit_sum(n): return sum(int(d) for d in str(abs(n)))
print("Q231",digit_sum(1234))

def armstrong(n): s = str(n); return n == sum(int(d) ** len(s) for d in s)
print("Q232",armstrong(153), armstrong(123))

def power(base, exp):
    r = 1
    for _ in range(exp): r *= base
    return r
print("Q233",power(2, 10))

def largest(lst):
    m = lst[0]
    for v in lst:
        if v > m: m = v
    return m
print("Q234",largest([3, 9, 2, 7]))

def remove_dups(lst):
   return list(dict.fromkeys(lst))  # keeps order
print("Q235",remove_dups([1, 2, 2, 3, 1]))

def remove_dups(lst): return list(dict.fromkeys(lst))  # keeps order
print("Q235",remove_dups([1, 2, 2, 3, 1]))

def merge(a, b): return a + b
print("Q236",merge([1, 2], [3, 4]))

def anagram(a, b): return sorted(a.lower()) == sorted(b.lower())
print("Q237",anagram("Listen", "Silent"))

def count_words(s): return len(s.split())
print("Q238",count_words("the quick brown fox"))

def cap_words(s): return " ".join(w.capitalize() for w in s.split())
print("Q239",cap_words("hello big world"))

def check_even(n):
    def is_even(x): return x % 2 == 0
    return is_even(n)
print("Q240",check_even(4), check_even(7))

def bmi_category(w, h):
    b = w / h ** 2
    if b < 18.5: return round(b, 1), "Underweight"
    elif b < 25: return round(b, 1), "Normal"
    elif b < 30: return round(b, 1), "Overweight"
    return round(b, 1), "Obese"
print("Q241",bmi_category(70, 1.75))

def valid_email(e): return "@" in e and "." in e
print("Q242",valid_email("a@b.com"), valid_email("abc"))

def table(n):
    for i in range(1, 11): print("Q243",f"{n} x {i} = {n * i}")
table(5)

def gcd(a, b):
    while b: a, b = b, a % b
    return a
print("Q244",gcd(48, 18))

def lcm(a, b):
 return a * b // gcd(a, b)
print("Q245",lcm(4, 6))

def has_digit(s):
 return any(c.isdigit() for c in s)
print("Q246",has_digit("abc1"), has_digit("abc"))

def sum_even(*args): 
 return sum(n for n in args if n % 2 == 0)
print("Q247",sum_even(1, 2, 3, 4, 5, 6))

def greeting(name):
 return "Hello, " + name + "! Welcome."
print("Q248",greeting("Ada"))

def second_largest(lst): 
 return sorted(set(lst))[-2]
print("Q249",second_largest([4, 9, 1, 9, 7]))

def strong_password(p):
    return len(p) >= 8 and any(c.isdigit() for c in p) and any(c.isupper() for c in p) \
        and any(c.islower() for c in p) and any(not c.isalnum() for c in p)
print("Q250",strong_password("Abcdef1!"), strong_password("abc"))

def to_hm(minutes): 
 return str(minutes // 60) + " hr " + str(minutes % 60) + " min"
print("Q251",to_hm(135))

def discount(price):
 return price * 0.9 if price > 1000 else price
print("Q252",discount(1500), discount(500))

def vote(age): 
 return "Eligible to vote" if age >= 18 else "Not eligible to vote"
print("Q253",vote(20), vote(15))

def full_name(first, last):
 return first + " " + last
print("Q254",full_name("Ada", "Lovelace"))

def circle_area(r, pi=math.pi): 
 return pi * r ** 2
print("Q255",circle_area(5), circle_area(5, 3.14))

def person(): 
 return "Ada", 30, "London"
name, age, city = person(); print(name, age, city)

def count_case(s): 
 return sum(c.isupper() for c in s), sum(c.islower() for c in s)
print("Q257",count_case("Hello World"))

def perfect_square(n): 
 return n >= 0 and math.isqrt(n) ** 2 == n
print("Q258",perfect_square(49), perfect_square(50))

def pattern(n):
    for i in range(1, n + 1): print("Q259","*" * i)
pattern(4)

def average(lst): 
 return sum(lst) / len(lst)
print("Q260",average([1, 2, 3, 4]))

def is_sorted(lst): 
 return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))
print("Q261",is_sorted([1, 2, 3]), is_sorted([3, 1, 2]))

first, last = "Ada", "Lovelace"
print("Q262",first + " " + last)

name, age = "Ada", 30; 
print("Q263",name + " is " + str(age))

print("Q264","hey " * 10)

print("Q265",f"{first} {last}")

print("Q266","{} {}".format(first, last))

print("Q267"," ".join(["Python", "is", "fun"]))

print("Q268",f"Number: {n}", "Number: " + str(n))

print("Q269","hello" + "", "" + "world")

val = None
try: print("Q270","Value: " + val)
except TypeError as e: print("Q270","Error:", e)

print("Q271","Value: " + str(val), f"Value: {val}")  # fixes

print("Q271",",".join(map(str, "nums")))

print("Q272","Flag: " + str("flag"), f"Flag: {"flag"}")

print("Q273",f"2+3={2 + 3}")

s = "abc"; print("Q274",s + s[::-1])

print("Q275","hello" "world")  # adjacent literals join automatically

print("Q276","hello".__add__(" world"))

words = ["I", "love", "Python"]
print("Q277"," ".join(words))
sent = ""
for w in words: sent += w + " "
print("Q277",sent.strip())

m = "line one\n" + "line two"
print("Q278",m)

m2 = """a
b""" + """
c"""
print("Q279",m2)
print("Q279","folder" + "/" + "file.txt", os.path.join("folder", "file.txt"))

print("Q280","user" + "@" + "domain")

print("Q281",f"Price: {price:.2f}")

print("Q282",first[0] + last[0])

print("Q283",["item" + str(i) for i in range(3)])

print("Q284","World" in s)

print("Q285","Wow" + "!!!", "Wow" + "!" * 3)

print("Q286","-".join(["a", "b", "c"]))

print("Q287","Line1" + "\n" + "Line2")

print("Q288",(first + last).upper())

print("Q289",r, len(r))

print("Q290",f"{s}{s}")

print("Q291","Hello, " + "user_name" + "!")

print("Q292","Paris" + ", " + "France")

print("Q293",s.replace("morning", "evening"))

print("Q294",s[2:7])

print("Q295",s)

print("Q296","sep.join(items)")

print("Q297",str(a) + str(b), f"{a}{b}")

print("Q298","Col1" + "\t" + "Col2")

print("Q299",n, a)

print("Q300","I am " + "n" + " and I am " + str(a) + " years old")           # +

print("Q300",f"I am {n} and I am {a} years old")                           # f-string

print("Q300","I am {} and I am {} years old".format(n, a))                 # format

print("Q300",c, "c == c[::-1]")  # check palindrome