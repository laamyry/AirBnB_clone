#!/usr/bin/python3
'''Console module AirBnB'''
import cmd
from models.base_model import BaseModel as base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage
import re
import json


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    al_class = ["BaseModel", "User", "State",
                 "City", "Amenity", "Place", "Review"]

    str_att = ["name", "amenity_id", "place_id", "state_id",
                "user_id", "city_id", "description", "text",
                "email", "password", "first_name", "last_name"]
    int_att = ["number_rooms", "number_bathrooms",
                "max_guest", "price_by_night"]
    float_att = ["latitude", "longitude"]

    def do_EOF(self, arg):
        return True

    def do_quit(self, arg):
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        classes = {
            "BaseModel": base,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review
        }
        if self.valid(arg):
            args = arg.split()
            if args[0] in classes:
                new = classes[args[0]]()
            storage.save()
            print(new.id)

    def do_clear(self, arg):
        storage.all().clear()
        self.every(arg)
        print("** All data been clear! **")

    def valid(self, arg, _id_flag=False, _att_flag=False):
        args = arg.split()
        _len = len(arg.split())
        if _len == 0:
            print("** class name missing **")
            return False
        if args[0] not in HBNBCommand.al_class:
            print("** class doesn't exist **")
            return False
        if _len < 2 and _id_flag:
            print("** instance id missing **")
            return False
        if _id_flag and args[0]+"."+args[1] not in storage.all():
            print("** no instance found **")
            return False
        if _len == 2 and _att_flag:
            print("** attribute name missing **")
            return False
        if _len == 3 and _att_flag:
            print("** value missing **")
            return False
        return True

    def do_show(self, arg):
        if self.valid(arg, True):
            args = arg.split()
            _key = args[0]+"."+args[1]
            print(storage.all()[_key])

    def destr(self, arg):
        if self.valid(arg, True):
            args = arg.split()
            _key = args[0]+"."+args[1]
            del storage.all()[_key]
            storage.save()

    def every(self, arg):
        args = arg.split()
        _len = len(args)
        my_list = []
        if _len >= 1:
            if args[0] not in HBNBCommand.al_class:
                print("** class doesn't exist **")
                return
            for key, value in storage.all().items():
                if args[0] in key:
                    my_list.append(str(value))
        else:
            for key, value in storage.all().items():
                my_list.append(str(value))
        print(my_list)

    def casting(self, arg):
        try:
            if "." in arg:
                arg = float(arg)
            else:
                arg = int(arg)
        except ValueError:
            pass
        return arg

    def updat(self, arg):
        if self.valid(arg, True, True):
            args = arg.split()
            _key = args[0]+"."+args[1]
            if args[3].startswith('"'):
                match = re.search(r'"([^"]+)"', arg).group(1)
            elif args[3].startswith("'"):
                match = re.search(r'\'([^\']+)\'', arg).group(1)
            else:
                match = args[3]
            if args[2] in HBNBCommand.str_att:
                setattr(storage.all()[_key], args[2], str(match))
            elif args[2] in HBNBCommand.int_att:
                setattr(storage.all()[_key], args[2], int(match))
            elif args[2] in HBNBCommand.float_att:
                setattr(storage.all()[_key], args[2], float(match))
            else:
                setattr(storage.all()[_key], args[2], self.casting(match))
            storage.save()

    def counter(self, arg):
        counter = 0
        for key in storage.all():
            if arg[:-1] in key:
                counter += 1
        print(counter)

    def exe(self, arg):
        methods = {
            "all": self.every,
            "counter": self.counter,
            "show": self.do_show,
            "destroy": self.destr,
            "update": self.updat,
            "create": self.do_create
        }
        match = re.findall(r"^(\w+)\.(\w+)\((.*)\)", arg)
        args = match[0][0]+" "+match[0][2]
        _list = args.split(", ")
        _list[0] = _list[0].replace('"', "").replace("'", "")
        if len(_list) > 1:
            _list[1] = _list[1].replace('"', "").replace("'", "")
        args = " ".join(_list)
        if match[0][1] in methods:
            methods[match[0][1]](args)

    def default(self, arg):
        match = re.findall(r"^(\w+)\.(\w+)\((.*)\)", arg)
        if len(match) != 0 and match[0][1] == "update" and "{" in arg:
            _dict = re.search(r'{([^}]+)}', arg).group()
            _dict = json.loads(_dict.replace("'", '"'))
            for k, v in _dict.items():
                _arg = arg.split("{")[0]+k+", "+str(v)+")"
                self.exe(_arg)
        elif len(match) != 0:
            self.exe(arg)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
