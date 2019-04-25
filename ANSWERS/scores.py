#!/usr/bin/env python
# import ...
# GLOBAL_VAR ...

def main():
    data = read_data()
    for student, score in sorted(data.items()):
        grade = get_grade(score)
        print("{:20s} {} {}".format(student, score, grade))
    
    average = get_average(data)
    print("\naverage score is  {:.2f}\n".format(average))

def read_data():
    scores_by_student = {}
    
    with open("../DATA/testscores.dat") as scores_in:
    
        for line in scores_in:
            (name, score) = line.split(":")
            score = int(score)
            scores_by_student[name] = score
    
    return scores_by_student

def get_grade(raw_score):
    if raw_score > 94:
        grade = 'A'
    elif raw_score > 88:
        grade = 'B'
    elif raw_score > 82:
        grade = 'C'
    elif raw_score > 74:
        grade = 'D'
    else:
        grade = 'F'
        
    return grade

def get_average(data):
    total = 0
    for student, score in data.items():
        total += score
    average = total / len(data)

    return average
        

main()