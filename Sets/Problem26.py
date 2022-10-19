'''
You are given a set A and n other sets.
Your job is to find whether set A is a strict superset of each of the n sets.
Print True, if A is a strict superset of each of the n sets. Otherwise, print False.

A strict superset has at least one element that does not exist in its subset.
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
set_A = set(map(int, input().split()))
n = int(input())
set_list = []
for _ in range(n):
    set_ = set(map(int, input().split()))
    set_list.append(set_)
flag = True
for set_ in set_list:
    if set_A.issuperset(set_) != True:
        flag = False
        break
print(flag)