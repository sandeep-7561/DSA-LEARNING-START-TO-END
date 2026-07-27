def greet():
    print("Hello Bro")

greet()

def add(a,b): # -> a and both Parameters
    print(a+b)

add(5,10) # -> 5 and 10 both Arguments


#---------RETURN---------------
def add_num():
    return 10 + 20

x = add_num()

print(x)


#---------Multiple Parameters---------
def add(a, b):
    return a + b

print(add(5, 10))

#--------------Default Parameter---------------
def greet(name="Sandeep"):
    print(name)

greet() #by defalut its print sandeep

greet("Rahul") #its print rahul 


#--------------Keyword Arguments---------------
def student(name, age):
    print(name, age)

student(age=20, name="Sandeep") #order not matter
student("sandeep",20)# -> Positional Arguments 


#--------------Return Multiple Values-----------------
def calculate(a, b):
    return a+b, a-b

sum1, sub1 = calculate(5,10)
print(sum1)
print(sub1)


#---------------Local Variable-------------------
def demo():
    x = 100
    print(x)
demo()

#if i will try to print x outer from function 
'''
print(x)
ERROR: NameError
'''

#----------------------Global Variable----------------
x = 100
def demo():
    print(x)
demo()

#-------------------Global Keyword------------------
count = 0
def increase():
    global count # global keyword use for global any variable
    count += 1
increase()
print(count)

#-------------------Recursion------------------
'''
def fun():
    print("Hello")
    fun()
fun()

output: RecursionError
Infinite recursion
'''

#------------------Correct recursion---------------
def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n-1)

countdown(5)

#----------------Lambda Function-----------------
mult = lambda x,y: x*y
print(mult(5,5))


#-------------------map()------------------
arr = [1,2,3,4]
result = list(map(lambda x:x*2,arr))
print(result)

arr = [1,2,3,4]
result = list(map(lambda x:x%2==0,arr)) # -> its print true or false only
print(result)

#----------------filter()-----------------
arr = [1,2,3,4,5,6]
result = list(filter(lambda x:x%2==0, arr)) # -> its print number only even
print(result)

#---------------function inside funtion -----------------------
def outer():
    def inner():
        print("Hello")
    inner()
outer()

#----------------Variable Length Arguments--------------------
# *args
def add(*numbers):
    print(numbers)
    print(type(numbers))
add(1,2,3,4,5)


# **kwargs
def student(**data):
    print(data)
    print(type(data))
student(name="Sandeep", age=20)



'''
5 Start:
return
Parameters
Arguments
Local Variables
Recursion

4 Start:
*args
Multiple Return
Lambda

3 Start:
map()
filter()
'''