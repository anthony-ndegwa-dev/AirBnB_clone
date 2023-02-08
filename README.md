# AirBnB_clone

Description:

	Creating a clone of AirBnB web application by first creating a basic console using Cmd Python module, making it possible to implement methods show, create, update and destroy to the existing classes and subclasses.


Environment:

	The console was developed on Ubuntu 20.04


Requirements:

	Experience in python3, be able to use a command line interpreter, Ubuntu 20.04, python3 and pep8 style corrector.


Starting Command Interpreter:

	Clone the repository and run console.py


Usage:

	Commands 	Description
	=======================================================================
	create 		Creates object of given class
	show 		Prints the string representation of an instance based on the class name and id
	all 		Prints all string representation of all instances based or not on the class name
	update 		Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)
	destroy 	Deletes an instance based on the class name and id (save the change into the JSON file)
	count 		Retrieve the number of instances of a class
	help 		Prints information about specific command
	quit/ EOF 	Exit the program


Example 1:

	root@911a86503c1e:~/AirBnB_clone# ./console.py
	(hbnb) create User                                                
	e9ab8ab9-c6a7-4dba-b5ff-eb5d84b59fdd                                                        
	(hbnb) create User                                                          
	e9ab8ab9-c6a7-4dba-b5ff-eb5d84b59fdd
	(hbnb) show User e9ab8ab9-c6a7-4dba-b5ff-eb5d84b59fdd
	[User] (e9ab8ab9-c6a7-4dba-b5ff-eb5d84b59fdd) {'id': 'e9ab8ab9-c6a7-4dba-b5ff-eb5d84b59fdd', 'created_at': datetime.datetime(2023, 2, 8, 8, 19, 41, 642322), 'updated_at': datetime.datetime(2023, 2, 8, 8, 19, 41, 642370)}
	(hbnb) all User
	["[User] (e9ab8ab9-c6a7-4dba-b5ff-eb5d84b59fdd) {'id': 'e9ab8ab9-c6a7-4dba-b5ff-eb5d84b59fdd', 'created_at': datetime.datetime(2023, 2, 8, 8, 19, 41, 642322), 'updated_at': datetime.datetime(2023, 2, 8, 8, 19, 41, 642370)}"]
	(hbnb) all User
	["[User] (e9ab8ab9-c6a7-4dba-b5ff-eb5d84b59fdd) {'id': 'e9ab8ab9-c6a7-4dba-b5ff-eb5d84b59fdd', 'created_at': datetime.datetime(2023, 2, 8, 8, 19, 41, 642322), 'updated_at': datetime.datetime(2023, 2, 8, 8, 19, 41, 642370)}"]
	(hbnb) show User
	** instance id missing **


Example 2:

	root@911a86503c1e:~/AirBnB_clone# ./console.py
	(hbnb) create User                                                
	e9ab8ab9-c6a7-4dba-b5ff-eb5d84b59fdd
	(hbnb)
	root@911a86503c1e:~/AirBnB_clone# ./console.py
	(hbnb) create User
	e9ab8ab9-c6a7-4dba-b5ff-eb5d84b59fdd
	(hbnb) show User e9ab8ab9-c6a7-4dba-b5ff-eb5d84b59fdd
	[User] (e9ab8ab9-c6a7-4dba-b5ff-eb5d84b59fdd) {'id': 'e9ab8ab9-c6a7-4dba-b5ff-eb5d84b59fdd', 'created_at': datetime.datetime(2023, 2, 8, 8, 19, 41, 642322), 'updated_at': datetime.datetime(2023, 2, 8, 8, 19, 41, 642370)}
	(hbnb) all User
	["[User] (e9ab8ab9-c6a7-4dba-b5ff-eb5d84b59fdd) {'id': 'e9ab8ab9-c6a7-4dba-b5ff-eb5d84b59fdd', 'created_at': datetime.datetime(2023, 2, 8, 8, 19, 41, 642322), 'updated_at': datetime.datetime(2023, 2, 8, 8, 19, 41, 642370)}"]
	(hbnb) all User
	["[User] (e9ab8ab9-c6a7-4dba-b5ff-eb5d84b59fdd) {'id': 'e9ab8ab9-c6a7-4dba-b5ff-eb5d84b59fdd', 'created_at': datetime.datetime(2023, 2, 8, 8, 19, 41, 642322), 'updated_at': datetime.datetime(2023, 2, 8, 8, 19, 41, 642370)}"]
	(hbnb) show User
	** instance id missing **
