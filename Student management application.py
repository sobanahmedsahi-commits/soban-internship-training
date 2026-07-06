class Student:
    def __init__(self, roll_no, name, age, grade):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.grade = grade

    def display(self):
        print(f"Roll No: {self.roll_no}, Name: {self.name}, Age: {self.age}, Grade: {self.grade}")


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, roll_no, name, age, grade):
        for s in self.students:
            if s.roll_no == roll_no:
                print("Student with this roll number already exists.")
                return
        student = Student(roll_no, name, age, grade)
        self.students.append(student)
        print("Student added successfully.")

    def remove_student(self, roll_no):
        for s in self.students:
            if s.roll_no == roll_no:
                self.students.remove(s)
                print("Student removed successfully.")
                return
        print("Student not found.")

    def update_student(self, roll_no, name=None, age=None, grade=None):
        for s in self.students:
            if s.roll_no == roll_no:
                if name:
                    s.name = name
                if age:
                    s.age = age
                if grade:
                    s.grade = grade
                print("Student updated successfully.")
                return
        print("Student not found.")

    def search_student(self, roll_no):
        for s in self.students:
            if s.roll_no == roll_no:
                s.display()
                return
        print("Student not found.")

    def show_all(self):
        if not self.students:
            print("No students found.")
            return
        for s in self.students:
            s.display()


def main():
    manager = StudentManager()

    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Update Student")
        print("4. Search Student")
        print("5. Show All Students")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            roll_no = input("Enter roll number: ")
            name = input("Enter name: ")
            age = input("Enter age: ")
            grade = input("Enter grade: ")
            manager.add_student(roll_no, name, age, grade)

        elif choice == "2":
            roll_no = input("Enter roll number: ")
            manager.remove_student(roll_no)

        elif choice == "3":
            roll_no = input("Enter roll number: ")
            name = input("Enter new name (leave blank to skip): ")
            age = input("Enter new age (leave blank to skip): ")
            grade = input("Enter new grade (leave blank to skip): ")
            manager.update_student(roll_no, name or None, age or None, grade or None)

        elif choice == "4":
            roll_no = input("Enter roll number: ")
            manager.search_student(roll_no)

        elif choice == "5":
            manager.show_all()

        elif choice == "6":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
