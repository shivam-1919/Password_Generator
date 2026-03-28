import string
import random

print("Welcome to Advanced Password Generator!\n")

digits = string.digits
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
symbols = string.punctuation

print("Choose any one: Advanced or Simple")
choose = input("For advance 'a'\nFor simple 's'\n: ")

if choose == 's':
    character = digits + lowercase + uppercase + symbols

elif choose == 'a':
    character = string.ascii_letters

    user_number = input("Include Numbers? (y/n): ")
    user_symbol = input("Include Symbols? (y/n): ")

    if user_number == 'y':
        character += digits
    if user_symbol == 'y':
        character += symbols

else:
    print("Invalid choice!")
    exit()

passlen = int(input("Enter password length: "))
passcount = int(input("Number of passwords: "))

for i in range(passcount):
    password = ''.join(random.choices(character, k=passlen))
    print(password)