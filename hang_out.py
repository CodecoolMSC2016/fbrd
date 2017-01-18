class Hangout:

    def __init__(participants, blood_alcohol_level, money_spent):
        self.participants = participants
        self.blood_alcohol_level = blood_alcohol_level
        self.money_spent = money_spent

    def buy_a_round_of_shot(self, cost_per_shot):

        if self.money_spent <= 2000:
            if self.blood_alcohol_level < 20:
                for participant in self.participants:
                    participant.social_life += 10

                self.blood_alcohol_level += 10
                self.money_spent += cost_per_shot * len(self.participants)

            else:
                print("Everybody is drunk as fuck, lets puke, and start over again!")
                print("Blooooooah!!-.")
                self.blood_alcohol_level -= 10
        else:
            print("We're poor as the mice of the church...")
