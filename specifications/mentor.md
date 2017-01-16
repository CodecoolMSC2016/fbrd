#Mentor

##the class' parent class (if any)
* Person

##the class' description
This class represents a mentor in real life.

##attributes
* `nickname`
    * **date type:** string
    * **description:** stores the mentor's secret nickname between the students

##instance methods 
* `__init___`
    * **arguments:** mentor_name
    * **description:** calls the Person's constructor, but also set's the nickname attribute 
    (should raise an error, if empty).

* `create_by_csv`
    * **argument:** file_path
    * **return:** list_of_mentors
    * **description:** gets a csv file path as an argument 
    (the csv contains all the data needed to instantiate a mentor object) 
    and gives back a list of mentors.