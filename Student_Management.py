import re

class Student:
    def __init__(self, name, gender, id_number, blood_group, mobile_number, email):
        self._name = name
        self._gender = gender
        self._id_number = id_number
        self._blood_group = blood_group
        self._mobile_number = mobile_number
        self._email = email

    def display(self):
        print("Name:", self._name)
        print("Gender:", self._gender)
        print("ID Number:", self._id_number)
        print("Blood Group:", self._blood_group)
        print("Mobile Number:", self._mobile_number)
        print("Email:", self._email)

    def update_info(self, attribute, value):
        if attribute == 'name':
            self._name = value
        elif attribute == 'gender':
            self._gender = value
        elif attribute == 'blood_group':
            self._blood_group = value
        elif attribute == 'mobile_number':
            if re.match(r'^\d{11}$', value):
                self._mobile_number = value
            else:
                print("Invalid mobile number format.")
        elif attribute == 'email':
            if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', value):
                self._email = value
            else:
                print("Invalid email format.")
        else:
            print("Invalid attribute.")


class StudentSystem:
    def __init__(self):
        self._students = []

    def add_student(self, student):
        self._students.append(student)

    def delete_student(self, id_number):
        for student in self._students:
            if student._id_number == id_number:
                self._students.remove(student)
                return True
        return False

    def modify_student(self, id_number, attribute, value):
        for student in self._students:
            if student._id_number == id_number:
                student.update_info(attribute, value)
                return True
        return False

    def search_student(self, id_number):
        for student in self._students:
            if student._id_number == id_number:
                student.display()
                return
        print("Student not found.")


def main():
    system = StudentSystem()

    while True:
        print("\nStudent Information System\n")
        print("1. Add student")
        print("2. Delete student")
        print("3. Modify student")
        print("4. Search student")
        print("5. Exit")

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
            new_value = input("Enter new value: ")
            if system.modify_student(id_number, attribute, new_value):
                print("Student modified successfully.")
            else:
                print("Student not found.")

        elif choice == "4":
            id_number = input("Enter ID number of student to search: ")
            system.search_student(id_number)

        elif choice == "5":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
