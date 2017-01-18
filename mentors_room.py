from student import Student


class MentorsRoom:

    def __init__(self):
        self.bfa_status = None

    def do_a_bfa(self, student):
        student.energy_level -= 20
        self.bfa_status = True

    def do_a_meeting(self, participants):
        for mentor in participants:
            mentor.energy_level -= 20
