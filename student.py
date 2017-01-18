from person import Person
import csv


class Student(Person):

    FIRST_NAME = 0
    LAST_NAME = 1
    BIRTH = 2
    GENDER = 3
    ENERGY = 4
    SOCIAL = 5

    def __init__(self, first_name, last_name, year_of_birth, gender, energy_level, social_life, knowledge_level=50):
        super().__init__(first_name, last_name, year_of_birth,
                         gender, energy_level, social_life)

    @classmethod
    def create_by_csv(cls):
        students = list()
        student_objects = list()

        with open("data/students.csv", "r") as students_db:
            reader = csv.reader(students_db, delimiter='\t')
            for row in reader:
                students.append(row[0].split())

        for entry in range(len(students)):
            student_objects.append(Student(students[entry][cls.FIRST_NAME], students[entry][cls.LAST_NAME], int(students[entry][
                                   cls.BIRTH]), students[entry][cls.GENDER], int(students[entry][cls.ENERGY]), int(students[entry][cls.SOCIAL])))

        return student_objects
