'''
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
Print the average of the marks array for the student name provided, showing 2 places after the decimal.
'''

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    def get_average_marks(name):
        marks_list=student_marks.get(name)
        average_marks=sum(marks_list)/len(marks_list)
        return average_marks
    
    print("{:0.2f}".format(get_average_marks(query_name)))