#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

with open('myfruits.txt', 'w') as myfruits_out:
    for fruit in fruits:
        myfruits_out.write(fruit.upper() + '\n')

#with open('myfruits.txt', 'x') as myfruits_out:
#    for fruit in fruits:
#        myfruits_out.write(fruit.upper() + '\n')

    