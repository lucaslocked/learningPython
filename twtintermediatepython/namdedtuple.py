# Named Tuples
# Named Tuples Assign Meaning To Each Position In A Tuple And Allow For More Readable, Self-Documenting Code. They Can Be Used Wherever Regular Tuples Are Used, And They Add The Ability To Acess Fields By Name Instead Of Position.

import collections
from collections import namedtuple

Point = namedtuple('Point', {'x': 0, 'y': 0, 'z': 0})
newP = Point(3, 4, 5)
print(newP.x, newP.y, newP.z)
print(newP[0])
print(newP._asdict())
print(newP._fields)
newP = newP._replace(y=6)
print(newP)

p2 = Point._make(['a', 'b', 'c'])
print(p2)