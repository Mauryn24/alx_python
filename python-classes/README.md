*Title*
python - Classes and attributes


*Description*
Classes - blueprints for creating objects
Classes are creaated by using the keyword *class* followed by a colon
For example; class cars:
                x = 5
                x is a property to the class

    
    *creating objects*
Objects are created using the class name. Example; p = cars()
I

    *__init__ function*
-> The __init__() function is called automatically every time the class is being used to create a new object.
-> Inside the class one can initialize the class by using the *__init__* keyword
ie; def __init__ (self, parameters... ) 


    *Object Methods*
Methods are functions that belong to an object


    *instances*


Public instances are accessible from anywhere. They are declared without any special characters.


Private instances are only accessible from within the class that they are defined in. They are declared by prefixing the name of the instance with two underscores (__).


Protected instances are accessible from within the class that they are defined in and from its subclasses. They are declared by prefixing the name of the instance with a single underscore (_).
For example;
class cars:
    def __init__(self, make, year, color):
        self.make = make #public instance
        self.__year = year #private instance
        self._color = "red" #protected instance
