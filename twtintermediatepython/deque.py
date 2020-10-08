# Deque

# Deques Are Also Known As Double Ended Queue. Their Main Feature Is Made To Add And Remove Elements From Either End Of Another Collection

import collections
from collections import deque

d = deque("hello")
# When You Convert A String To A Deque, It Just Converts To A List With Each Character As An Element In The List
print(d)

# We Might Think That Deques Act And Have The Functionality Of A List, But Deques Actually Provide Even More Funtionality.
# Normal List Function Append
d.append('4')
# PopLeft: Pop The Left-Most Element
d.popleft()
print(d)

# Extend: Will Append Whatever Is Passed Into .extend() To The End
d.extend('456')
print(d)

d.rotate(-1)
print(d)