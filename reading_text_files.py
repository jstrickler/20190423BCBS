#!/usr/bin/env python

# mary_in = open('DATA/mary.txt')

with open('DATA/mary.txt') as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip()
        print(line)

print('-' * 30)

with open('DATA/mary.txt') as mary_in:
    all_contents = mary_in.read()
    print(all_contents, '\n')
    print(repr(all_contents))

print('-' * 30)

# read lines WITH newlines
with open('DATA/mary.txt') as mary_in:
    all_lines = mary_in.readlines()
    print(all_lines)

print('-' * 30)

# read lines WITHOUT newlines
with open('DATA/mary.txt') as mary_in:
    all_lines = [line.rstrip() for line in mary_in]
    print(all_lines)

    