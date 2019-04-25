#!/usr/bin/env python

def hello():
    print("Hello, world")
    
hello()
hello()
hello

def greet(whom="world"):
    print("Hello,", whom)
    
greet("world")
greet("Mom")
greet("Everybody!!")
greet()

def welcome(greeting, *people):
    for person in people:
        print("{}, {}".format(greeting, person))
    print()
    
welcome("Hello", "Mom")
welcome("Hello", "Mom", "Dad", "Uncle Fergus")

def nil():
    return "wombat"


x = nil()

print(x)

print(nil() * 10)




def stuff():
    return 'wombat', 42, None

s = stuff()
print(s, type(s))

animal, number, flag = stuff()

print(animal)
print(number)
















