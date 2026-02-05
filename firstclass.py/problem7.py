import random
size = 11
array=[]

for i in range(size):
    random_number = round(random.uniform(0, 10),1)
    array.append(random_number)

# Sort the array in ascending order
array_sorted = sorted(array)

# Find the first minimum
first_minimum = array_sorted[0]

# Find the second minimum
second_minimum = array_sorted[1]

# Find the first maximum
first_maximum = array_sorted[-1]

# Find the second maximum
second_maximum = array_sorted[-2]

# Find the median value
median_value = array_sorted[size // 2]

print("Array:", array)
print("First Minimum:", first_minimum)
print("Second Minimum:", second_minimum)
print("First Maximum:", first_maximum)
print("Second Maximum:", second_maximum)
print("Median Value:", median_value)
