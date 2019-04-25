#!/usr/bin/env python
from collections import namedtuple

person = 'Bill', 'Gates', 'Microsoft'

print(person)

print(person[0], person[1])

first_name, last_name, product = person

print(first_name, last_name)

values = ['a', 'b', 'c', 'd', 'e', 'f']

x, y, *z = values
print(x, y, z)

x, *y, z = values
print(x, y, z)

*x, y, z = values
print(x, y, z)


people = [
    ('Melinda', 'Gates', 'Gates Foundation'),
    ('Steve', 'Jobs', 'Apple', 'NeXT'),
    ('Larry', 'Wall', 'Perl'),
    ('Paul', 'Allen', 'Microsoft', 'Seahawks'),
    ('Larry', 'Ellison', 'Oracle'),
    ('Bill', 'Gates', 'Microsoft', 'Gates Foundation'),
    ('Mark', 'Zuckerberg', 'Facebook'),
    ('Sergey','Brin', 'Google'),
    ('Larry', 'Page', 'Google'),
    ('Linus', 'Torvalds', 'Linux', 'Git'),
]

print(people[0])
print(people[0][0])
print(people[0][0][0])

print(people[-1][-1][-1])

#for person in people:
#    first_name, last_name, product = person
#    print(first_name, last_name)

for first_name, last_name, *product in people:
    print(first_name, last_name, product)
print()


Person = namedtuple('Person', 'first_name last_name product')

p = Person('Bill', 'Gates', 'Microsoft')

print(p.first_name, p.last_name)









