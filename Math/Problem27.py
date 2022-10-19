'''
You are given a complex z. Your task is to convert it to polar coordinates.
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
from cmath import polar

z = complex(input())
result = polar(z)
print(result[0])
print(result[1])