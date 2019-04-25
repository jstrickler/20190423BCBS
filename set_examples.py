#!/usr/bin/env python

agatha_countries = [
    "Peru", "Spain", "France"
        ]

abi_countries = [
        "France", "India", "UK", 'Spain'
        ]

agatha = set(agatha_countries)
abi = set(abi_countries)

print("Both:", agatha & abi)
print("Just one:", agatha ^ abi)
print("All:", agatha | abi)
print("Just Agatha:", agatha - abi)
print("Just Abi:", abi - agatha)
