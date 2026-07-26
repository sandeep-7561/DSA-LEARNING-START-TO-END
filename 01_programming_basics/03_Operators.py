#-----------Arithmetic Operators---------------
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

#---------Comparison (Relational) Operators---------
a = 10
b = 5

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

#------------Assignment Operators--------------
a = 10

a += 5
print(a)

a *= 2
print(a)

#-------------Logical Operators---------------
age = 20
salary = 50000

print(age > 18 and salary > 30000)
print(age > 18 or salary > 100000)
print(not(age > 18))


#---------------Bitwise Operators--------------
a = 5
b = 3

print(a & b)
print(a | b)

#----------------Membership Operators-----------------
fruits = ["Apple", "Banana", "Mango"]

print("Apple" in fruits)
print("Orange" in fruits)
print("Orange" not in fruits)

#---------------Identity Operators--------------------
a = [1, 2]
b = a
c = [1, 2]

print(a is b)
print(a is c)
print(a == c)


print(16>>2)