#!/usr/bin/python3
"""Test cases for the console"""
import os
import datetime
import uuid
import unittest
from unittest.mock import patch
from models import storage
from console import HBNBCommand
from models.engine.file_storage import FileStorage
from io import StringIO
from models.base_model import BaseModel


class TestHBNBCommand_prompting(unittest.TestCase):
    """Unittest of the custom command prompt(hbnb)"""
    """@patch('sys.stdout', new_callable=StringIO)
    def test_do_EOF(self, mock_stdout):
        """"""
        with patch('builtins.input', return_value='EOF'):
            with patch('os._exit') as mock_exit, patch('sys.stdout', new=StringIO()) as f:
                result = HBNBCommand().onecmd("EOF")
                self.assertTrue(result)
                self.assertEqual(f.getvalue(), '')
                mock_exit.assert_called_once_with(0)
"""
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
    
    def test_emptyline(self):
        """Test empty line input"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
            self.assertEqual('', f.getvalue())

if __name__ == '__main__':
    unittest.main()
