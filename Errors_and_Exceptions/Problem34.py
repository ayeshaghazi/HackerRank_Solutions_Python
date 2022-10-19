'''
You are given two values a and b.
Perform integer division and print a/b.
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for _ in range(T):
    try:
        a, b = map(int, input().split())
        print(a // b)
    except (ZeroDivisionError, ValueError) as error:
        print("Error Code:", error)