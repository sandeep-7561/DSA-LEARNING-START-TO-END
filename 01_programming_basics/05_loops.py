#while loop
n = 1
while n <= 10:
    print(n)
    n +=1


#Forward loop
for i in range(5):
    print(i)

# backward loop 
for i in range(10,0,-1):
    print(i)

# Custom Step
for i in range(0,20,2):
    print(i)

#Reverse Traversal
arr = [10,20,30,40,50]
rev_arr = []
for i in range(len(arr)-1,-1,-1):
    rev_arr.append(arr[i])
print(rev_arr)

#nested loop
for i in range(3):
    for j in range(3):
        print(i, j)

'''
time complexity:
    Runs:
        n times
    Complexity:
        O(n)

Nested Loop:
    Runs:
        n x n
    Complexity:
        O(n²)
'''

# Break
for i in range(1,11):
    if i > 5:
        break
    print(i)

# Continue 
for i in range(1,11):
    if i == 5:
        continue
    print(i)

# pass 
for i in range(5):
    pass

# While True 
'''
comment for reason
while True:
    input_usr = input("Enter: ")
    if input_usr.lower() == 'exit':
        break

    print("you enter", input_usr)
'''

# Loop over String
name = 'SANDEEP'
for ch in name:
    print(ch)

# loop over list 
arr = [22,88,63,45,23]
for x in arr:
    print(x)

# Loop using Index 
for i in range(len(arr)):
    print(i,arr[i])

# Enumerate
for index, value in enumerate(arr):
    print(index,value)


# two pointers
arr = [10,20,30,40,50]

left = 0
right = len(arr)-1
while left <= right:
    print(arr[left],arr[right])
    left += 1
    right-=1

#sliding window
arr = [1,2,3,4,5]
k = 3
for i in range(len(arr)-k+1):
    print(arr[i:i+k])


# Loop Inside Loop (Pattern Problems)
for i in range(5):
    for j in range(i+1):
        print("*",end=" ")
    print()

