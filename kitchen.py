class Kitchen():

    @staticmethod
    def drink_coffee(person):
        person.energy_level += 20
        print(person.first_name + " " + person.last_name + "'s energy level increased to " + str(person.energy_level))


    @staticmethod
    def eat(person):
        person.hunger_level -= 30
        print(person.first_name + " " + person.last_name + "'s hunger level decreased to " + str(person.hunger_level))


    @staticmethod
    def random_talk(person):
        person.social_life += 15
        print(person.first_name + " " + person.last_name + "'s Social Life level increased to " + str(person.social_life))