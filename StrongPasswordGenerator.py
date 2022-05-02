
'''
 * @file StrongPasswordGenerator.py
 * @date 2022-05-02
 * @copyright Copyright (c) 2022
'''

'''
    Here i've made one of the good strong password generator
    so that you'll feel about to hack before making 
    such passwords

    You can try it out, go through the code
    Just basic stuff
    I've used random module here
'''

import random

lenth=int(input("How many letters would you like in your password?\n"))

symbols=int(input("How many symbols would you like?\n"))

numbers=int(input("How many numbers would you like?\n"))

number_list=['1','2','3','4','5','6','7','8','9','0']
symbol_list=['!','@','#','$','%','&','*','(',')','+']

char_list=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

ss=""

total_char = lenth-symbols-numbers

# Here we're taking random char,symbols,numbers from the lists
for i in range(0,total_char):
  ss+=random.choice(char_list)

for i in range(0,symbols):
  ss+=random.choice(symbol_list)

for i in range(0,numbers):
  ss+=random.choice(number_list)

# Here i've used -> Suffling of characters in a given string
password=''.join(random.sample(ss,len(ss)))

# Finally pass printing
print(f"Here is your password: {password}")