#!/usr/bin/python3

""" The console command interpreter """

import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ The entry point of command Interpreter """

    prompt = '(hbnb) '
    my_class_list = ["BaseModel", "User", "State", "City", "Amenity",
                     "Place", "Review"]

    def do_EOF(self, args):
        """ End of File implementation to exit program """
        return True

    def do_quit(self, args):
        """ Quit command to exit the program """
        return True

    def emptyline(self):

        """Do nothing when an empty line in entered in response to prompt"""
        pass
    
    def postloop(self):
        """ Do nothing after each console loop """
        pass

    def do_create(self, args):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        Args:
            args (string): command line input
        """
        command = args.split()
        if not self.verify_class_name(command):
            return
        new_instance = eval(command[0] + '()')
        if isinstance(new_instance, BaseModel):
            new_instance.save()
            print(new_instance.id)
        elif isinstance(new_instance, User):
            new_instance.save()
            print(new_instance.id)
        elif isinstance(new_instance, State):
            new_instance.save()
            print(new_instance.id)
        elif isinstance(new_instance, City):
            new_instance.save()
            print(new_instance.id)
        elif isinstance(new_instance, Amenity):
            new_instance.save()
            print(new_instance.id)
        elif isinstance(new_instance, Place):
            new_instance.save()
            print(new_instance.id)
        elif isinstance(new_instance, Review):
            new_instance.save()
            print(new_instance.id)
        return

    def do_show(self, args):
        """
        Prints the string representation of an instance
        based on the class name and id.
        Args:
            args(string): A string of command line inputs
        """
        command = args.split()
        if not self.verify_class_name(command):
            return
        if not self.verify_id(command):
            return
        key = '{}.{}'.format(command[0], command[1])
        objs = models.storage.all()

        print(objs[key])

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name
        and id (save the change into the JSON file).
        """
        command = args.split()
        if not self.verify_class_name(command):
            return
        if not self.verify_id(command):
            return
        key = '{}.{}'.format(command[0], command[1])
        objs = models.storage.all()

        del objs[key]
        models.storage.save()

    def do_all(self, args):
        """
        Prints all string representation of all instances
        based or not on the class name.
        """
        command = args.split()
        objs = models.storage.all()

        print_all = []
        if len(command) == 0:
            for v in objs.values():
                print_all.append(str(v))
        elif command[0] in HBNBCommand.my_class_list:
            for k, v in objs.items():
                if command[0] in k:
                    print_all.append(str(v))
        else:
            print("** class doesn't exist **")
            return False

        print(print_all)

    def do_update(self, args):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute
        (save the change into the JSON file)
        """

        command = args.split()

        if not self.verify_class_name(command):
            return
        if not self.verify_id(command):
            return
        if not self.verify_attribute_name(command):
            return

        objs = models.storage.all()
        key = '{}.{}'.format(command[0], command[1])

        setattr(objs[key], command[2], command[3])
        models.storage.save()

    def default(self, args):
        """ called when the first input command is a class name """
        command = args.strip().split('.')
        if len(command) < 2:
            print("** attribute name missing **")
            return

        objs = models.storage.all()
        class_name = command[0]
        command_name = command[1].lower()

        split2 = command_name.strip(')').split('(')
        command_name = split2[0]

        if command_name == "all":
            HBNBCommand.do_all(self, class_name)
        elif command_name == "count":
            count = 0

            for k in objs.keys():
                split_k = k.split('.')
                if class_name == split_k[0]:
                    count += 1
            print(count)

    @classmethod
    def verify_class_name(cls, command):
        """ verifies correct class names input """
        if len(command) == 0:
            print("** class name missing **")
            return False
        elif command[0] not in HBNBCommand.my_class_list:
            print("** class doesn't exist **")
            return False
        return True

    @staticmethod
    def verify_id(command):
        """verify if the id is in list of objects"""
        if len(command) < 2:
            print("** instance id missing **")
            return False
        objs = models.storage.all()
        key = '{}.{}'.format(command[0], command[1])

        if key not in objs.keys():
            print("** no instance found **")
            return False

        return True

    @staticmethod
    def verify_attribute_name(command):
        """
        Verifies the attributes inputted in the command
        """
        if len(command) < 3:
            print("** attribute name missing **")
            return False
        elif len(command) < 4:
            print("** value missing **")
            return False
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
