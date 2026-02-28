print(1+1)#addition
print(2-1)#subtraction
print(2*2)#multiplication
print(4/4)#division
print(4%3)#remainder
print(4**2)#power
print(4//2)#floor division ..(rounds down the nearest value.. return an integer instead of float value)
print("my name is " + "charan") 

age=19
age+=5#age=age+5
print(f"my age is {age}")

num=20
num*=4#num=num*4
print(num)

name="sai"
name+=" charan"
print(name)

#comparision operators
a=1
b=2
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

#Boolean operators
condition1=True
condition2=False
print(not condition1)#tells that  that  it is not true
print(condition1 and condition2)#tells that both are true
print(condition1 or condition2)#tells anyone is true
print(False or 'hey')
print('hi' or 'hey')
print(False or '[]')

print('sai' and 'charan')
print(False and 'charan')
print([] and 'sai')
print([] and False)
print(False and [])

#Example of terenary operator
age = int(input("enter your age "))
def is_adult(age):
    return True if age>18 else False
print(is_adult(age))