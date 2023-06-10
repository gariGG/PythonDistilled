"""
chapter 3 Program Structure and Control Flow
https://github.com/dabeaz/python-distilled
"""
import numpy as np
import copy

# Chapter 4 Pojects, Types and Protocols
# 4.1 Essential Concepts
a = 10
a.numerator
b = [1, 2, 3]
b.append(7)
c = a + 10
d = b + [4, 5]
d = copy.deepcopy(b)
d = b
d += [4, 5]
b[0] = 100
print(d)


def compare(a, b):
    if a is b:
        print('same object')
    if a == b:
        print('same value')
    if type(a) is type(b):
        print('same type')


a = [1, 2, 3]
b = [1, 2, 3]
compare(a, a)
compare(a, b)
compare(a, [4, 5, 6])

items = list()


def removeall(items: list, item) -> list:
    return [i for i in items if i != item]


class mylist(list):
    def removeall(self, val):
        return [i for i in self if i != val]


items = mylist([5, 8, 2, 7, 2, 13, 9])
items.removeall(2)
a = [1, 2, [3, 4]]
b = list(a)
b.append(100)
b[2][0] = -100
b = copy.deepcopy(a)
b[2][0] = -100
a

from datetime import date
import math
d = date(2012, 12, 21)

print(repr(d))
print(f'The date is: {d!r}')

items = {
    'number': 42,
    'text': 'Hello World'}
items['fun'] = abs
items['error'] = ValueError
items['mod'] = math
nums = [1, 2, 3, 4]
items['append'] = nums.append
line = 'ACME, 100, 490.10'
parts = line.rsplit(',')
column_types = [str, int, float]
row = [ty(val) for ty, val in zip(column_types, parts)]

