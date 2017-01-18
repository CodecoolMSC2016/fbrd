class Lounge:

    def __init__(self, darts_Skill_level, playstation_skill_level):
        self.darts_skill_level = darts_Skill_level
        self.playstation_skill_level = playstation_skill_level

    def play(self, game_name, time_spent):
        if game_name == "darts":
            self.darts_skill_level += 5 * time_spent
        elif game_name == "playstation":
            self.playstation_skill_level += 5 * time_spent
        else:
            pass
            # throw error

    @staticmethod
    def nap_in_bean_bags(person, time_spent):
        person.energy_level += 2 * time_spent

    @staticmethod
    def watch_random_video_on_tv(person, time_spent):
        person.energy_level += 1 * time_spent
        person.social_life += 2 * time_spent
