# CTI-110
# P2HW2 - List
# Kervens Briquet
# 06/20/2023
def main():
    whileLoop()
    #forLoop()


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

def whileLoop():
    keep_going = "NO"
    total = 0
    count = 0
    while keep_going.lower() == "yes":
        grade = int(input("Enter a grade: "))
        total += grade
        count +=1
        keep_going = input("Do you want to enter another grade? Enter yes or no: ")

print("-----------Results-----------")
lowest_grade = min(grades)
highest_grade = max(grades)
grade_sum = sum(grades)
grade_average = grade_sum / len(grades)
print("Lowest Grade: ", format(lowest_grade, ".2f"))
print("Highest Grade: ", format(highest_grade, ".2f"))
print("Sum of Grades: ", format(grade_sum, ".2f"))
print("Average Grade: ", format(grade_average, ".2f"))
print("---------------------------------------")



average = total /count
print(average)

def forLoop():
    scores = []
    num = int(input("Enter number of scores to total: "))
    for i in range (1, num + 1):
        score = float(input(f'Enter score #{i}: '))
        while score < 0 or score > 100:
            print("Bad score!")
            score = float(input(f'Enter score #{i}: '))
        scores.append(score)
    print("Score list:", scores)
    lowest = min(scores)
    print(lowest)
    scores.remove(lowest)
    print("modified: ", scores)
    ave = sum(scores)/ len(scores)
    print("Average: ", ave)
    

main()
