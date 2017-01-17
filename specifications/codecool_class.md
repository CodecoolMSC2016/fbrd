#Codecool class

##the class' parent class (if any)
* Mentor
* Student

##the class' description
This class represents a class in real life.

##attributes
* `location`
    * **date type:** string
    * **description:** stores the location of the class
* `year`
    * **date type:** integer
    * **description:** year of the class start
* `mentors`
    * **date type:** list
    * **description:** contain mentor objects
* `students`
    * **date type:** list
    * **description:** contain student objects

##instance methods 
* `__init___`
    * **arguments:** location, year, mentors, students
    * **description:** calls the Person's constructor, but also set's the nickname attribute 
    (should raise an error, if empty).
    
*  `find_mentor_by_full_name`
    * **arguments:** full_name
    * **description:** give back a mentor by it's full_name

*  `find_student_by_full_name`
    * **arguments:** full_name
    * **description:** give back a student by it's full_name

* `generate_local`
    * **argument:** None
    * **return:** CodecoolClass object stroring some localized data in it's attributes
    * **description:** A CodecoolClass object can give back a mentor/student by it's full_name 
    (given as an argument) with the find_mentor_by_full_name and find_student_by_full_name methods.