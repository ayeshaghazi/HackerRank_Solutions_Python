'''
Given 2 sets of integers, M and N, print their symmetric difference in ascending order. 
The term symmetric difference indicates those values that exist in either M or N but do not exist in both.
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

M = int(input())
a = set(list(map(int, input().split())))
N = int(input())
b = set(list(map(int, input().split())))
z = list(a.symmetric_difference(b))
z.sort()
for _ in range(len(z)):
    print(z[_], end="\n")
