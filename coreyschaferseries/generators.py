# def square_numbers(nums):
#     result = []
#     for i in nums:
#         yield(i*i)
#     return result

# my_nums = square_numbers([1,2,3,4,5])

my_nums = [x*x for x in [1,2,3,4,5]]

# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))

print(list(my_nums))

for num in my_nums:
    print(num)