# Enter your code here. Read input from STDIN. Print output to STDOUT

# Enter your code here. Read input from STDIN. Print output to STDOUT
import heapq
x = int(input())
list_A = list(map(int, input().split()))
list_B = list(map(int, input().split()))
ult_list = []
for i, num in enumerate(list_A):
    for j in range(list_B[i]):
        ult_list.append(num)
ult_list = sorted(ult_list)

x = len(ult_list)
mid = x // 2 
if x % 2 == 0:
    median = (ult_list[mid] + ult_list[mid - 1]) / 2
else:
    median = ult_list[mid]

ptile25 = mid // 2 - 1
ptile25_1 = mid // 2 

if mid % 2 == 0:
    q25 = (ult_list[ptile25] + ult_list[ptile25_1]) / 2
    q75 = (ult_list[-ptile25-2] + ult_list[- ptile25_1]) / 2 
else: 
    q25 = ult_list[ptile25_1] 
    q75 = ult_list[-ptile25_1-1] 

# print(ult_list)
# print((q25), (median), (q75), sep="\n")
print("%.1f" %(float(q75 - q25)))
