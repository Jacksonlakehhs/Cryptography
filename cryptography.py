"""
cryptography.py
Author: Jackson Lake
Credit: 

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
#convert each one to a number that represents it, operate on that number, then convert back to a letter.

associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

command = input("Enter e to encrypt, d to decrypt, or q to quit: ")

if command == "e" or command == "d":
    message = input("Message: ")
    key = input("Key: ")
    if len(message) > len(key):
        key = len(message)*key
    nums=[]
    if command == "e":
        for i in range(len(message)): 
            nums.append(associations.find(message[i]) + associations.find(key[i]))
        for x in nums:
            print(associations[x], end = '')
    if command == "d":
        for i in range(len(message)): 
            nums.append(associations.find(message[i]) - associations.find(key[i]))
        for x in nums:
            print(associations[x], end = '')
elif command == "q": 
    print("Goodbye!")
else:
    print("Did not understand command, try again.")