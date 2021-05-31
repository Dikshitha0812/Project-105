import csv
import math

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]

n = len(data)
total =0
for x in data:
    total += int(x)

mean = total / n


list = []
for x in data:
    a = int(x) - mean
    a = a**2
    list.append(a)
sum = 0
for x in list:
    sum = x + sum
#print(len(data))
div = sum/(n - 1)
sD = math.sqrt(div)
print("Standard Deviation Of The Data = ", sD)