#!/usr/bin/python3
"""
    Airbnb console program
"""
import cmd
import re
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """contains the entry point of the command interpreter"""
    prompt = '(hbnb) '
    
    def do_EOF(self, line):
        """exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
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
         'User': User,
         'Place': Place,
         'State': State,
         'Review': Review,
         'City': City,
         'Amenity': Amenity,
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
         'User': User,
         'Place': Place,
         'State': State,
         'Review': Review,
         'City': City,
         'Amenity': Amenity,
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

    def default(self, line):
        """Called for any command not recognized by other 'do_*' """
        # Show an instance based on its ID
        lines = line.split('.')
        if lines[1].startswith("show(\""):
            pattern = r'show\("([^"]+)"\)'
            match = re.findall(pattern, lines[1])
            match = match[0]
            key = "{}.{}".format(lines[0], match)
            for ky, obj in storage.all().items():
                if match ==  obj.id:
                    print(obj)
                    return
            print("** no instance found **")
        # Destroy an instance based on his ID 
        if lines[1].startswith("destroy"):
            cls_name = line[:-10]
            if lines[1].startswith("destroy(\""):
                pattern = r'destroy\("([^"]+)"\)'
                match = re.findall(pattern, lines[1])
                match = match[0]

                key = "{}.{}".format(lines[0], match)
                for ky, obj in storage.all().items():
                    if key ==  ky:
                       del storage.all()[key]
                       storage.save()
                       return
                print("** no instance found **")

        # get all insts of a class, eg User.all()
        if line.endswith(".all()"):
            cls_name = line[:-6]

            try:
                cls = globals()[cls_name]
                objlst = [str(obj) for key, obj in storage.all().items() if isinstance(obj, cls)]
                print(objlst)
            except KeyError:
                print("** class doesn't exist **")
        # Gets the total number of insts of a cls, ex User.count()
        if line.endswith(".count()"):
            cls_name = line[:-8]
            try:
                cls = globals()[cls_name]
                objlst = [obj for key, obj in storage.all().items() if isinstance(obj, cls)]
                print(len(objlst))
            except KeyError:
                 print("** class doesn't exist **")
                
    def do_all(self, line):
        """
            Prints all string representation of all instances based
            or not on the class name
        """
        args = line.split('.')
        insts = storage.all()
        print(args[0])
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
            'User': User,
            'Place': Place,
            'State': State,
            'Review': Review,
            'City': City,
            'Amenity': Amenity,
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
