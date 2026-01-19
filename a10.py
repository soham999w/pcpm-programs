# Write a Python program to input marks of 5 subjects and calculate total, percentage, and grade.
marks = []
for i in range(1, 6):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)
total = sum(marks)
percentage = (total / 500) * 100   
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"
print("\nTotal Marks:", total)
print("Percentage:", percentage, "%")
print("Grade:", grade)
