import unittest

from opres import Ok, Err
from opres import Some, Nothing


class TestResult(unittest.TestCase):
    def test_unwrap(self):
        res_var = Ok(10)
        self.assertEqual(res_var.unwrap(), 10)

        res_var = Ok("10")
        self.assertEqual(res_var.unwrap(), "10")

        res_var = Ok(None)
        self.assertEqual(res_var.unwrap(), None)

        res_var = Ok(Err(RuntimeError("error")))
        self.assertEqual(res_var.unwrap(), Err(RuntimeError("error")))

        res_var = Err("error")
        self.assertRaises(SystemExit, res_var.unwrap)

    def test_unwrap_err(self):
        res_var = Ok(10)
        self.assertRaises(SystemExit, res_var.unwrap_err)

        res_var = Err("error")
        self.assertEqual(res_var.unwrap_err(), "error")

    def test_unwrap_or(self):
        res_var = Ok(10)
        self.assertEqual(res_var.unwrap_or(0), 10)

        res_var = Ok(True)
        self.assertEqual(res_var.unwrap_or(False), True)

        res_var = Err("error")
        self.assertEqual(res_var.unwrap_or(0), 0)

    def test_unwrap_or_else(self):
        res_var = Ok(10)
        self.assertEqual(res_var.unwrap_or_else(lambda: 0), 10)

        res_var = Err("error")
        self.assertEqual(res_var.unwrap_or_else(lambda: 0), 0)

    def test_is_ok(self):
        res_var = Ok(10)
        self.assertEqual(res_var.is_ok(), True)

        res_var = Err("error")
        self.assertEqual(res_var.is_ok(), False)

    def test_is_err(self):
        res_var = Ok(10)
        self.assertEqual(res_var.is_err(), False)

        res_var = Err("error")
        self.assertEqual(res_var.is_err(), True)

    def test_expect(self):
        res_var = Err("error")
        self.assertRaises(SystemExit, res_var.expect, "message")
        try:
            res_var.expect("message")
        except SystemExit as e:
            self.assertEqual(str(e), "message")

    def test_map(self):
        res_var = Ok(["1", "2", "3"])
        length = res_var.map(len)
        self.assertEqual(length, Ok(3))

        res_var = Err("error")
        length = res_var.map(len)
        self.assertEqual(length, Err("error"))

    def test_map_or(self):
        res_var = Ok(["1", "2", "3"])
        length = res_var.map_or(len, 0)
        self.assertEqual(length, Ok(3))

        res_var = Err("error")
        length = res_var.map_or(len, 0)
        self.assertEqual(length, Ok(0))

    def test_map_or_else(self):
        res_var = Ok(["1", "2", "3"])
        length = res_var.map_or_else(len, lambda: 0)
        self.assertEqual(length, Ok(3))

        res_var = Err("error")
        length = res_var.map_or_else(len, lambda: 0)
        self.assertEqual(length, Ok(0))

    def test_ok(self):
        res_var = Ok(["1", "2", "3"])
        self.assertEqual(res_var.ok(), Some(["1", "2", "3"]))

        res_var = Err("error")
        self.assertEqual(res_var.ok(), Nothing())

    def test_err(self):
        res_var = Ok(["1", "2", "3"])
        self.assertEqual(res_var.err(), Nothing())

        res_var = Err("error")
        self.assertEqual(res_var.err(), Some("error"))


if __name__ == '__main__':
    unittest.main()
