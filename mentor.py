import csv
from person import Person


class Mentor(Person):

    def __init__(self, first_name, last_name, year_of_birth, gender, energy_level = 75, social_life = 20,
                 darts_skill_level = 0, playstation_skill_level = 0, hunger_level = 0, blood_alcohol_level = 0,
                 mentor_name = ""):
        super().__init__(first_name, last_name, year_of_birth, gender, energy_level,
                 social_life, darts_skill_level, playstation_skill_level, hunger_level, blood_alcohol_level)
        self.mentor_name = mentor_name

    @staticmethod
    def do_presentation(person):
            person.energy_level -= 30
            print(person.first_name + " " + person.last_name + "'s energy level decreased to " + str(person.energy_level))
            person.knowledge_level += 15
            print(person.first_name + " " + person.last_name + "'s knowledge level increased to " + str(person.knowledge_level))

    @classmethod
    def create_by_csv(cls):
        print("Generating mentors object list from CSV file.")
        with open('data/mentors.csv') as csvfile:
            mentors_obj_list = []
            data = csv.reader(csvfile)
            for mentor_row_raw_data in data:
                first_name, last_name, year_of_birth, gender, energy_level, \
                social_life, darts_skill_level, playstation_skill_level, hunger_level, blood_alcohol_level, mentor_name = mentor_row_raw_data

                mentors_obj_list.append(Mentor(first_name, last_name, int(year_of_birth), gender, int(energy_level),
                                           int(social_life), int(darts_skill_level), int(playstation_skill_level), int(hunger_level),
                                           int(blood_alcohol_level), mentor_name))
        return mentors_obj_list
