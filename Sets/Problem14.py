'''
Ms. Gabriel Williams is a botany professor at District College. 
One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.

Formula used:
Average = Sum of distinct heights / Total number of distinct heights
'''

def average(array):
    # your code goes here
    return round(sum(set(array))/len(set(array)), 3)