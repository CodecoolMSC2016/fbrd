#Person

##the class' parent class (if any)
None

##the class' description
 This class represents a Person in real life, 
 but we only use it to inherit it's features in Student and Mentor classes.

##attributes
* `first_name`
    * **dataq type:** string
    * **description:** first name of the person
* `last_name`
    * **data type:** string
    * **description:** last name of the person
* `year_of_birth`
    * **data type:** integer
    * **description:** Birth year of the person
* `gender`
    * **data type:** string
    * **description:** should be male/female/notsure
* `hunger_level`
    * **data type:** int
    * **description:** current hunger level
* `energy_level`
    * **data type:** integer
    * **description:** current energy level
* `social_life`
    * **data type:** integer
    * **description:** current social life level
* `darts_skill_level`
    * **data type:** integer
    * **description:** current darts skill level
* `playstation_skill_level`
    * **data type:** integer
    * **description:** current ps skill level
* `blood_alcohol_level`
    * **data type:** integer
    * **description:** blood alcohol level

##instance methods 
* `__init___`
    * **arguments:** first_name, last_name, year_of_birth, gender
    * **description:** gets all the attributes above. It should raise an error, 
    if any of the attributes is empty, and also if the provide gender is not valid

* `regenerate`
    * **arguments:** None
    * **description:** if the blood alcohol level exceds 50, the person pukes, sets back alcohol level a little