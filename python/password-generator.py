import random

length = 16
symbols = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-=!@#$%^&*()_+,./")

password = ""
for i in range(length):
  password += random.choice(symbols) # random.choice() selects random object from the array

print("Password: " + password)
