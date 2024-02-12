![welcome](https://github.com/Mohabdo21/AirBnB_clone/blob/main/images/image.jpeg?raw=true)

# AirBnB Clone - The Console

## Overview

Welcome to the AirBnB clone project! This is the first step towards building our first full web application. The console created in this project will be used in all other following projects: HTML/CSS templating, database storage, API, front-end integration.

This project is done by the team: Sara Khalid Mustafa and Mohannad Babeker.

## Features

![project stages](https://github.com/Mohabdo21/AirBnB_clone/blob/main/images/process.png?raw=true)

The project has the following features:

- A parent class (BaseModel) that takes care of the initialization, serialization, and deserialization of future instances.
- A simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file.
- Classes for all entities used in AirBnB (User, State, City, Place, etc.) that inherit from BaseModel.
- The first abstracted storage engine of the project: File storage.
- Unittests to validate all our classes and storage engine.

## Learning Objectives

This project will help us to learn about:

- Creating a Python package.
- Creating a command interpreter in Python using the cmd module.
- Implementing Unit testing in a large project.
- Serializing and deserializing a Class.
- Writing and reading a JSON file.
- Managing datetime.
- Understanding and using UUID.
- Using \*args and \*\*kwargs in Python.
- Handling named arguments in a function.

## Getting Started

To get started with this project, clone this repository and navigate to the project directory. Run the console file to start the command interpreter.

```bash
$ git clone https://github.com/Mohabdo21/AirBnB_clone.git

$ cd AirBnB_clone/

$ ./console.py
```
You should see the console prompt `(hbnb)` .

## Usage

**Interactive Mode**:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
```

It Also can run on **Non-Interactive** mode:

```
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
```

Console Commands
----------------

The console supports several commands for managing your objects:

- `create` - create an object
- `show` - show an object (based on id)
- `destroy` - destroy an object
- `all` - show all objects, of one type or all types
- `update` - Updates an instance based on the class name and id
- `quit/EOF` - quit the console
- `help` - see descriptions of commands

### `create`

Creates a new instance of a given class, saves it to the JSON file, and prints the `id`.

Usage: `create <class>`

Example:

```
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907

```

### `show`

Prints the string representation of an instance based on the class name and `id`.

Usage: `show <class> <id>` or `<class>.show(<id>)`

Example:

```
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}

```

### `destroy`

Deletes an instance based on the class name and `id`.

Usage: `destroy <class> <id>` or `<class>.destroy(<id>)`

Example:

```
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907

```

### `all`

Shows all instances of a given class. If no class is specified, it displays all instantiated objects.

Usage: `all` or `all <class>` or `<class>.all()`

Example:

```
(hbnb) all BaseModel
["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}", "[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}"]

```

### `count`

Retrieves the number of instances of a given class.

Usage: `count <class>` or `<class>.count()`

Example:

```
(hbnb) User.count()
2

```

### `update`

Updates an instance based on the class name and `id` by adding or updating an attribute.

Usage:

-   `update <class> <id> <attribute_name> <attribute_value>`
-   `<class>.update(<id>, <attribute_name>, <attribute_value>)`
-   `<class>.update(<id>, <dictionary>)`

Example:

```
(hbnb) User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", "first_name", "John")
(hbnb) User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", "age", 89)

```

### `quit` and `EOF`

These commands are used to exit the program.

Usage: `quit` or `EOF`

Example:

```
(hbnb) quit

```

# Help

To Display information and usage of available commands:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) help all
Usage: all or all <class> or <class>.all()
        Display string representation of all instances
        of a given class if no class is specified display
        all instatiated objects
(hbnb)
```

Error Messages
--------------

If you enter a command incorrectly, the console will print an error message. For example, if you try to create an instance of a class that doesn't exist, you'll see the message `** class doesn't exist **`.

```
(hbnb) all MyModel
** class doesn't exist **

```

That's it! You're now ready to manage your AirBnB objects using the HBNB console. Enjoy!

# Supported classes:

- BaseModel
- User
- State
- City
- Amenity
- Place
- Review

![repr of the json file](https://github.com/Mohabdo21/AirBnB_clone/blob/main/images/jsoncrack.com.jpeg?raw=true)
