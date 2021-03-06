# Task 
# Given an array, X, of N integers and an array, W, representing the respective weights of 's elements, calculate and print the weighted mean of 's elements. Your answer should be rounded to a scale of  decimal place (i.e., format).
# Input Format

# The first line contains an integer, , denoting the number of elements in arrays  and . 
# The second line contains  space-separated integers describing the respective elements of array . 
# The third line contains  space-separated integers describing the respective elements of array .

# Constraints
# n in (0, 50)
# xi, where  is the  element of array .
# wi, where  is the  element of array .
# Output Format

# Print the weighted mean on a new line. Your answer should be rounded to a scale of  decimal place (i.e.,  format).

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
xi = list(map(int,input().split()))
ni = list(map(int,input().split())) 

for i in range(len(xi)):
    xi[i] *= ni[i]

print("%.1f" % (sum(xi)/sum(ni)))

