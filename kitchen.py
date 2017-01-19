class Kitchen():

    @staticmethod
    def drink_coffee(person):
        person.energy_level += 20

    @staticmethod
    def eat(person):
        person.hunger_level += 30

    @staticmethod
    def random_talk(person):
        person.social_life += 15