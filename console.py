#!/usr/bin/python3

""" The console command interpreter """

import cmd
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ The entry point of command Interpreter """

    prompt = '(hbnb) '
    my_class_list = ["BaseModel"]

    def do_EOF(self, args):
        """ End of File implementation to exit program """
        return True

    def do_quit(self, args):
        """ Quit command to exit the program """
        return True

    def emptyline(self):

        """Do nothing when an empty line in entered in response to prompt"""
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
