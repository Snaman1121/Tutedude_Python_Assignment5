# Task 1: Student Marks Dictionary

# 1. Creates a dictionary where student names are keys and marks are values
student_marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 95
}

# 2. Asks the user to input a student's name
search_name = input("Enter the student's name: ")

# 3. Retrieves and displays the corresponding marks

if search_name in student_marks:
    print(f"{search_name}'s marks: {student_marks[search_name]}")
# 4. If the name is not found, display an appropriate message
else:
    print("Student not found.")