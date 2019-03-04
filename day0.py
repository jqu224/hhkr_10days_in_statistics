# Enter your code here. Read input from STDIN. Print output to STDOUT
import heapq as hq

# read the total number 
count = int(input())

# a, read in the list and convert it into a list of int
my_list = input().split()
inputs = list(map(int, my_list))
len_list = len(inputs) 
mean = sum(inputs) / len_list


# c, find the mode
dict_list = {}
for i in inputs:
    if i in dict_list:
        dict_list[i] += 1
    else:
        dict_list[i] = 1
max_num, max_ocr = 0, 0
for key, value in dict_list.items():
    if max_ocr < value:
        max_num, max_ocr = key, value
    if max_ocr == value and  max_num > key:
        max_num, max_ocr = key, value

# b, find the median
hq.heapify(inputs)
temp1 = inputs[0]
for i in range(0,round(len_list/2)):
    temp1 = hq.heappop(inputs)
if len_list%2 == 0:
    temp2 = hq.heappop(inputs)
else:
    temp2 = temp1
median = (temp1 + temp2) / 2

print(mean)
print(median)
print(max_num)


