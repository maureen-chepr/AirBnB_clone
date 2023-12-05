#!/usr/bin/python3
"""
    Airbnb console program
"""
import cmd
from models import storage, BaseModel


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

    def do_create(self, line):
        """Creates a new instance of BaseModel. Saves it json fi, prints id"""
        #if not self.__class__.__name__:
        if len(line) == 0:
            print("** class name missing **")
        else:
            try:
                cls_type = eval(line)
                new_inst = cls_type()
                new_inst.save()
                storage.save()
                print(new_inst.id)
            except:
                print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an instance based on the class name and id"""
        args = line.split()
        if len(line) == 0:
            print("** class name missing **")
        cls_name = args[0]
        if cls_name not in cls_mapping:
            print("** class doesn't exist **")
        inst_id = args[1]
        key = "{}.{}".format(cls_name, inst_id)
        insts = storage.all()
        if key not in insts:
            print("** no instance found **")
        else:
            print(insts[key])



if __name__ == '__main__':
    HBNBCommand().cmdloop()       
