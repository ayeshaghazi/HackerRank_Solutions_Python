'''
You have a non-empty set s, and you have to execute N commands given in N lines.
The commands will be pop, remove and discard.
'''

n = int(input())
s = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    command, *args = input().split()
    args = list(args)
    if len(args) > 0:
        exec("s.{}({})".format(command, *args))
    else:
        exec("s.{}()".format(command))

print(sum(s))