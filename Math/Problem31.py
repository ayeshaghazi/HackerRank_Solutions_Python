'''
You are given three integers: a, b, and m. Print two lines.
On the first line, print the result of pow(a,b). On the second line, print the result of pow(a,b,m).
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

if __name__ == '__main__':
    a=int(input())
    b=int(input())
    m=int(input())
    
    print(pow(a,b))
    print(pow(a, b, m))