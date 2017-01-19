from codecool_class import CodecoolClass
from mentor import Mentor
from student import Student
from mentors_room import MentorsRoom
from lounge import Lounge
from kitchen import Kitchen
from hang_out import Hangout
import time
import os
from asci import *
import random

codecool_msc = CodecoolClass.generate_local()
students = codecool_msc.students
mentors = codecool_msc.mentors
kitchen = Kitchen()
mentors_room = MentorsRoom()
hangouts = Hangout(0)
date = time.strftime("%Y/%m/%d")


def wake_up():
    os.system("clear")
    print(date)
    print("*Alarm clock buzzing*")  # todo blinking shjit
    time.sleep(2)
    print("Not this shit again...")
    time.sleep(1.5)
    print("*Loud yawning*")
    print("Just five more minutes..")
    ascii_later()
    print("Time to take a shower..")
    time.sleep(2)
    print("*Water splashing*")
    print("*Singing some backstreet boys miserably*")
    time.sleep(3.5)
    print("Time to dress up, and go to CodeCool..")
    ascii_at_codecool()


def go_to_kitchen():
    print("Good morning boii, what's up?")
    time.sleep(2)
    print("{} {} says: {}".format(students[0].first_name, students[
          0].last_name, "Mornin', nothing much. U?\n"))
    time.sleep(2)
    print("I still feel tired. (Energy level: {}) ".format(
        mentors[0].energy_level))
    time.sleep(2)
    print("{} {} says: {}\n".format(students[0].first_name, students[
          0].last_name, "I'm tired too, lets drink a coffe! (Energy Level:{})".format(students[0].energy_level)))
    time.sleep(1)
    print("*Slurp*\n")

    kitchen.drink_coffee(students[0])
    time.sleep(1)
    kitchen.drink_coffee(mentors[0])
    time.sleep(1)
    print("\n*random bullshit talk*\n")
    time.sleep(1)
    kitchen.random_talk(students[0])
    time.sleep(1)
    kitchen.random_talk(mentors[0])
    ascii_time()
    print("Oh, its 9 o' clock already, we need to go to the classroom!")
    time.sleep(1)


def classroom():
    print("I see everybody's here, great!")
    time.sleep(1)
    print("So, welcome folks, today i'll do a presentation about gitHub, and version control...")
    ascii_eternity()

    for student in students:
        mentors[0].do_presentation(student)
        time.sleep(0.5)
        print("\n")

    mentors[0].energy_level -= 20
    print(mentors[0].first_name + " " + mentors[0].last_name +
          "'s energy level decreased to " + str(mentors[0].energy_level))


def bfa():
    ascii_later()
    m_room = MentorsRoom()
    bfa_student = students[random.randint(0, len(students) - 1)]
    print("Sigh, there is a leftover bfa i need to do.")
    print("{} {} come with me to the mentors room please!".format(
        bfa_student.first_name, bfa_student.last_name))
    m_room.do_a_bfa(bfa_student)
    print("{} {}'s BFA succeeded: {}".format(
        bfa_student.first_name, bfa_student.last_name, m_room.bfa_status))
    ascii_time()


def eat():
    mentors[0].hunger_level = 80
    print(mentors[0].first_name + " " + mentors[0].last_name +
          "'s hunger level increased to: " + str(mentors[0].hunger_level) + "\n")
    time.sleep(1)
    print("Better go eat something.\n")
    time.sleep(1)
    print("*Nom Nom*\n")
    time.sleep(2)
    kitchen.eat(mentors[0])
    kitchen.eat(students[2])
    print("*random bullshit talk*\n")
    time.sleep(1)
    kitchen.random_talk(students[2])
    time.sleep(1)
    kitchen.random_talk(mentors[0])
    ascii_later()


def rest():
    time.sleep(1)
    print(mentors[0].first_name + " " + mentors[0].last_name +
          "'s energy level decreased to " + str(mentors[0].energy_level))
    print("I should rest a little.")
    lounge = Lounge()
    ascii_later()
    print("I take a nap in the beanbags at the lounge...\n")
    lounge.nap_in_bean_bags(mentors[0], 5)
    print(mentors[0].first_name + " " + mentors[0].last_name +
          "'s energy level increased to " + str(mentors[0].energy_level) + "\n")
    time.sleep(1)
    print("Lets play some darts! \n")
    lounge.play(mentors[0], "darts", 5)
    time.sleep(1)
    print(mentors[0].first_name + " " + mentors[0].last_name +
          "'s darts skill increased to " + str(mentors[0].darts_skill_level))
    print("Lets watch some DANK Meme videos on YouTube!")
    time.sleep(1)
    lounge.watch_random_video_on_tv(mentors[0], 2)
    print(mentors[0].first_name + " " + mentors[0].last_name +
          "'s energy level increased to " + str(mentors[0].energy_level) + "\n")
    print("Oh noes, there will be a meeting soon!")


def meeting():
    ascii_later()
    print("Entering meeting room...\n")
    time.sleep(1)
    print("So lets talk about why we bought the Brewie machine for 1690$")
    ascii_eternity()
    print("We couldn't found the asnwer for our main meeting question.. or maybe for ...?!  ")
    mentors_room.do_a_meeting(mentors[0])
    ascii_dotdotdot()
    ascii_later()
    mentors_room.do_a_meeting(mentors[0])
    print(mentors[0].first_name + " " + mentors[0].last_name +
          "'s energy level decreased to " + str(mentors[0].energy_level))
    time.sleep(1)
    print("The day is almost over, I should hang out somewhere...")
    input(">")

def hangout():
    os.system("clear")
    print("Arriving at Paprika, our Codecool drink base\n")
    time.sleep(2)
    print("Hmm, many many Codecooler here.. it is going to be a long and expensive night...")
    time.sleep(1)
    print("But whatever, lets #Yolo this night!\n")
    print("The first round on me")
    time.sleep(3)
    hangouts.buy_a_round_of_shot(mentors[0],470,len(students))
    time.sleep(2)
    print("Nah, lets drink it guys!")
    time.sleep(1)
    print("\n < place deformed face here >\n")
    print("uhh, yeeeeAAHH")
    time.sleep(4)
    print("Lets do another, it was like water for me.")
    hangouts.buy_a_round_of_shot(mentors[0],470,len(students))
    time.sleep(2)
    print("There they are... = )")
    time.sleep(0.5)
    print("The last one, buys the next round!")
    ascii_dotdotdot()
    os.system("clear")
    print("*Alarm clock buzzing*")
    time.sleep(2)
    print("No, not this shit again...")


def main():
    # wake_up()
    # go_to_kitchen()
    # classroom()
    # eat()
    # rest()
    # meeting()
    hangout()


if __name__ == "__main__":
    main()
