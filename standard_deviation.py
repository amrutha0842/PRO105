import math
import csv
from collections import Counter 

with open('data.csv', newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)
#file_data.pop(0)
data = file_data[0]
#Finding Mean
def mean(data):
    n = len(data)
    total = 0
    for x in data:
        total += int(x)
    mean = total/n
    return mean

# Squaring and getting the values 
square_list = []
for number in data:
    a = int(number) - mean(data)
    a = a**2 
    square_list.append(a)

# Getting Sum
sum = 0
for i in square_list:
    sum = sum + i
    
# Dividing the sum by the total value
result = sum/(len(data)-1)

# getting the deviation by taking the square root of the result
standard_deviation = math.sqrt(result)
print("standard deviation" + str(standard_deviation))