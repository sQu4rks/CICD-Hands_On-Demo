import unittest

from guestbook.utils import get_entry

class TestEntry(unittest.TestCase):
    def test_succesful_init(self):
        e = get_entry("text", "author")
        self.assertIsNotNone(e)

    def test_none_arg_raises_exception(self):
        self.assertRaises(Exception, get_entry, "text", None)
        self.assertRaises(Exception, get_entry, None, "author")
        self.assertRaises(Exception, get_entry, None, None)

    def test_keys_present(self):
        e = get_entry("text", "author")

        self.assertIn("text", e)
        self.assertIn("author", e)
        self.assertIn("timestamp", e)
        