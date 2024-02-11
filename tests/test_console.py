#!/usr/bin/python3
""" unittest for console"""

import sys
import unittest
from io import StringIO

import models
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Test suite for the console module"""

    def setUp(self):
        """Set up testing environment by
        redirecting stdout to a StringIO object"""
        self.stdout_backup = sys.stdout
        self.stdout_mock = StringIO()
        sys.stdout = self.stdout_mock

    def tearDown(self):
        """Reset stdout to its original state after each test"""
        sys.stdout = self.stdout_backup

    def create_console_instance(self):
        """Create an instance of the HBNBCommand class"""
        return HBNBCommand()

    def test_quit_command(self):
        """Test that the 'quit' command exists and works correctly"""
        console = self.create_console_instance()
        self.assertTrue(console.onecmd("quit"))

    def test_EOF_command(self):
        """Test that the 'EOF' command exists and works correctly"""
        console = self.create_console_instance()
        self.assertTrue(console.onecmd("EOF"))

    def test_all_command(self):
        """Test that the 'all' command exists and works correctly"""
        console = self.create_console_instance()
        console.onecmd("all")
        self.assertTrue(isinstance(self.stdout_mock.getvalue(), str))

    def test_show_command(self):
        """
        Test that the 'show' command exists and works correctly
        """
        console = self.create_console_instance()
        console.onecmd("create User")
        user_id = self.stdout_mock.getvalue().strip()
        sys.stdout = self.stdout_backup
        self.stdout_mock.close()
        self.stdout_mock = StringIO()
        sys.stdout = self.stdout_mock
        console.onecmd(f"show User {user_id}")
        output = self.stdout_mock.getvalue()
        sys.stdout = self.stdout_backup
        self.assertTrue(isinstance(output, str))

    def test_show_command_missing_class_name(self):
        """
        Test that the 'show' command correctly
        handles the case where the class name is missing
        """
        console = self.create_console_instance()
        console.onecmd("show")
        output = self.stdout_mock.getvalue()
        sys.stdout = self.stdout_backup
        self.assertEqual("** class name missing **\n", output)

    def test_show_command_missing_id(self):
        """
        Test that the 'show' command correctly
        handles the case where the instance id is missing
        """
        console = self.create_console_instance()
        console.onecmd("show User")
        output = self.stdout_mock.getvalue()
        sys.stdout = self.stdout_backup
        self.assertEqual("** instance id missing **\n", output)

    def test_show_command_no_instance_found(self):
        """
        Test that the 'show' command correctly handles
        the case where the instance is not found
        """
        console = self.create_console_instance()
        console.onecmd("show User 124356876")
        output = self.stdout_mock.getvalue()
        sys.stdout = self.stdout_backup
        self.assertEqual("** no instance found **\n", output)

    def test_create_command(self):
        """
        Test that the 'create' command works correctly
        """
        console = self.create_console_instance()
        console.onecmd("create User")
        output = self.stdout_mock.getvalue()
        self.assertTrue(isinstance(output, str))

    def test_create_command_missing_class_name(self):
        """
        Test that the 'create' command correctly handles the case where the
        class name is missing
        """
        console = self.create_console_instance()
        console.onecmd("create")
        output = self.stdout_mock.getvalue()
        self.assertEqual("** class name missing **\n", output)

    def test_create_command_nonexistent_class(self):
        """
        Test that the 'create' command correctly handles the case where the
        class name does not exist
        """
        console = self.create_console_instance()
        console.onecmd("create Binita")
        output = self.stdout_mock.getvalue()
        self.assertEqual("** class doesn't exist **\n", output)

    def test_update_command_missing_class_name(self):
        """
        Test that the 'update' command correctly handles
        the case where the class name is missing
        """
        console = self.create_console_instance()
        console.onecmd("update")
        output = self.stdout_mock.getvalue()
        self.assertEqual("** class name missing **\n", output)

    def test_update_command_missing_id(self):
        """
        Test that the 'update' command correctly handles
        the case where the instance id is missing
        """
        console = self.create_console_instance()
        console.onecmd("update User")
        output = self.stdout_mock.getvalue()
        self.assertEqual("** instance id missing **\n", output)

    def test_update_command_missing_attribute_name(self):
        """
        Test that the 'update' command correctly handles
        the case where the attribute name is missing
        """
        console = self.create_console_instance()
        console.onecmd("update User 1234")
        output = self.stdout_mock.getvalue()
        self.assertEqual("** no instance found **\n", output)

    def test_update_command_missing_value(self):
        """
        Test that the 'update' command correctly handles
        the case where the value is missing
        """
        console = self.create_console_instance()
        console.onecmd("update User 1234 first_name")
        output = self.stdout_mock.getvalue()
        self.assertEqual("** no instance found **\n", output)

    def test_update_command_nonexistent_class(self):
        """
        Test that the 'update' command correctly handles
        the case where the class name does not exist
        """
        console = self.create_console_instance()
        console.onecmd("update Binita 1234 first_name 'John'")
        output = self.stdout_mock.getvalue()
        self.assertEqual("** class doesn't exist **\n", output)

    def test_update_command_no_instance_found(self):
        """
        Test that the 'update' command correctly handles
        the case where the instance is not found
        """
        console = self.create_console_instance()
        console.onecmd("update User 1234 first_name 'John'")
        output = self.stdout_mock.getvalue()
        self.assertEqual("** no instance found **\n", output)


if __name__ == "__main__":
    unittest.main()
