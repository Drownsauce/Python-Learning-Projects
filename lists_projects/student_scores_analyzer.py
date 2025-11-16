#Travis Delcambre
#I know it's more OOP than list but, its just better this way
#keeps track of each student name and grades with methods to manipulate each student object
class Student:
    def __init__(self, name, grades=None):
        self.name = name
        self.grades = grades if grades else []

    def add_grades(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

    def highest_score(self):
        return max(self.grades)

    def lowest_score(self):
        return min(self.grades)

    def __str__(self):
        return f"[{self.name}] Grades: {self.grades}"

#Classroom class that controls all student objects and methods to display and add / remove student objects
class Classroom:
    def __init__(self, students=None):
        self.students = students if students else []

    def get_student(self, name):
        for student in self.students:
            if student.name == name:
                return student
        return None

    def view_students(self):
        for student in self.students:
            print(student)

    def add_student(self, name, grades=None):
        self.students.append(Student(name, grades))
        print(self.students)

    def remove_student(self, name):
        student = self.get_student(name)
        if student:
            self.students.remove(student)

    def filter_students(self, grade):
        filtered_students = [student for student in self.students if student.average_grade() >= grade]
        return filtered_students

    def students_stats(self):
        for student in self.students:
            print(f"([{student.name}] grade average: {student.average_grade():.2f} highest score: {student.highest_score()} lowest score: {student.lowest_score()})")

#Main code just controls the interface and user_choice
classroom = Classroom()
while True:
    try:
        user_choice = int(input("Enter option:\n(1. Add Student / 2. Add Grade / 3. View Students / 4. Filter grades / 5. Remove Student / 6. Grade Stats)\n>"))
    except ValueError:
        print("Must be an integer!")
        continue

    match user_choice:
        case 1:
            student_name = input("Student name: ").strip().lower()
            classroom.add_student(student_name)
        case 2:
            while True:
                student_name = input("Student name: ").strip().lower()
                try:
                    student_obj = classroom.get_student(student_name)
                    break
                except Exception as err:
                    print(err)
            if student_obj:
                while True:
                    grade_input = float(input("(-1 to stop) Enter grade: "))
                    if grade_input == -1:
                        break

                    student_obj.add_grades(grade_input)
        case 3:
            classroom.view_students()
        case 4:
            while True:
                try:
                    grade_filter = float(input("Grade score to filter by: "))
                    break
                except ValueError:
                    print("Must be a number!")

            grade_filtered_students = classroom.filter_students(grade_filter)
            for filtered_student in grade_filtered_students:
                print(filtered_student)
        case 5:
            student_name = input("Student name: ").strip().lower()
            classroom.remove_student(student_name)
        case 6:
            classroom.students_stats()
        case _:
            break