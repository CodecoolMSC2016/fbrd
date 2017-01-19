from person import Person
import csv


class Student(Person):

    FIRST_NAME = 0
    LAST_NAME = 1
    BIRTH = 2
    GENDER = 3
    ENERGY = 4
    SOCIAL = 5
    DARTS_SK = 6
    PS_SK = 7
    HUNGER = 8
    BA_LEV = 9

    def __init__(self, first_name, last_name, year_of_birth, gender, energy_level=75,
                 social_life=20, darts_skill_level=0, playstation_skill_level=0,
                 hunger_level=0, blood_alcohol_level=0, knowledge_level=20):
        super().__init__(first_name, last_name, year_of_birth, gender, energy_level,
                         social_life, darts_skill_level, playstation_skill_level, hunger_level, blood_alcohol_level)
        self.knowledge_level = knowledge_level

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
                                   cls.BIRTH]), students[entry][cls.GENDER], int(students[entry][cls.ENERGY]), int(students[entry][cls.SOCIAL]),
                int(students[entry][cls.DARTS_SK]), int(
                    students[entry][cls.PS_SK]), int(students[entry][cls.HUNGER]),
                int(students[entry][cls.BA_LEV])))

        return student_objects
