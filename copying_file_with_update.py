#!/usr/bin/env python

with open('myfruits.txt') as myfruits_in:
    with open('pfruits.txt', 'w') as pfruits_out:
        for fruit in myfruits_in:
            if fruit.lower().startswith('p'):
                pfruits_nout.write(fruit)