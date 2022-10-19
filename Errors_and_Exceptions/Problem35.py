'''
You are given a string S.
Your task is to find out whether S is a valid regex or not.
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
T=int(input())
for t in range(T):
    S=input()
    text="This is some text for the regex."
    try:
        re.match(S, text)
        print(True)
    except:
        print(False)