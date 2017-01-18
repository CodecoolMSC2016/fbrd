import csv
from person import Person


class Mentor(Person):

    def __init__(self, first_name, last_name, year_of_birth, gender, energy_level, social_life, mentor_name):
        super().__init__(first_name, last_name, year_of_birth,
                         gender, energy_level, social_life)
        self.mentor_name = mentor_name

    def do_presentation(self, students_object_list):
        for student in students_object_list:
            student.energy_level -= 30
            student.knowledge_level += 15
            self.energy_level -= 20

    @classmethod
    def create_by_csv(cls):
        with open('data/mentors.csv') as csvfile:
            mentors_list = []
            data = csv.reader(csvfile)
            for mentor_row_raw_data in data:
                first_name, last_name, year_of_birth, gender, energy_level, social_life, mentor_name = mentor_row_raw_data
                mentors_list.append(Mentor(first_name, last_name, int(
                    year_of_birth), gender, int(energy_level), int(social_life), mentor_name))
        return mentors_list
