#number 3

import random
size=25
array=[]

num1=int(input("enter first number:"))
num2=int(input("enter last number:"))

for i in range(size):
  element=random.randint(num1,num2)
  array.append(element)


print("random int value",array)