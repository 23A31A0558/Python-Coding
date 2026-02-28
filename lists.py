# name="charan"
# print(name[0])
# print(name[-1])
# print(name[1:3])#prints characters with index range

#
names=["sai","charan","hi","pragati"]
# print("charan" in names)
# print("hello" in names)
# print(7 in names)
# print(names)
# print(names[2:5])#sclicing of list
# print(len(names))
# names.append("hello")#adds element at the end of the list
# print(names)
names.insert(2,"hi")#adds element at the specified index
print(names)
names.remove("hi")#removes the first occurrence of the specified element
print(names)
names[1:3]=["hello","hi"]#replaces the specified range of elements with new elements
print(names)
names.sort()#sorts the list in ascending order
print(names)