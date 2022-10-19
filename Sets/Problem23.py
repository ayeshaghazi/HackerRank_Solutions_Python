'''
You are given a set A and N number of other sets. 
These N number of sets have to perform some specific mutation operations on set A.
Your task is to execute those operations and print the sum of elements from set A.
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
set_A = set(map(int, input().split()))
N = int(input())
for _ in range(N):
    command, length = input().split()
    set_b = set(map(int, input().split()))
    exec("set_A.{}({})".format(command, set_b))

print(sum(set_A))