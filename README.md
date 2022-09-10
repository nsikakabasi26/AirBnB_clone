cription í¿  AirBnB is a complete web application, integrating database storage, a back-end API, and front-end interfacing in a clone of AirBnB.

The project currently only implements the back-end console.

Classes í¶‘ AirBnB utilizes the following classes:

BaseModel FileStorage User State City Amenity Place Review PUBLIC INSTANCE ATTRIBUTES id created_at updated_at Inherits from BaseModel Inherits from BaseModel Inherits from BaseModel Inherits from BaseModel Inherits from BaseModel Inherits from BaseModel PUBLIC INSTANCE METHODS save to_dict all new save reload "" "" "" "" "" "" PUBLIC CLASS ATTRIBUTES email password first_name last_name name state_id name name city_id user_id name description number_rooms number_bathrooms max_guest price_by_night latitude longitude amenity_ids place_id user_id text PRIVATE CLASS ATTRIBUTES file_path objects Storage í»„ The above classes are handled by the abstracted storage engine defined in the FileStorage class.

Every time the backend is initialized, AirBnB instantiates an instance of FileStorage called storage. The storage object is loaded/re-loaded from any class instances stored in the JSON file file.json. As class instances are created, updated, or deleted, the storage object is used to register corresponding changes in the file.json.

Console í²» The console is a command line interpreter that permits management of the backend of AirBnB. It can be used to handle and manipulate all classes utilized by the application (achieved by calls on the storage object defined above).

Using the Console The AirBnB console can be run both interactively and non-interactively. To run the console in non-interactive mode, pipe any command(s) into an execution of the file console.py at the command line.

$ echo "help" | ./console.py CONCEPTS LEARNT How to create a Python package How to create a command interpreter in Python using the cmd module What is Unit testing and how to implement it in a large project How to serialize and deserialize a Class How to write and read a JSON file How to manage datetime What is an UUID What is *args and how to use it What is **kwargs and how to use it How to handle named arguments in a function SYNOPSIS Starting the Commandline Interpreter The Commandline Interpreter can be started by executing the command ./console.py. The console can create, destroy, and update objects. Type help within the console to get a list of command options and its function.

Example:

firdaus@ubuntu:~$ ./console.py (hbnb) help

Documented commands (type help ):
EOF create help quit

Undocumented commands:
all destroy show update

(hbnb) help quit Quit command to exit the program (hbnb) quit firdaus@ubuntu:~$ OBJECTS IMPLEMENTED This repository contains the following files:

Folder File Description tests Contains test files for AirBnb Clone console.py Command line Interpreter for managing AirBnB objects models base_model.py Defines all common attributes/methods for other classes models amenity.py Creates class amenity models city.py Creates class city models place.py Creates class place models review.py Creates class review models state.py Creates class state models user.py Creates class user models/engine/ file_storage.py Serializes instances to a JSON file and deserializes JSON file to instances To be updated

AUTHORS: Ayomide Soniyi , Eze Samuel
