#map
# numbers=[1, 2, 3, 4, 5]
# def double(a):
#     return a*2
# result=map(double, numbers)
# print(list(result))

#filter
# numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# def even(a):
#     return a%2==0
# result=filter(even,numbers)
# # print(list(result))

# numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# result=filter(lambda x:x%2==0,numbers)
# print(list(result))

#reduce
from functools import reduce
expenses=[('rent', 1000), ('groceries', 200)]
sum=reduce(lambda a, b: a[1]+b[1], expenses)
print(sum)