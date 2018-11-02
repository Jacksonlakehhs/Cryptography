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
command = "z"


while command != "q":
    command = input("Enter e to encrypt, d to decrypt, or q to quit: ")
    if command == "e" or command == "d":
        message = input("Message: ")
        key = input("Key: ")
        if len(message) > len(key):
            key = len(message)*key
        nums=[]
        if command == "e":
            for i in range(len(message)): 
                thing = associations.find(message[i]) + associations.find(key[i])
                if thing >= 86:
                    associations = associations*2
                print(associations[thing], end = '')
            print()
        if command == "d":
            for i in range(len(message)):
                thing = associations.find(message[i]) - associations.find(key[i])
                if thing < 0:
                    thing += 86
                print(associations[thing], end = '')
            print()
    elif command != "q": 
        print("Did not understand command. try again.")

print("Goodbye!")