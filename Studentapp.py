# Simple Student Record Management System

students = []  # This will be a list of dictionaries

def add_student():
    name = input("Enter student's name: ")
    age = int(input("Enter age: "))
    subjects = input("Enter subjects (comma-separated): ").split(",")
    marks = float(input("Enter average marks: "))

    student = {
        "name": name,
        "age": age,
        "subjects": tuple(subject.strip() for subject in subjects),  # tuple
        "marks": marks
    }

    students.append(student)
    print("Student added successfully!\n")

def view_students():
    if not students:
        print("No student records found.\n")
        return

    for index, student in enumerate(students, start=1):
        print(f"{index}. Name: {student['name']}, Age: {student['age']}, Marks: {student['marks']}")
        print(f"   Subjects: {', '.join(student['subjects'])}")
    print()

def search_student():
    search_name = input("Enter student name to search: ")
    found = False
    for student in students:
        if student["name"].lower() == search_name.lower():
            print(f"Found: {student}")
            found = True
            break
    if not found:
        print("Student not found.\n")

def show_unique_subjects():
    subject_set = set()
    for student in students:
        subject_set.update(student["subjects"])

    print(f"All unique subjects: {subject_set}\n")
import numpy     

def main():
    while True:
        print("=== Student Record Menu  BY . AHMAD SANDHU ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Show Unique Subjects")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            show_unique_subjects()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
