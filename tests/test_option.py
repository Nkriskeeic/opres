import unittest
from opres import Some, Nothing
from opres import Ok, Err


class TestOption(unittest.TestCase):
    def test_unwrap(self):
        some_var = Some(10)
        self.assertEqual(some_var.unwrap(), 10)

        some_var = Some("10")
        self.assertEqual(some_var.unwrap(), "10")

        some_var = Some(None)
        self.assertEqual(some_var.unwrap(), None)

        some_var = Some(Nothing())
        self.assertEqual(some_var.unwrap(), Nothing())

        some_var = Nothing()
        self.assertRaises(SystemExit, some_var.unwrap)

    def test_unwrap_or(self):
        some_var = Some(10)
        self.assertEqual(some_var.unwrap_or(0), 10)

        some_var = Nothing()
        self.assertEqual(some_var.unwrap_or(0), 0)

    def test_unwrap_or_else(self):
        some_var = Some(10)
        self.assertEqual(some_var.unwrap_or_else(lambda: 0), 10)

        some_var = Nothing()
        self.assertEqual(some_var.unwrap_or_else(lambda: 0), 0)

    def test_is_some(self):
        some_var = Some(10)
        self.assertEqual(some_var.is_some(), True)

        some_var = Nothing()
        self.assertEqual(some_var.is_some(), False)

    def test_is_nothing(self):
        some_var = Some(10)
        self.assertEqual(some_var.is_nothing(), False)

        some_var = Nothing()
        self.assertEqual(some_var.is_nothing(), True)

    def test_expect(self):
        some_var = Some(10)
        self.assertEqual(some_var.expect("message"), 10)

        some_var = Nothing()
        self.assertRaises(SystemExit, some_var.expect, "message")
        try:
            some_var.expect("message")
        except SystemExit as e:
            self.assertEqual(str(e), "message")

    def test_map(self):
        some_var = Some(["1", "2", "3"])
        length = some_var.map(len)
        self.assertEqual(length, Some(3))

        some_var = Nothing()
        length = some_var.map(len)
        self.assertEqual(length, Nothing())

    def test_map_or(self):
        some_var = Some(["1", "2", "3"])
        length = some_var.map_or(len, 0)
        self.assertEqual(length, Some(3))

        some_var = Nothing()
        length = some_var.map_or(len, 0)
        self.assertEqual(length, Some(0))

    def test_map_or_else(self):
        some_var = Some(["1", "2", "3"])
        length = some_var.map_or_else(len, lambda: 0)
        self.assertEqual(length, Some(3))

        some_var = Nothing()
        length = some_var.map_or_else(len, lambda: 0)
        self.assertEqual(length, Some(0))

    def test_ok_or(self):
        some_var = Some(10)
        self.assertEqual(some_var.ok_or(0), Ok(10))

        some_var = Nothing()
        self.assertEqual(some_var.ok_or(0), Err(0))

    def test_ok_or_else(self):
        some_var = Some(10)
        self.assertEqual(some_var.ok_or_else(lambda: 0), Ok(10))

        some_var = Nothing()
        self.assertEqual(some_var.ok_or_else(lambda: 0), Err(0))


if __name__ == '__main__':
    unittest.main()
