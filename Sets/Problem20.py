'''
The students of District College have subscriptions to English and French newspapers. 
Some students have subscribed only to English, some have subscribed only to French, and some have subscribed to both newspapers.
You are given two sets of student roll numbers. 
One set has subscribed to the English newspaper, one set has subscribed to the French newspaper. 
Your task is to find the total number of students who have subscribed to both newspapers.
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
n_roll_numbers = set(map(int, input().split()))
b = int(input())
b_roll_numbers = set(map(int, input().split()))
print(len(list(n_roll_numbers.intersection(b_roll_numbers))))