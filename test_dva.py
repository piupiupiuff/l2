import unittest
from io import StringIO
import sys
import dva

class TestDva(unittest.TestCase):
    def test_length(self):
        self.assertTrue(dva.length('Q1!asdasd'))
        self.assertFalse(dva.length('q123!#'))

    def test_digit(self):
        self.assertTrue(dva.digit('Q1!asdasd'))
        self.assertFalse(dva.digit('QWEasd!@#'))

    def test_uppercase(self):
        self.assertTrue(dva.uppercase('QjhsvW@'))
        self.assertFalse(dva.uppercase('23asd!@#'))

    def test_lowercase(self):
        self.assertTrue(dva.lowercase('asd'))
        self.assertFalse(dva.lowercase('QW!@'))

    def test_spec_char(self):
        self.assertTrue(dva.special_char('!@#'))
        self.assertFalse(dva.special_char('fse124QQ'))

    def test_input_from_stdin(self):
        sys.stdin = StringIO("Qwe123qqq\n")
        self.assertEqual(dva.enter_password(), "Qwe123qqq")

    def test_error_message_in_stderr(self):
        sys.stdin = StringIO("invalid_password\n")
        sys.stderr = StringIO()
        self.assertEqual(dva.validate_password('invalid_password'), False)
        error_message = sys.stderr.getvalue()
        self.assertIn("Пароль не відповідає критеріям", error_message)

    def test_exit_code(self):
        sys.stdin = StringIO("Qwe123!qqq\n")
        self.assertTrue(dva.validate_password('Qwe123!qqq'))

    def test_exit_code_valid_password(self):
        sys.stdin = StringIO("Qwe123qqq\n")
        with self.assertRaises(SystemExit) as cm:
            dva.validate_password('Qwe123qqq')
        self.assertEqual(cm.exception.code, 0)

    def test_exit_code_invalid_password(self):
        sys.stdin = StringIO("invalid_password\n")
        with self.assertRaises(SystemExit) as cm:
            dva.validate_password('invalid_password')
        self.assertNotEqual(cm.exception.code, 0)