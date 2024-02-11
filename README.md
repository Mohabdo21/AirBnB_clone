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

```
$ git clone https://github.com/Mohabdo21/AirBnB_clone.git

$ cd AirBnB_clone/

$ ./console.py
```

## Usage

Interactive Mode:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
```

It Also can run on Non-Interactive mode:

```
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
```

## Commands:

- `create` - create an object
- `show` - show an object (based on id)
- `destroy` - destroy an object
- `all` - show all objects, of one type or all types
- `update` - Updates an instance based on the class name and id
- `quit/EOF` - quit the console
- `help` - see descriptions of commands

To start console type in shell

```
AirBnB_clone$ ./console.py
(hbnb)

```

---

# Create

To create an object use command `create`:

```
(hbnb) create BaseModel

```

# Show

To show an instance based on the class name and id. Ex:

```
(hbnb) show BaseModel 1234-1234-1234.

```

# Destroy

To Delete an instance of an object using class name and id `destroy <class_name id>`. Ex:

```
(hbnb) destroy BaseModel 1234-1234-1234.

```

# All

`all` or `all <class_name>` to display the instance of all classes or the selected class Ex:

```
(hbnb) all or all State

```

# Update

Updates an instance attributes based on the class name and id:

```
(hbnb) update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com"

```

# Quit

`quit` or `EOF` to terminate the console.

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

# Supported classes:

- BaseModel
- User
- State
- City
- Amenity
- Place
- Review

![repr of the json file](https://github.com/Mohabdo21/AirBnB_clone/blob/main/images/jsoncrack.com.jpeg?raw=true)
