#!/usr/bin/python3
"""Test cases for the console"""
import unittest
from unittest.mock import patch
from models import storage
from console import HBNBCommand
from models.engine.file_storage import FileStorage
from io import StringIO


class TestHBNBCommand_prompting(unittest.TestCase):
    """Unittest of the custom command prompt(hbnb)"""

    def test_prompt_string(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

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
            result = HBNBCommand().onecmd("BaseModel 45678")
            self.assertFalse(result)
            exp_out = mock_stdout.getvalue().strip()
            out = (
                    exp_out, '[BaseModel] (45678) {'\
                            '\'first_name\': \'Betty\', \'id\': \'45678\',' \
                            ' \'created_at\': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293),' \
                            ' \'updated_at\': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}'
                            )
            self.assertEqual(exp_out, out)

if __name__ == '__main__':
    unittest.main()
