#!/usr/bin/env python

list1 = list()
list2 = [1, 2, 3, 4]
list3 = []

cities = ['Durham', 'Chapel Hill', 'Cary', 'Raleigh',
          'Fuquay-Varina', 'Apex']

print(cities[0], cities[-1])

cities.append('Hillsborough')

print(cities, '\n')

cities.append('Roxboro')
print(cities, '\n')

cities.insert(0, "Tarboro")
cities.insert(4, "Asheboro")

print(cities, '\n')

more_cities = ["Statesboro", "Marion", "Asheville"]

cities.extend(more_cities)

print(cities, '\n')

#  LIST.append(ITEM)  LIST.insert(POS, ITEM)
#  LIST.extend(ITERABLE)

del cities[4]

print(cities, '\n')


cities.remove('Fuquay-Varina')

print(cities, '\n')

c = cities.pop()
print(c)
print(cities, '\n')

c = cities.pop(3)
print(c)
print(cities, '\n')

for city in cities:
    # city = cities[0]
    # block....
    # city = cities[1]
    # block....
    print(city.upper())
    if city == 'Roxboro':
        break

#  for VAR ... in ITERABLE:

#      ... VAR  ...


nums = [800,80,1000,32,255,400,5,5000]

print(len(nums), sum(nums), min(nums), max(nums))
print(sorted(nums))































