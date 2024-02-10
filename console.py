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
        """Creates a new instance of BaseModel"""
        if len(line) == 0:
            print("** class name missing **")
        else:
            try:
                cls_type = eval(line)
                new_inst = cls_type()
                new_inst.save()
                #storage.save()
                print(new_inst.id)
            except Exception:
                pass
                print("** class doesn't exist **")

    def do_show(self, line):
        """String representation of an instance"""
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

        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) >= 3:
            print("** too many arguments **")
            return
        cls_name = args[0]
        if cls_name not in class_mapping or not cls_name:
            print("** class doesn't exist **")
            return
        inst_id = args[1]
        key = "{}.{}".format(cls_name, inst_id)
        insts = storage.all()
        if cls_name not in class_mapping:
            print("** class doesn't exist **")
            return
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
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        cls_name = args[0]
        if cls_name not in class_mapping:
            print("** class doesn't exist **")
            return
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
        lines = line.split('.')
        if len(lines) > 1:

            # Show an instance based on its ID
            if lines[1].startswith("show"):
                pattern = r"show\((.*?)\)"
                match = re.findall(pattern, lines[1])
                obj_id = match[0].split(',')[0]
                obj_id = obj_id.replace('"', '')
                # print(obj_id)
                key = "{}.{}".format(lines[0], obj_id)
                for ky, obj in storage.all().items():
                    if ky == key: 
                        print(storage.all()[ky])
                        return
                print("** no instance found **")

            # Destroy an instance based on his ID
            if lines[1].startswith("destroy"):
                cls_name = line[:-10]
                pattern = r'destroy\("([^"]+)"\)'
                match = re.findall(pattern, lines[1])
                match = match[0]

                key = "{}.{}".format(lines[0], match)
                for ky, obj in storage.all().items():
                    if key == ky:
                        del storage.all()[key]
                        storage.save()
                        return
                print("** no instance found **")

            # update an instance based on it's ID
            if lines[1].startswith("update("):
                #update multiple attributes in an instance using a dict
                if lines[1].split()[1].startswith("{"):
                    _, args = line.split("(", 1) # Extract uuid from parsed str argmnt
                    args = args.rsplit(")", 1)[0] 
                    uuid = args.split()[0].replace('"', "").replace("'", "").strip(",")
                    key = "{}.{}".format(lines[0], uuid)
                    #key = '"' + key + '"'
                    pattern = r'{.*}' # regex pattern to use to extract dictio
                    dictionary = re.search(pattern, args).group() #extract dict
                    dictionary = eval(dictionary)
                    keys_stored = list(storage.all().keys())
                    if key in keys_stored:
                        for k, val in dictionary.items():
                            setattr(storage.all()[key], k, val)
                    return

                #Update an instance's attribute one at a time
                parts = lines[1].strip("update(").rstrip(")").split(", ")
                if len(parts) == 3:
                    parts2 = []
                    for part in parts:
                        part = part.strip("\"").strip("'")
                        parts2.append(part)
                    instance_id, attr_name, attr_value = parts2

                    instance_id = instance_id.strip("\"").rstrip("'")
                    attr_name = attr_name.strip("\"").strip("'")
                    attr_value_str = attr_value.strip("\"").strip("'")
                      #check if attribute to be set has an int val and cast it
                    if attr_value_str.isdigit():
                        cast = type(eval(attr_value_str))
                        attr_value_str = cast(attr_value_str)
                    key = "{}.{}".format(lines[0], instance_id)
                    insts = storage.all()
                    if key in insts:
                        instance = insts[key]
                    else:
                       print("** instance not found **")
                       return

                    setattr(instance, attr_name, attr_value_str)
                    instance.save()
                    storage.save()
                else:
                    print("Usage: <class name>.update(<id>, <attribute\
name>,<attribute value>) or\n"
"Usage: <class name>.update(<id>, <dictionary\
representation>)")
                    return
                
            # get all insts of a class, eg User.all().
            if line.endswith(".all()"):
                cls_name = line[:-6]
                try:
                    cls = globals()[cls_name]
                    objlst = [str(obj) for key, obj in storage.all().items()
                              if isinstance(obj, cls)]
                    print(objlst)
                except KeyError:
                    print("** class doesn't exist **")

            # Gets the total number of insts of a cls, ex User.count().
            if line.endswith(".count()"):
                cls_name = line[:-8]
                try:
                    cls = globals()[cls_name]
                    objlst = [obj for key, obj in storage.all().items()
                              if isinstance(obj, cls)]
                    print(len(objlst))
                except KeyError:
                    print("** class doesn't exist **")

    def do_all(self, line):
        """Prints all string representation of all instances"""
        args = line.split()
        insts = storage.all()
        if len(args) == 0:
            # If no class name is provided, print all instances
            str_rep = [str(instance) for instance in insts.values()]
        else:
            # If class name is provided, filter instances of that class
            class_mapping = {
                  'BaseModel': BaseModel,
                  'User': User,
                  'Place': Place,
                  'State': State,
                  'Review': Review,
                  'City': City,
                  'Amenity': Amenity,
                  }
            if args[0] not in class_mapping:
                print("** class doesn't exist **")
                return
            cls_name = args[0]
            str_rep = [str(instance) for key, instance in insts.items()
                       if key.startswith(cls_name + ".")]

        if not str_rep:
            print("** class doesn't exist **")
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
        inst_id = inst_id.strip("\"").strip("'")
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
        attr_name = attr_name.strip("\"").strip("'")
        attr_value_str = args[3]
        attr_value_str = attr_value_str.strip("\"").strip("'")
        instance = insts[key]
        setattr(instance, attr_name, attr_value_str)
        instance.save()
        storage.save()

    def do_count(self, line):
        """Prints total number of insts of a cls"""
        class_mapping = {
        'BaseModel': BaseModel,
        'User': User,
        'Place': Place,
        'State': State,
        'Review': Review,
        'City': City,
        'Amenity': Amenity,
         }
        count = 0
        try:
            if line in class_mapping:
                cls = class_mapping[line]
                for key, objs in storage.all().items():
                    if isinstance(objs, cls):
                        count += 1
                print(count)
        except KeyError:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
