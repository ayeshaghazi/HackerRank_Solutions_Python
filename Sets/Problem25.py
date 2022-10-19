'''
You are given two sets, A and B.
Your job is to find whether set A is a subset of set B.

If set A is subset of set B, print True.
If set A is not a subset of set B, print False.
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for _ in range(T):
    num_elems_A = int(input())
    set_A = set(map(int, input().split()))
    num_elems_B = int(input())
    set_B = set(map(int, input().split()))
    
    if set_A.issubset(set_B):
        print(True)
    else:
        print(False)