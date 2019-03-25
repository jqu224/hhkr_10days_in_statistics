Task 
The ratio of boys to girls for babies born in Russia is 1.09:1. 
If there is 1 child born per birth, 
what proportion of Russian families with exactly 6 children will have at least 3 boys?

Write a program to compute the answer using the above parameters. 
Then print your result, rounded to a scale of  decimal places (i.e.,  format).


# Enter your code here. Read input from STDIN. Print output to STDOUT

boy, girl = map(float, input().split())
p_girl = girl / (boy + girl)
girl6 = (p_girl) ** 6
girl5 = 6 * ((p_girl) ** 5) * (1- p_girl)
girl4 = 15 * ((p_girl) ** 4) * ((1- p_girl) ** 2)
answer = 1 - girl6 - girl5 - girl4 

print("%.3f" % float(answer))
