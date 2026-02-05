import random
size = 10

array1 = []
array2 = []

for i in range(size):
    array1.append(round(random.uniform(0, 10), 1))  
    array2.append(round(random.uniform(0, 10), 1))  

print("Array 1 (before sorting):", array1)
print("Array 2 (before sorting):", array2)

array1_sorted_desc = sorted(array1, reverse=True)  
array2_sorted_desc = sorted(array2)  

print("Array 1 (descending order):", array1_sorted_desc)
print("Array 2 (ascending order):", array2_sorted_desc)
