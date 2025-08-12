import random

string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&'()*+,-./:;<=>?@[\]^_{|}~"

length  = int(input("enter the password length : "))

password = ""

for _ in range(length):
    password += random.choice(string)

print(password)