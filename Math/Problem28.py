'''
ABC is a right triangle, 90 degrees at B.
Therefore, the angle of ABC = 90 degrees.
Point M is the midpoint of hypotenuse AC.
You are given the lengths AB and BC.
Your task is to find angle MBC (angle theta, as shown in the figure) in degrees
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import atan, degrees

def solve(side_AB, side_BC):
    answer = degrees(atan(side_AB/side_BC))
    return answer

side_AB = int(input())
side_BC = int(input())
result = round(solve(side_AB, side_BC))
print("{}\xb0".format(result))
