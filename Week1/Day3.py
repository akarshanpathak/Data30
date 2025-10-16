# Create a dictionary with student names as keys and marks as values
students = {
    "Akarshan": 98,
    "Riya": 92,
    "Aditya": 79,
    "Neha": 95,
    "Rahul": 85
}


top_student = max(students, key=students.get)


print("Student with the highest marks is:", top_student)
