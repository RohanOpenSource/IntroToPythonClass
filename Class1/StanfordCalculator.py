# English, Math, Science, and History
english_grade = int(input("What is your english grade? "))
math_grade = int(input("What is your math grade? "))
science_grade = int(input("What is your science grade? "))
history_grade = int(input("What is your history grade? "))

#Grade Point *Average*

gpa = (english_grade + math_grade + science_grade + history_grade) / 4

print("your gpa is " + str(gpa))

#Are you eligable for stanford?

good_student = bool(input("Are you a good student(answer in True or False) "))

num_extracurriculars = int(input("How many extracurriculars do you have? "))

volunteer_hours = int(input("How many volunteer hours have you collected? "))

can_go_to_stanford = (gpa >= 5) and good_student and (num_extracurriculars >= 20) and (volunteer_hours >= 500)

print("You are eligable to go to Stanford: " + str(can_go_to_stanford))
