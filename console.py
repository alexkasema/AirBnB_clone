#!/usr/bin/python3

""" The console command interpreter """

import cmd


class HBNBCommand(cmd.Cmd):
    """ The entry point of command Interpreter """

    prompt = '(hbnb) '

    def do_EOF(self, args):
        """ End of File implementation to exit program """
        return True

    def do_quit(self, args):
        """ Quit command to exit the program """
        return True

    def emptyline(self):

        """Do nothing when an empty line in entered in response to prompt"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
