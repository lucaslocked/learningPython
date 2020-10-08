# Filter Functions

# Filter Functions Are Similar To Map Functions As Well, Mainly Due To The Fact That It Is An Iterator As Well. However Filter Functions Have The Added Functionality To Run Certain Functions In Order To Filter Values Based On That Function. An Example Would Be If A We Used An isOdd() Function, We Could Filter isOdd() With Our List, Tuple, Set, Etc. And It Would Only Return The Values That Came Out As Odd. Without Any Type Of Function That Would Allow The Filter Function To Filter A List, Tuple, Set, Etc. The Filter Function Is Nothing But The Map Function

def add7(x):
    return x + 7

def isOdd(x):
    return x%2 != 0

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

b = list(filter(isOdd, a))

c = list(map(add7, filter(isOdd, a)))
print(c)