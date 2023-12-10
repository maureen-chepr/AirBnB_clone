#!/usr/bin/python3
"""Test cases for the console"""
import datetime
import uuid
import unittest
from unittest.mock import patch
from models import storage
from console import HBNBCommand
from models.engine.file_storage import FileStorage
from io import StringIO
from models.base_model import BaseModel
from models.state import State


class TestHBNBCommand_prompt(unittest.TestCase):
    """Unittest of the custom command prompt(hbnb)"""

    def test_prompt_string(self):
        """correct output of prompt"""
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_emptyline(self):
        """input as an empty: line"""
        with patch('builtins.input', return_value=''):
            with patch("sys.stdout", new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd(""))
                self.assertEqual("", f.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_EOF(self, mock_stdout):
        """Test do_EOF command"""
        with patch('builtins.input', return_value='EOF'):
            result = HBNBCommand().onecmd("EOF")
            self.assertTrue(result)
            self.assertEqual(mock_stdout.getvalue(), '')

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_quit(self, mock_stdout):
        """Test do_quit command"""
        with patch('builtins.input', return_value='quit'):
            with patch('sys.stdout', new=StringIO()) as f:
                result = HBNBCommand().onecmd("quit")
                self.assertTrue(result)
                self.assertEqual(f.getvalue(), '')

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_create(self, mock_stdout):
        """Test do_create command"""
        with patch('builtins.input', return_value='create BaseModel'):
            with patch('sys.stdout', new=StringIO()) as f:
                result = HBNBCommand().onecmd("create BaseModel")
                self.assertFalse(result)
                exp = f.getvalue().strip()
                self.assertTrue(
                    exp, "{}".format(exp)
                )

    def test_do_update(self):
        """Test the do_update method"""
        with patch('sys.stdout', new_callable=StringIO) as f:
            obj = State()
            storage.new(obj)
            storage.save()
            HBNBCommand().onecmd('update State {} name "new_name"'
                                 .format(obj.id))
            updated_obj = storage.all()['State.{}'.format(obj.id)]
            self.assertEqual(updated_obj.name, '"new_name"')

    def test_help_quit(self):
        """Testing help quit"""
        with patch("sys.stdout", new=StringIO()) as f:
            expd_outp = "Quit command to exit the program"
            result = HBNBCommand().onecmd("help quit")
            self.assertFalse(result)
            self.assertEqual(expd_outp, f.getvalue().strip())

    def test_help_create(self):
        """Testing help create"""
        with patch("sys.stdout", new=StringIO()) as f:
            expd_outp = "Creates a new instance of BaseModel. \
                         Saves it json fi, prints id"
            result = HBNBCommand().onecmd("help create")
            self.assertFalse(result)
            self.assertEqual(expd_outp, f.getvalue().strip())

    def test_help_show(self):
        """Testing help show"""
        with patch("sys.stdout", new=StringIO()) as f:
            expd_outp = "Prints the string representation of an instance \
                         based on the class name and id"
            result = HBNBCommand().onecmd("help show")
            self.assertFalse(result)
            self.assertEqual(expd_outp, f.getvalue().strip())

    def test_help_destroy(self):
        """Testing help destroy"""
        with patch("sys.stdout", new=StringIO()) as f:
            expd_outp = "Deletes an instance based on the class name and id"
            result = HBNBCommand().onecmd("help destroy")
            self.assertFalse(result)
            self.assertEqual(expd_outp, f.getvalue().strip())

    def test_help_all(self):
        """Testing help all"""
        with patch("sys.stdout", new=StringIO()) as f:
            exp_out = "Prints all string representation of all instances"
            result = HBNBCommand().onecmd("help all")
            self.assertFalse(result)
            self.assertEqual(exp_out, f.getvalue().strip(), exp_out)

    def test_doc(self):
        """Testing for presence of docstring"""
        self.assertIsNotNone(HBNBCommand.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.default.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)

    def test_do_update_missing_class_name(self):
        """Test do_update when the class name is missing"""
        with patch('sys.stdout', new_callable=StringIO) as f:
            HBNBCommand().onecmd('update')
            exp_out = "** class name missing **\n"
            self.assertEqual(f.getvalue(), exp_out)

    def test_do_update_missing_instance_id(self):
        """Test do_update when the instance id is missing"""
        with patch('sys.stdout', new_callable=StringIO) as f:
            HBNBCommand().onecmd('update BaseModel')
            exp_out = "** instance id missing **\n"
            self.assertEqual(f.getvalue(), exp_out)

    def test_do_update_missing_class_and_instance_id(self):
        """Test do_update when both class name and instance id are missing"""
        with patch('sys.stdout', new_callable=StringIO) as f:
            HBNBCommand().onecmd('update')
            exp_out = "** class name missing **\n"
            self.assertEqual(f.getvalue(), exp_out)

    def test_do_update_missing_attribute_name(self):
        """Test do_update when the attribute name is missing"""
        with patch('sys.stdout', new_callable=StringIO) as f:
            HBNBCommand().onecmd('update BaseModel 123')
            exp_out = "** attribute name missing **\n"
            self.assertEqual(f.getvalue(), exp_out)

    def test_do_update_missing_value(self):
        """Test do_update when the value for the attribute is missing"""
        with patch('sys.stdout', new_callable=StringIO) as f:
            HBNBCommand().onecmd('update BaseModel 123 name')
            exp_out = "** value missing **\n"
            self.assertEqual(f.getvalue(), exp_out)

    def test_do_all_too_many_arguments(self):
        """Test do_all when there are too many arguments"""
        with patch('sys.stdout', new_callable=StringIO) as f:
            HBNBCommand().onecmd('all BaseModel abc')
            exp_out = "** too many arguments **\n"
            self.assertEqual(f.getvalue(), exp_out)

    def test_do_count_missing_class_name(self):
        """Test do_count when the class name is missing"""
        with patch('sys.stdout', new_callable=StringIO) as f:
            HBNBCommand().onecmd('count')
            exp_out = "** class name missing **\n"
            self.assertEqual(f.getvalue(), exp_out)

    def test_do_count_too_many_arguments(self):
        """Test do_count when there are too many arguments"""
        with patch('sys.stdout', new_callable=StringIO) as f:
            HBNBCommand().onecmd('count BaseModel abc')
            exp_out = "** too many arguments **\n"
            self.assertEqual(f.getvalue(), exp_out)

    def test_do_show_missing_class_name(self):
        """Test do_show when the class name is missing"""
        with patch('sys.stdout', new_callable=StringIO) as f:
            HBNBCommand().onecmd('show')
            exp_out = "** class name missing **\n"
            self.assertEqual(f.getvalue(), exp_out)

    def test_do_show_missing_instance_id(self):
        """Test do_show when the instance id is missing"""
        with patch('sys.stdout', new_callable=StringIO) as f:
            HBNBCommand().onecmd('show BaseModel')
            exp_out = "** instance id missing **\n"
            self.assertEqual(f.getvalue(), exp_out)

    def test_do_show_missing_class_name_and_instance_id(self):
        """Test do_show when both class name and instance id are missing"""
        with patch('sys.stdout', new_callable=StringIO) as f:
            HBNBCommand().onecmd('show')
            exp_out = "** class name missing **\n"
            self.assertEqual(f.getvalue(), exp_out)

    def test_do_show_too_many_arguments(self):
        """Test do_show when there are too many arguments"""
        with patch('sys.stdout', new_callable=StringIO) as f:
            HBNBCommand().onecmd('show BaseModel extra_argument')
            exp_out = "** too many arguments **\n"
            self.assertEqual(f.getvalue(), exp_out)

    def test_do_all_too_many_arguments(self):
        """Test do_all when there are too many arguments"""
        with patch('sys.stdout', new_callable=StringIO) as f:
            HBNBCommand().onecmd('all BaseModel extra_argument')
            exp_out = "** too many arguments **\n"
            self.assertEqual(f.getvalue(), exp_out)

    def test_do_destroy_missing_class_name(self):
        """Test do_destroy when the class name is missing"""
        with patch('sys.stdout', new_callable=StringIO) as f:
            HBNBCommand().onecmd('destroy')
            exp_out = "** class name missing **\n"
            self.assertEqual(f.getvalue(), exp_out)

    def test_do_destroy_missing_instance_id(self):
        """Test do_destroy when the instance id is missing"""
        with patch('sys.stdout', new_callable=StringIO) as f:
            HBNBCommand().onecmd('destroy BaseModel')
            exp_out = "** instance id missing **\n"
            self.assertEqual(f.getvalue(), exp_out)

    def test_do_destroy_missing_class_name_and_instance_id(self):
        """Test do_destroy when both class name and instance id are missing"""
        with patch('sys.stdout', new_callable=StringIO) as f:
            HBNBCommand().onecmd('destroy')
            exp_out = "** class name missing **\n"
            self.assertEqual(f.getvalue(), exp_out)


if __name__ == "__main__":
    unittest.main()
