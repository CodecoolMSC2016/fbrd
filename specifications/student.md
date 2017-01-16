#Student

##the class' parent class (if any)
* Person

##the class' description
This class represents a student in real life.

##attributes
* `knowledge_level`
    * **date type:** integer
    * **description:** stores the knowledge level of the student in programming
* `energy_level`
    * **date type:** integer
    * **description:** current energy level

##instance methods 
* `__init___`
    * **arguments:** mentor_name
    * **description:** calls the Person's constructor, but also set's the nickname attribute 
    (should raise an error, if empty).

* `create_by_csv`
    * **argument:** file_path
    * **return:** list_of_mentors
    * **description:** gets a csv file path as an argument 
    (the csv contains all the data needed to instantiate a student object) 
    and gives back a list of students.