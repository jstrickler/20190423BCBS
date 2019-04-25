#!/usr/bin/env python
from pprint import pprint

knight_data = {}

with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')
#        print(name, title, color, quest, comment)
        knight_data[name] = title, color, quest, comment

pprint(knight_data)
print()

#        KEY, VALUE in DICT.items()
for knight_name, knight_info in sorted(knight_data.items()):
    print(knight_info[0], knight_name)
print()

print(knight_data['Lancelot'])
print(knight_data['Lancelot'][2])
