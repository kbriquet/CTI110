# CTI-110

# P2HW2 - List

# Kervens Briquet

# 06/20/2023


print("Grade Tracker")
print()

grades = []

module1 = float(input("Enter grade for Module 1: "))
grades.append(module1)

module2 = float(input("Enter grade for Module 2: "))
grades.append(module2)

module3 = float(input("Enter grade for Module 3: "))
grades.append(module3)

module4 = float(input("Enter grade for Module 4: "))
grades.append(module4)

module5 = float(input("Enter grade for Module 5: "))
grades.append(module5)

module6 = float(input("Enter grade for Module 6: "))
grades.append(module6)

print()

print("-----------Results-----------")


lowest_grade = min(grades)
highest_grade = max(grades)
grade_sum = sum(grades)
grade_average = grade_sum / len(grades)

print("Lowest Grade:   ", format(lowest_grade, ".2f"))
print("Highest Grade:  ", format(highest_grade, ".2f"))
print("Sum of Grades:  ", format(grade_sum, ".2f"))
print("Average Grade:  ", format(grade_average, ".2f"))
print("---------------------------------------")

# updated 06/22/2023
