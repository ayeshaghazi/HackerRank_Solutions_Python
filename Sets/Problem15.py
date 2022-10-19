'''
There is an array of n integers. 
There are also 2 disjoint sets, A and B, each containing m integers. 
You like all the integers in set A and dislike all the integers in set B. Your initial happiness is 0. 
For each i integer in the array, if , you add 1 to your happiness. If i belongs to set B, you add -1 to your happiness. 
Otherwise, your happiness does not change. Output your final happiness at the end.
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

happiness_=0
arr_=[]
n, m = map(int, input().split())
arr_= list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

# Disjoint sets have no elements in common
for _ in range(len(arr_)):
    if arr_[_] in A:
        happiness_+=1
    elif arr_[_] in B:
        happiness_-=1

print(happiness_)
