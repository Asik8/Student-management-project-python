class Student:
    def __init__(self, name, gender, id_number, blood_group, mobile_number, email):
        """
        Constructor for the Student class
        """
        self._name = name
        self._gender = gender
        self._id_number = id_number
        self._blood_group = blood_group
        self._mobile_number = mobile_number
        self._email = email

    def display(self):
        """
        Method to display student information
        """
        print("Name:", self._name)
        print("Gender:", self._gender)
        print("ID Number:", self._id_number)
        print("Blood Group:", self._blood_group)
        print("Mobile Number:", self._mobile_number)
        print("Email:", self._email)


class StudentSystem:
    def __init__(self):
        """
        Constructor for the StudentSystem class
        """
        self._students = []

    def add_student(self, student):
        """
        Method to add a student to the system
        """
        self._students.append(student)

    def delete_student(self, id_number):
        """
        Method to delete a student from the system
        """
        for student in self._students:
            if student._id_number == id_number:
                self._students.remove(student)
                return True
        return False

    def modify_student(self, id_number, **kwargs):
        """
        Method to modify a student's information
        """
        for student in self._students:
            if student._id_number == id_number:
                for key, value in kwargs.items():
                    setattr(student, "_" + key, value)
                return True
        return False

    def display_students(self):
        """
        Method to display the list of students in the system
        """
        if not self._students:
            print("No students in the system.")
        else:
            for student in self._students:
                student.display()

    def search_student(self, id_number):
        """
        Method to search for a student by ID number and display their information
        """
        for student in self._students:
            if student._id_number == id_number:
                student.display()
                return
        print("Student not found.")


def main():
    """
    Main function to run the Student Information System
    """
    system = StudentSystem()

    while True:
        print("\nStudent Information System\n")
        print("1. Add student")
        print("2. Delete student")
        print("3. Modify student")
        print("4. Display student list")
        print("5. Search student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            gender = input("Enter gender: ")
            id_number = input("Enter ID number: ")
            blood_group = input("Enter blood group: ")
            mobile_number = input("Enter mobile number: ")
            email = input("Enter email: ")
            student = Student(name, gender, id_number, blood_group, mobile_number, email)
            system.add_student(student)
            print("Student added successfully.")

        elif choice == "2":
            id_number = input("Enter ID number of student to delete: ")
            if system.delete_student(id_number):
                print("Student deleted successfully.")
            else:
                print("Student not found.")

        elif choice == "3":
            id_number = input("Enter ID number of student to modify: ")
            attribute = input("Enter attribute to modify (name/gender/blood_group/mobile_number/email): ")

            # Validating attribute input
            valid_attributes = ["name", "gender", "blood_group", "mobile_number", "email"]
            if attribute.lower() not in valid_attributes:
                print("Invalid attribute. Please enter a valid attribute.")
                continue

            new_value = input("Enter new value: ")
            if system.modify_student(id_number, **{attribute: new_value}):
                print("Student modified successfully.")
            else:
                print("Student not found.")

        elif choice == "4":
            system.display_students()

        elif choice == "5":
            id_number = input("Enter ID number of student to search: ")
            system.search_student(id_number)

        elif choice == "6":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
