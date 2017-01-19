class Hangout:

    def __init__(self, money_spent):
        self.money_spent = money_spent

    def buy_a_round_of_shot(self,person, cost_per_shot, number_of_shots):

        if self.money_spent <= 2000:
            person.social_life += 10
            person.blood_alcohol_level += 10
            self.money_spent += cost_per_shot * number_of_shots
        else:
            print("We're poor as the mice of the church...")
