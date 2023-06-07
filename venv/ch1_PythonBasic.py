import numpy as np
import pandas as pd

# Running Python
6000 + 4523.50 + 134.25
_ + 8192.75


def fun(name: str):
    if isinstance(name, str):
        print(name)
    else:
        print('Missing String!')


# 1.3 Primitives, Variables and Expression
principal = 1000
rate = 0.05
numyears = 5
year = 1

while year <= numyears:
    principal = principal * (1 + rate)
    # print(f'{year:>3d} {principal:0.2f}')
    print('%3d %0.2f' % (year, principal))
    year += 1

# 1.4 Arithmetic Operators

x = float(7) / float(4)
type(x)
round(x, 1)

# 1.5 Conditionals and Control Flow
a = 2
b = 10

x = 0
while (x := x + 1) < 10:
    print(x)

x = 0
while x < 10:
    if x == 5:
        break
    else:
        print(x)
        x += 1
print('Done')


# date: 07-June-2023
# 2.11 Operations on Mutable Sequences
a = [1, 2, 3, 4]
b = 4*[a]
b = [list(a) for _ in range(4)]
print(b)
a[0] = -1
print(b)
a1, *_, aL = a
a = [1, 2, 3, 4, 5]
a[1] = 6
print(a)
a[2:] = [0]

# 2.12 Operations with Sets
a = {'a', 'b', 'c'}
a = ['a', 'b', 'c']
# a = {'a': [1, 2, 3]} # dict
b = {'c', 'd'}
b = ['c', 'd']
z = a
z += b
a & b
a.add('j')

a = {'x': 1, 'y': 2, 'z': 3}
b = {'z': 3, 'w': 4, 'q': 5}

a.keys() | b.keys()

# 2.13 Operations on Mappings
d['x', 'y', 'z'] = [1, 4, 6]

d = {}
d[1, 2, 3] = 'foo'
d[1, 0, 3] = 'bar'

d = {}
d['foo'] = [1, 2, 3]
d['bar'] = [1, 0, 3]
d = dict(zip(['foo', 'bar'], [[1, 2, 3], [1, 0, 4]]))

d = {}
d[(1, 2, 3)] = 'foo'
d[(1, 0, 3)] = 'bar'
print(d)

# 2.14 List, Set, and Dictionary Comprehensions
nums = [1, 2, 3, 4, 5]
squares = []
for n in nums:
    squares.append(n * n)
print(squares)
nums = [1, 2, 3, 4, 5]
squares = [n * n for n in nums]
print(squares)
squares = [n * n for n in nums if n > 2]
print(squares)
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'MSFT', 'shares': 50, 'price': 45.67},
    {'name': 'HPE', 'shares': 75, 'price': 34.51},
    {'name': 'CAT', 'shares': 60, 'price': 67.89},
    {'name': 'IBM', 'shares': 200, 'price': 95.25}
]

names = [s['name'] for s in portfolio]
more100 = [s['name'] for s in portfolio if s['shares'] > 100]
cost = sum([s['shares']*s['price'] for s in portfolio])
name_shares = [(s['name'], s['shares']) for s in portfolio]

names = {s['name'] for s in portfolio}
price = {s['name']: s['price'] for s in portfolio}
type(price)


def toint(x):
    try:
        return int(x)
    except ValueError:
        return None


values = ['1', '2', '-4', 'n/a', '-3', '5']
data1 = [toint(x) for x in values]
# following both command are equivalent
data2 = [toint(x) for x in values if toint(x) is not None]
data3 = [v for x in values if(v := toint(x)) is not None]
data4 = [v for x in values if(v := toint(x)) is not None and v >= 0]

# 2.15 Generator Expressions
nums = [1, 2, 3, 4, 5]
squares = (x*x for x in nums)
for n in squares:
    print(n)

path = r'C:\Users\ggeor\OneDrive\PythonCodeProjects\PythonDistiled'
f = open(path + r'\data.txt')
line = (t.strip() for t in f)
comments = (t for t in line if t[0] == '#')
type(comments)

for c in comments:
    print(c)
clist = list(comments)
data1 = [v for x in values if(v := toint(x)) is not None]
data1 = [v for x in values if (v := toint(x)) is not None and v >= 2]
sum(x*x for x in data1)

# 2.16 The Attribute (.) Operator











