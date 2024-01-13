#!/usr/bin/python3

""" The console command interpreter """

import cmd
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
