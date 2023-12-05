#!/usr/bin/python3
"""
    Airbnb console program
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """contains the entry point of the command interpreter"""
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """empty line + ENTER shouldn’t execute anything"""
        return False

if __name__ == '__main__':
    HBNBCommand().cmdloop()       
