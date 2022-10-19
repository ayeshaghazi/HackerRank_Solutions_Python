'''
Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
'''

if __name__ == '__main__':
    score_list=[]
    student_score_list=[]

    #Append inputs to a master list of lists
    for _ in range(int(input())):
        name = input()
        score = float(input())
        score_list.append(score)
        student_score_list.append([name, score])

    #Retrieve the second_lowest_score
    score_list=sorted(set(score_list))
    score_list.remove(min(score_list))
    second_lowest_score=score_list[0]
    
    #Sort the master list of lists by the student name
    student_score_list=sorted(student_score_list, key=lambda x: x[0])
    
    #Search the master list of lists for the second lowest score and return student names in alphabetical order
    for student_list in student_score_list:
        if second_lowest_score in student_list:
            print(student_list[0], end="\n")
    
    


