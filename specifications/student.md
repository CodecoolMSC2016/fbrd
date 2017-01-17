#Student

##the class' parent class (if any)
* Person

##the class' description
This class represents a student in real life.

##attributes
* `knowledge_level`
    * **date type:** integer
    * **description:** stores the knowledge level of the student in programming

##instance methods 
* `__init___`
    * **arguments:** knowledge_level
    * **description:** calls the Person's constructor, but also set's the attributes above 
    (should raise an error, if any is empty).

* `create_by_csv`
    * **argument:** file_path
    * **return:** list_of_students
    * **description:** gets a csv file path as an argument 
    (the csv contains all the data needed to instantiate a student object) 
    and gives back a list of students.