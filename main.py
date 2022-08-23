import random

def shuffle_password(string):
    #Convert the string into a list with the builtin function to use the shuffle method
    listTemp = list(string)
    random.shuffle(listTemp)
    return ''.join(listTemp)

#Generate 2 uppercase using builtin chr() with random lib
upper_case1 = chr(random.randint(65, 90))
upper_case2 = chr(random.randint(65, 90))

#Generate 2 lowercase using builtin chr() with random lib
lower_case1 = chr(random.randint(97, 122))
lower_case2 = chr(random.randint(97, 122))

#Generate 2 numbers from 0 - 9
num1 = str(random.randint(0,9))
num2 = str(random.randint(0,9))

#Generate 2 symbols ex: $#@!...
symb1 = chr(random.randint(33, 38))
symb2 = chr(random.randint(33, 38))

#Join all parts generated
string = upper_case1+upper_case2+num1+num2+lower_case2+lower_case1+symb2+symb1

#Call a function to shuffle the string to get a password
password = shuffle_password(string)


print("Your password was generated.")
print("="*10)
print(" {} ".format(password))
print("="*10)
