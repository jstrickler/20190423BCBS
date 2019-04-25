#!/usr/bin/env python

while True:
    user_name = input("What is your name? (q to quit) ")
    if user_name == 'q':
        break
    if user_name == '':
        continue
    print("Hello,", user_name)


# NOT PYTHONIC:
#i = 0
#while i < 10:
#    print(i)
#    i += 1
    