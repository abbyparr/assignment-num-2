import random
import string
import time
import math 

#ask the format (random)
print('what is the format you are using?')
format = input('enter format: random or memorable')
print('the format is', format)

#selecting random characters among character types
    #lower case
x = "abcdefghijklmnop"
lower = random.choice(x)
print(lower)
#printing a random lower case

    #upper case
x = "abcdefghijklmnop"
y = x.upper()
print(y)
#printing upper case letters

upper = random.choice(y)
print(upper)
#printing a random upper case

    #numbers
numbers=[]
for i in range (2):
    numbers.append(random.randrange(1, 11))
    print(numbers)
#printing 2 random integers

    #puncuation symbols
p = "!?."
p = random.choice(p)
print(p)
#printing a random symbol
    
#put the password together
password = lower + upper + numbers + p
print(password)

#argument specifying length of password
#use len() function
length = len(password)
print('the length of the password is', length)

#argument - if you want puncuation symbols included in password
print('would you like puncuation symbols in the password?')
s = input('yes or no')
print(s)

if s == 'yes':
    #puncuation symbols
    p = "!?."
    p = random.choice(p)
    print(p)
#printing a random symbol

else:
    print('no punctuation will be included')

#argument specifying characters that aren't allowed in password
print('what characters are not allowed in the password?')
c = input('enter unwanted characters')

#current time 
print (time.ctime())

with open("Generated_Passwords.txt", "a") as random:
    random.write("append text")
    random.write(time.ctime())







