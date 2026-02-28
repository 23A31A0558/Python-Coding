names=("sai","charan","hi","pragati")
print(names.index("hi"))#returns the index of the first occurrence of the specified element
print(len(names))#returns the number of elements in the tuple
print("sai" in names)#returns True if the specified element is present in the tuple, otherwise False
print(names[1:3])#slicing of tuple
print(sorted(names))#returns a sorted list of the elements in the tuple
newtuple=names+("hello","bye","good morning")#concatenation of tuples
print(newtuple)