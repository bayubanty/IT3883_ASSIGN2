# ASSIGN-2-3883
# Program Name: Calc_Average.py
# Course: IT3883/Section XXX
# Student Name: Awoh, Bayo
# Assignment Number: Lab #2
# Due Date: 02/07/2025
# Purpose: recall data and arrange the result in ascending order
# List Specific resources used to complete the assignment.

def calculate_averages(filepath):
    students = []

    with open(filepath, 'r') as file:
        for line in file:
            name, *scores = line.split()
            students.append((name, sum(map(int, scores)) / len(scores)))

    for name, avg in sorted(students, key=lambda x: x[1], reverse=True):
        print(f"{name} {avg:.2f}")

calculate_averages("/Users/bayoawoh/PycharmProjects/pythonProject22/records.txt")
