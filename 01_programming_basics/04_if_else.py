user_input = int(input('Enter Your Age: '))

if user_input >= 18:
    print(f'Your age is {user_input}. Your have RTV.')

elif user_input<=18 and user_input>=13:
    print(f'Your age is {user_input}. Your are in teenage.')

else:
    print('Your are children')



# one line if else
print("you have RTV." if user_input>=18 else "you are in teenage" if user_input<=18 and user_input>=13 else "You are childern")