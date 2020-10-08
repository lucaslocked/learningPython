import re

# for i in range(1, 100):
#     print(i, end=", ")

k = 'aa'
s = 'aaadaa'
result = re.search(k, s)
indices = (result.start(), result.end())
print(indices)
result = re.search(k, s)
indices = (result.start(), result.end() - 1)
print(indices)
