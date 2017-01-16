#Person

##the class' parent class (if any)
None

##the class' description
 This class represents a Person in real life, 
 but we only use it to inherit it's features in Student and Mentor classes.

##attributes
* `first_name`
    * **date type:** string
    * **description:** first name of the person
* `last_name`
    * **date type:** string
    * **description:** last name of the person
* `year_of_birth`
    * **date type:** integer
    * **description:** Birth year of the person
* `gender`
    * **date type:** string
    * **description:** should be male/female/notsure

##instance methods 
* `__init___`
    * **arguments:** first_name, last_name, year_of_birth, gender
    * **description:** gets all the attributes above. It should raise an error, 
    if any of the attributes is empty, and also if the provide gender is not valid