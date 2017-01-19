class MentorsRoom:

    def __init__(self):
        self.bfa_status = None

    def do_a_bfa(self, person):
        person.energy_level -= 20
        self.bfa_status = True

    @staticmethod
    def do_a_meeting(person):
        person.energy_level -= 10
