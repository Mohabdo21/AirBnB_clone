#!/usr/bin/python3

"""defined HBNB program console"""

import cmd
import json
import re
from shlex import split

from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


def parse(arg):
    """This is function parsing the argument string"""
    arg = arg.replace("'", '"')
    curly_b = re.search(r"\{(.*?)\}", arg)
    brakets = re.search(r"\[(.*?)\]", arg)
    if curly_b is None:
        if brakets is None:
            return [i.strip(",") for i in split(arg)]
        lex = split(arg[: brakets.span()[0]])
        ret = [i.strip(",") for i in lex]
        ret.append(brakets.group())
        return ret
    lex = split(arg[: curly_b.span()[0]])
    ret = [i.strip(",") for i in lex]
    ret.append(curly_b.group())
    return ret


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB
    Attribute:
        prompt (str): The command prompt
    """

    prompt = "(hbnb) "
    _models = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
    }

    def default(self, line):
        """Default behavior for cmd module when input is invalid"""
        args = line.split()
        argd = {
            "all": self.do_all,
            "show": self.do_show,
            "create": self.do_create,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update,
        }
        match = re.search(r"\.", line)
        if match is not None:
            args = [line[: match.span()[0]], line[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", args[1])
            if match is not None:
                command = [args[1][: match.span()[0]], match.group()[1:-1]]
                if command[0] in argd:
                    call = "{} {}".format(args[0], command[1])
                    try:
                        return argd[command[0]](call)
                    except Exception as e:
                        print(f"Error: {e}")
        print(f"*** Unknown syntax: {line}")
        return False

    def do_quit(self, _):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program on EOF (ctrl+D)"""
        return True

    def emptyline(self):
        """Do nothing when an empty line is enterd"""
        pass

    def do_create(self, arg):
        """Usage: create <class>
        Create a new class instance and print its id
        """
        ar = parse(arg)
        if len(ar) == 0:
            print("** class name missing **")
        elif ar[0] not in self._models:
            print("** class doesn't exist **")
        else:
            print(self._models[ar[0]]().id)
            storage.save()

    def do_show(self, arg):
        """Usage: show <class> <id> or <class>.show(<id>)
        display the string representation of a class instance
        of a given id"""
        ar = parse(arg)
        obj = storage.all()
        if len(ar) == 0:
            print("** class name missing **")
        elif ar[0] not in self._models:
            print("** class doesn't exist **")
        elif len(ar) == 1:
            print("** instance id missing **")
        elif f"{ar[0]}.{ar[1]}" not in obj:
            print("** no instance found **")
        else:
            print(obj[f"{ar[0]}.{ar[1]}"])

    def do_destroy(self, arg):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of a given id"""
        ar = parse(arg)
        obj = storage.all()
        if len(ar) == 0:
            print("** class name missing **")
        elif ar[0] not in self._models:
            print("** class doesn't exist **")
        elif len(ar) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(ar[0], ar[1]) not in obj.keys():
            print("** no instance found **")
        else:
            del obj["{}.{}".format(ar[0], ar[1])]
            storage.save()

    def do_all(self, arg):
        """Usage: all or all <class> or <class>.all()
        Display string representation of all instances
        of a given class if no class is specified display
        all instatiated objects"""
        ar = parse(arg)
        if len(ar) > 0 and ar[0] not in self._models:
            print("** class doesn't exist **")
        else:
            objl = []
            for OBJ in storage.all().values():
                if len(ar) > 0 and ar[0] == OBJ.__class__.__name__:
                    objl.append(OBJ.__str__())
                elif len(ar) == 0:
                    objl.append(OBJ.__str__())
            print(json.dumps(objl))

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of given class"""
        ar = parse(arg)
        if len(ar) == 0:
            print("** class name missing **")
        elif ar[0] not in self._models:
            print("** class doesn't exist **")
        count = 0
        for OBJ in storage.all().values():
            if ar[0] == OBJ.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <atrribute_value>
        or <class>.update(<id>, <attribute_name>, <attribute_value>)
        or <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value or dictionary"""
        ar = parse(arg)
        obj = storage.all()
        data = None
        if len(ar) == 0:
            print("** class name missing **")
            return False
        if ar[0] not in self._models:
            print("** class doesn't exist **")
            return False
        if len(ar) == 1:
            print("** instance id missing **")
            return False
        if f"{ar[0]}.{ar[1]}" not in obj.keys():
            print("** no instance found **")
            return False
        if len(ar) == 2:
            print("** attribute name missing **")
            return False
        if len(ar) == 3:
            try:
                data = json.loads(ar[2])
                if not isinstance(data, dict):
                    print("** value missing **")
                    return False
            except json.JSONDecodeError:
                print("** value missing **")
                return False
        OBJ = obj[f"{ar[0]}.{ar[1]}"]
        if len(ar) == 4:
            if ar[2] in OBJ.__class__.__dict__.keys():
                valtype = type(OBJ.__class__.__dict__[ar[2]])
                OBJ.__dict__[ar[2]] = valtype(ar[3])
            else:
                OBJ.__dict__[ar[2]] = ar[3]
        elif isinstance(data, dict):
            for key, value in data.items():
                if key in OBJ.__class__.__dict__.keys() and type(
                    OBJ.__class__.__dict__[key]
                ) in {str, int, float}:
                    valtype = type(OBJ.__class__.__dict__[key])
                    OBJ.__dict__[key] = valtype(value)
                else:
                    OBJ.__dict__[key] = value
        OBJ.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
