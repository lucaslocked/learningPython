# Collections - Counters

# Collections Are Containers That Store Collections Of Data, And The Most Popular Ones Are Known As Lists, Sets, And Tuples. The One That I'm Using Is Known As Counters. Counters Are Dictionary Subclasses That Are Used To Count Hashable Objects. It Is An Unordered Collection Where Elements Are Stored As Dictionary Keys

import collections
from collections import Counter

# Containers
    # List
    # Set
    # Dict
    # Tuple - Immutable

# Types
    # Counter
    # Deque
    # namedTuple()
    # Ordered Dict
    # Default Dict

c = Counter('gallad')
print(c)

c = Counter(['a', 'a', 'b', 'c', 'c'])
print(c)

c = Counter({'a': 1, 'b': 2})
print(c)

c = Counter(cats = 4, dogs = 7)
print(c)

# The .elements() Function Is Used With The list() Function So That You Can Create A List Of All Of The Elements In The Collection. It Doesn't Matter Which Type Of Collection Is Used
print(list(c.elements()))

# The .most_common() Function Creates A List Ordering The Elements Inside The Collections (Again, It Doesn't Matter Which Type Of Collection Is Used) Nested In A Tuple With The Number Of Times That The Element Appears In The Collection.
print(c.most_common())

c = Counter(a = 4, b = 2, c = 0, d = -2)
d = ['a', 'b', 'c', 'd', 'e', 'f']
c.subtract(d)
print(c)
c.update(d)

print(c)
c.clear()
print(c)

c = Counter(a = 4, b = 2, c = 0, d = -2)
d = Counter({'a', 'b', 'b', 'c'})

print(c + d)
print(c - d)
print(c & d)