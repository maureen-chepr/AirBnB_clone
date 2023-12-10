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
            self.assertEqual(f.getvalue(), '')

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


class TestHBNBCommand_help(unittest.TestCase):
    """Testing help commands"""

    def test_help_quit(self):
        """Testing help quit"""
        with patch("sys.stdout", new=StringIO()) as f:
            expd_outp = "Quit command to exit the program"
            result = HBNBCommand().onecmd("help quit")
            self.assertFalse(result)
            self.assertEqual(expd_outp, f.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
