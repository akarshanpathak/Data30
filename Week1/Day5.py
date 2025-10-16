class Student:
    def __init__(self, name, marks):
        # Initialize the student's name and marks
        self.name = name
        self.marks = marks  # marks should be a list of numbers

    def calculate_average(self):
        # Calculate the average marks
        if len(self.marks) == 0:
            return 0
        return sum(self.marks) / len(self.marks)

# Example usage
student1 = Student("Akarshan", [85, 90, 78, 92, 88])

# Calculate and print average marks
average = student1.calculate_average()
print(f"Average marks of {student1.name}: {average}")
