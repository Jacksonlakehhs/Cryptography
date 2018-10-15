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


prompt = input("Enter e to encrypt, d to decrypt, or q to quit: ")


if prompt != "q":
    message = input("Message: ")
    key = input("Key: ")
    for i in range(0, len(message)): 
        nums = print(associations.find(message[i]) + associations.find(key[i]))

else: 
    print("Goodbye!")