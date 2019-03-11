# Enter your code here. Read input from STDIN. Print output to STDOUT

x = int(input())
listA = list(map(int, input().split()))
listA = sorted(listA)

mid = x // 2 
if x % 2 == 0:
    median = (listA[mid] + listA[mid - 1]) / 2
else:
    median = listA[mid]

ptile25 = mid // 2 - 1
ptile25_1 = mid // 2 

if mid % 2 == 0:
    q25 = (listA[ptile25] + listA[ptile25_1]) / 2
    q75 = (listA[-ptile25-2] + listA[- ptile25_1]) / 2 
else: 
    q25 = listA[ptile25_1] 
    q75 = listA[-ptile25_1-1] 

# print((q25), (median), (q75), sep="\n")
print(round(q25), round(median), round(q75), sep="\n")
