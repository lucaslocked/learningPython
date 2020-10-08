# Lambda Function

# Lambda Function Means 'Anonymous Function'. It Is Used When The Function You Create, Regardless Of The Parameters Passed, Can Only Consist Of One Expression. Another Use Case For It When You Want To Create Small Functions Inside A Larger Function Which Can Lower Line Count And Creates Cleaner Code

def func(x):
    func2 = lambda x: x + 5
    return func2(x) + 2

func3 = lambda x, y: x + y
print(func3(2,1))

print(func(2))

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_list = list(map(lambda x: x % 2 == 0, a))
print(new_list)