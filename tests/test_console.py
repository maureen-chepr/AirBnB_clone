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


class TestHBNBCommand_prompting(unittest.TestCase):
    """Unittest of the custom command prompt(hbnb)"""

    #def test_prompt_string(self):
        #self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_emptyline(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())
    
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
            result = HBNBCommand().onecmd("quit")
            self.assertTrue(result)
            self.assertEqual(mock_stdout.getvalue(), '')

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_create(self, mock_stdout):
        """Test do_create command"""
        with patch('builtins.input', return_value='create BaseModel'):
            result = HBNBCommand().onecmd("create BaseModel")
            self.assertFalse(result)
            exp = mock_stdout.getvalue().strip()
            self.assertTrue(
                    exp, "{}".format(exp)
                    )

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_show(self, mock_stdout):
        """Test do_show command"""
        with patch('builtins.input', return_value='show BaseModel 45678'):
            result = HBNBCommand().onecmd("show BaseModel 45678")
            self.assertFalse(result)
            exp_out = mock_stdout.getvalue().strip()
            out = ("** no instance found **")
            self.assertEqual(exp_out, out)  # Rem to test success inst

    @patch('sys.stdout', new_callable=StringIO)
    def test_help_quit(self, mock_out):
        """Testing help for quit fn"""
        with patch("builtins.input", return_value="help quit"):
            result = HBNBCommand().onecmd("help quit")
            self.assertFalse(result)
            expd_outp = "Quit command to exit the program\n        \n"
            self.assertEqual(mock_out.getvalue(), expd_outp)

    @patch('sys.stdout', new_callable=StringIO)
    def test_help_show(self, mock_outpt):
        """Teseting help for show"""
        with patch("builtins.input", return_value="help show"):
            result = HBNBCommand().onecmd("help show") 
            self.assertFalse(result)
            expct_outp = "Prints the string representation of an instance based on the class name and id\n"
            self.assertEqual(mock_outpt.getvalue(), expct_outp)

    @patch('sys.stdout', new_callable=StringIO)
    def test_help_destroy(self, mock_output):
        """Testing help for destroy"""
        with patch('builtins.input', return_value="help destroy"):
            result = HBNBCommand().onecmd("help destroy")
            exp_output = "Deletes an instance based on the class name and id\n"
            self.assertEqual(mock_output.getvalue(), exp_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_help_all(self, mock_output):
        """Test help for do_all"""
        with patch('builtins.input', return_value="help all"):
            result = HBNBCommand().onecmd("help all")
            exp_outpt = "Prints all string representation of all instances\n"
            self.assertEqual(mock_output.getvalue(), exp_outpt)

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_update(self, mock_output):
        """Test help update"""
        with patch('builtins.input', return_value="help update"):
            HBNBCommand().onecmd("help update")
            exp_output = "Updates an instance based on the class name and id\n"
            self.assertEqual(mock_output.getvalue(), exp_output)

    @patch('sys.stdout', new_callable=StringIO)
    def

if __name__ == '__main__':
    unittest.main()
