  # 106. print("Hi" * 3)
 
 
  # 111. list: an ordered, mutable collection -> [1, 2, 3]
  # 112. tuple: an ordered, IMMUTABLE collection -> (1, 2, 3)
  # 113. Difference: lists can be changed after creation; tuples cannot.
 
 
  # 119. a=[1,2]; a[0]=99; print(a)


  # 121. print(type([]))
  # 122. print(type(()))
  # 123. print(type({}))
  # empty_set = ()
  # empty_dict = {}
  # 124. print(empty_set)
  # 125. print(empty_dict)


  # 126. print(type([]), type({}))
  # 127. Indexing = accessing an item in a sequence by its position, e.g. s[0]
  # 128. print(len([1, 2, 3, 4]))
  # 129. print(bool([]), bool([0]))
  # 130. print(bool([""]), bool([" "]))

  # 131. x =5 print(isinstance(x, int))

# 141. print("+, -, /, //, %, *")
# 142. print("+ sum", 10 + 5) 
# 143. print("- subtract", 10 - 5)
# 144. print("_ doc's", 10_5)
# 145. print("/ It returns a float", 10 / 5)
# 146. print("// floor division, drop the remainder", 10 // 2)
# 147. print("% remainder/modulo", 10 % 2)
# 148. print("* multiplication", 2 * 3)
# 149. print(10 / 3)     
# 150. print(10 // 3)
# 151. print(10 % 3)
# 152. print(2 + 3 * 4)
# 153. print(2 * 3 * 2)
# 154. length = 10; width = 5; print(length * width) 
# 155. principal = 2000; rate = 10; time = 5; print(principal * rate * time / 100)
# 156. print("==, !=, >, <, <=, >=")

# 157. print("(==):", 5 == 5)
# 158. print("(!=):", 5 != 3)
# 159. print("(> <):", 5 > 3, 3 < 5)
# 160. print("(>= <=):", 5 >= 5, 5 <= 5)
# 161. print(5 == 5.0)   
# 162. print("5" == 5)   
# 163. print(10 > 5)     
# 164. print(True == 1)  
# 167. print( False == 0) 

# 166. and = True if BOTH are true; or = True if AT LEAST ONE is true; not = flips the boolean
# 167. print(True and False)
# 168. print(True or False)
# 169. print(not True)
# 170. print(5 > 3 and 10 > 5)
# 171. print(5 > 10 or 10 > 5)

# 172. 5 assignment operators: =, +=, -=, *=, /=
# val = 5
# 173. val += 5; print("(+=)", val)
# 174. val -= 3; print("(-=)", val)
# 175. val *= 2; print("(*=)", val)   
# 176. val /= 4; print("(/=)", val)

# 177. x += 1 is the same as x = x + 1
# 178. '=' assigns a fresh value; '+=' adds to the existing value and reassigns.

# 191. Operator chaining lets you combine comparisons; print(1 < 2 < 3)

# 192. print(10 + 20 * 30 / 10)

# 194. n1, n2 = 10, 3; print(n1 + n2, n1 - n2, n1 * n2, n1 / n2, n1 % n2, n1 // n2)

# 195. age_check = 20; print(age_check >= 18)

# 196. number = 15; print(number % 3 == 0 and number % 5 == 0)

# 197. letter = "e"; print(letter in "aeiou")

# 199. BODMAS = Brackets, Orders(powers), Division/Multiplication, Addition/Subtraction.

# 200. Small calculator
# def calculator(a, b):
#     return {
#         "+": a + b,
#         "-": a - b,
#         "*": a * b,
#         "/": a / b if b != 0 else "undefined",
#         "%": a % b if b != 0 else "undefined",
#         "//": a // b if b != 0 else "undefined",
#     }
# print( calculator(10, 3))
