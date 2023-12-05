#!/usr/bin/python3
"""
    Airbnb console program
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


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
        class_mapping = {
         'BaseModel': BaseModel,
        } 
        args = line.split()
        if len(line) == 0:
            print("** class name missing **")
        if len(args) < 2:
            print("** instance id missing **")
        cls_name = args[0]
        if cls_name not in class_mapping:
            print("** class doesn't exist **")
        inst_id = args[1]
        key = "{}.{}".format(cls_name, inst_id)
        insts = storage.all()
        if key not in insts:
            print("** no instance found **")
        else:
            print(insts[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        class_mapping = {
         'BaseModel': BaseModel,
        }
        args = line.split()
        if len(line) == 0:
            print("** class name missing **")
        if len(args) < 2:
            print("** instance id missing **")
        cls_name = args[0]
        if cls_name not in class_mapping:
            print("** class doesn't exist **")
        inst_id = args[1]
        key = "{}.{}".format(cls_name, inst_id)
        insts = storage.all()
        if key not in insts:
            print("** no instance found **")
        else:
            del insts[key]
            storage.save()

    def do_all(self, line):
        """
            Prints all string representation of all instances based
            or not on the class name
        """
        args = line.split()
        insts = storage.all()

        if len(args) == 0:
            # If no class name is provided, print all instances
            str_rep = [str(instance) for instance in insts.values()]
        else:
            # If class name is provided, filter instances of that class
            cls_name = args[0]
            str_rep = [str(instance) for key, instance in insts.items() if key.startswith(cls_name + ".")]

        if not str_rep:
            print("** no instance found **")
        else:
            print(str_rep)


    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        class_mapping = {
            'BaseModel': BaseModel,
        }
        args = line.split()

        if len(args) == 0:
            print("** class name missing **")
            return

        cls_name = args[0]

        if cls_name not in class_mapping:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        inst_id = args[1]
        key = "{}.{}".format(cls_name, inst_id)
        insts = storage.all()

        if key not in insts:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        attr_name = args[2]
        attr_value_str = args[3]

        instance = insts[key]

        try:
            attr_type = type(getattr(instance, attr_name))
            attr_value = attr_type(attr_value_str)
        except (ValueError, TypeError):
            pass

        # Update the attribute value
        if attr_name not in ["id", "created_at", "updated_at"]:
            setattr(instance, attr_name, attr_value)
            instance.save()
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
