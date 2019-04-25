#!/usr/bin/env python


fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

f0 = []
for f in fruits:
    f0.append(f.upper())
print("f0:", f0, '\n')

f1 = [f.upper() for f in fruits]
print("f1:", f1, '\n')

f2 = [f.upper() for f in fruits if f.startswith('p')]
print("f2:", f2, '\n')

f3 = [f for f in fruits if f.startswith('p')]
print("f3:", f3, '\n')

nums = [800,80,1000,32,255,400,5,5000]

n1 = [float(i) for i in nums]
print("n1:", n1, '\n')

n2 = [10 * float(i) for i in nums if i > 100]
print("n2:", n2, '\n')

ng1 = (float(i) for i in nums)
print("ng1:", ng1, '\n')


for x in ng1:
    print(x)
















