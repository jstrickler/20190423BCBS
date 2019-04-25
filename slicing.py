#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

print(fruits[0:3], '\n')
print(fruits[2:7], '\n')

#  ITER[START:STOP]  ITERABLE[START:STOP:STEP]
#  ITER[:STOP]   ITER[START:]

#  ITER[0:len(ITER):1]  default value

print(fruits[:3], '\n')
print(fruits[-3:], '\n')

print(fruits[0:3], '\n')
print(fruits[-3:len(fruits)], '\n')
print(fruits[::2], '\n')
print(fruits[1::2], '\n')

more_fruits = ['durian', 'tomato', 'eggplant']

print(fruits, '\n')
fruits[2:2] = more_fruits
print(fruits, '\n')

actor = 'Chris Hemsworth'

print(actor[:5])
print(actor[-5:])
print(actor[6:9])
print(actor[6:4])
print(actor[6:99])




















