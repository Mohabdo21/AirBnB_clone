#!/usr/bin/python3

"""defined HBNB console"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import re
from shlex import split

def parse(arg):
    curly_b = re.search(r"\{(.*?)\]", arg)
    brakets = re.search(r"\[(.*?)\]", arg)
    if curly_b is None:
        if brakets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lex = split(arg[:brakets.span()[0]])
            ret = [i.strip(",") for i in lex]
            ret.append(brakets.group())
            return ret
    else:
        lex = split(ar[:curly_b.span()[0]])
        ret = [i.strip(",") for i in lex]
        ret.append(curly_b.group())
        return ret


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB
    Attribute:
        prompt (str): the command prompt
    """
    
    prompt = '(hbnb) '
    __classes = {
        "BaseModel",
        "User",
        "State",
        "Place",
        "Amenity",
        "Review"
    }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program on EOF (ctrl+D)"""
        print("")
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
        elif ar[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(ar[0])().id)
            storage.save()

    def do_show(self, arg):
        """Usage: show <class> <id> or <class>.show(<id>)
            display the string representation of a class instance 
            of a given id """
        ar = parse(arg)
        obj = storage.all()
        if len(ar)==0:
            print("** class doesn't exist **")
        elif ar[0] not in HBNBCommand.__classes:
            print("** class dosen't exist **")
        elif len(ar) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(ar[0], ar[1]) not in obj:
            print("** no instance found **")
        else:
            print(obj["{}.{}".format(ar[0], ar[1])])

    def do_destroy(self, arg):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
            Delete a class instance of a given id"""
        ar = parse(arg)
        obj = storage.all()
        if len(ar) == 0:
            print("** class name missing **")
        elif len(ar[0]) not in HBNBCommand.__classes:
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
        if len(ar) > 0 and ar[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for OBJ in storage.all().values():
                if len(ar) > 0 and ar[0] == OBJ.__class__.__name__:
                    objl.append(OBJ.__str__())
                elif len(ar) == 0:
                    objl.append(OBJ.__str__())
            print(objl)

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
            Retrieve the number of instances of given class"""
        ar = parse(arg)
        count = 0
        for OBJ in storage.all().values():
            if ar[0] == OBJ.__class__.__name__:
                count += 1
        print(count)
if __name__ == '__main__':
    HBNBCommand().cmdloop()
