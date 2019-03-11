# Enter your code here. Read input from STDIN. Print output to STDOUT
 
n = int(input())
list_a = list(map(int, input().split()))
count = len(list_a)
avg = sum(list_a) / count
dividend = 0
for i in list_a:
    dividend += (i - avg)  ** 2
answer = (dividend / count) ** 0.5
print("%.1f" % answer)
