# Map Functions

# Map Functions Return The Map Object (Which Is Basically An Iterator) Of The Results After Applying The Given Function To Each Item Of Given Iteralbe Parameters

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def function(x):
    return x ** x

# newList = []
# for x in li   :
#     newList.append(function(x))

# print(newList)

# Mapping Allows Me To Write Everything Above In Only A One Line Of Code
print(list(map(function, li)))

# Below Is Basically The Functionality That the map() Function Provides
print([function(x) for x in li if x % 2 == 0])