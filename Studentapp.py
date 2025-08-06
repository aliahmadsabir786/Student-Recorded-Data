students = []

def add_student():
    Name = input("Enter a Name: ")
    Age = int(input("Enter an age: "))
    Subject = input("Enter subjects (comma separated): ").split(",")
    Marks = float(input("Enter marks: "))

    student = {
        "name": Name,
        "age": Age,
        "subject": tuple(sub.strip() for sub in Subject),
        "marks": Marks
    }

    students.append(student)
    print("Student added successfully.\n")


def view_student():
    if not students:
        print("No student found!\n")
        return

    for index, student in enumerate(students, start=1):
        print(f"{index}. Name: {student['name']}, Age: {student['age']}, Marks: {student['marks']}")
        print(f"   Subjects: {', '.join(student['subject'])}")
    print()


def search_students():
    search_name = input("Enter a name to search: ")
    found = False
    for student in students:
        if student["name"].lower() == search_name.lower():
            print(f"Found: {student}\n")
            found = True
            break
    if not found:
        print("Student not found.\n")


def search_unique_subject():
    subject_set = set()
    for student in students:
        subject_set.update(student["subject"])
    print(f"All unique subjects: {subject_set}\n")


def del_student():
    if not students:
        print("There is no student record.\n")
        return

    name_to_delete = input("Enter the student name to delete: ").strip()
    for i, student in enumerate(students):
        if student["name"].lower() == name_to_delete.lower():
            print(f"Found student record: {student}")
            confirm = input("Are you sure you want to delete this record? (yes/no): ").strip().lower()
            if confirm == "yes":
                del students[i]
                print("Student record deleted successfully.\n")
            else:
                print("Deletion cancelled.\n")
            return  # Exit after processing
    print("Student record not found.\n")


def main():
    while True:
        print("=== Student Record Menu BY AHMAD SANDHU ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Show Unique Subjects")
        print("5. Delete Student Record")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_student()
        elif choice == "3":
            search_students()
        elif choice == "4":
            search_unique_subject()
        elif choice == "5":
            del_student()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
