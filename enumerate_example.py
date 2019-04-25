#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

for i, fruit in enumerate(fruits):
    print(i, fruit)

print(list(enumerate(fruits)))

e = enumerate(fruits)
print(e)

for thing in e:
    print(thing)