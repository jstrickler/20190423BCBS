#!/usr/bin/env python

d1 = dict()
print(d1)
d2 = {'a': 5, 'm': 4, 'c': 2}

state_capitals = {'NC': 'Raleigh', 'SC': 'Columbia', 'VA': 'Richmond'}

state_capitals['TN'] = 'Memphis'

state_capitals['TN'] = 'Nashville'

state_capitals['GA'] = 'Atlanta'

print(state_capitals, '\n')

print(state_capitals['VA'])   # foo[2]

print(state_capitals.get('WV'))
print(state_capitals.get('WV', 'NOT FOUND'))

print(state_capitals.setdefault('WV', 'Charleston'))

print(state_capitals)

for state in "NJ", 'VA', 'WA', 'NM', 'ZEIFJOIEJF':
    print(state, state in state_capitals)
print()

for state, capital in sorted(state_capitals.items()):
    print(state, capital)
print()

print(list(state_capitals.items()))


















