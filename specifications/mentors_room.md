#Mentors_room

##the class' parent class (if any)
* Mentor
* Student

##the class' description
* This class represents the mentor room

##attributes
* `bfa_status`
    * **data type:** boolean
    * **description:** stores wether the bfa is succesful or not

##instance methods 
* `do_a_bfa`
    * **arguments:**  student (student object)
    * **returns None** (void)
    * **description:** get a student into doing a bfa, reducing his energy level 

* `do_a_meeting`
    * **arguments:** participants (list storing mentor objects)
    * **returns None** (void) 
    * **description:** arrange a meeting, which decreases the energy level of participants