import string
import random

s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)



def start_input():
    char_num = input("how many characters for the password?: ")
    return char_num


while True:
    try:
        char_num = int(start_input())
        if char_num < 6:
            print("you need at least 6 characters")
            char_num = int(start_input())
        else:
            break
    except:
        print("please enter number only")
        start_input()      

random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

part1 = round(char_num * (30/100))
part2 = round(char_num * (20/100))

password = []

for i in range(part1):
    password.append(s1[i])
    password.append(s2[i])

for i in range(part2):
    password.append(s3[i])
    password.append(s4[i])

random.shuffle(password)
result = "".join(password[0:])

print(result)