import unittest
from parser import ConfigParser


class TestConfigParser(unittest.TestCase):
    def setUp(self):
        self.parser = ConfigParser()

    def test_simple_constant(self):
        config = "x is 42;"
        result = self.parser.parse(config)
        # Ожидаем, что x будет равно 42
        self.assertIn("x", result)
        self.assertEqual(result["x"], 42)

    def test_array(self):
        config = "data is array(1, 2, 3);"
        result = self.parser.parse(config)
        # Ожидаем, что data будет списком [1, 2, 3]
        self.assertIn("data", result)
        self.assertEqual(result["data"], [1, 2, 3])

    def test_nested(self):
        # Define x first before referencing it in settings
        config = 'x is 42; settings is array(@"string", |x|);'
        result = self.parser.parse(config)
        # Expecting settings to contain ["string", 42]
        self.assertIn("settings", result)
        self.assertEqual(result["settings"], ["string", 42])

    def test_constants(self):
        config = "x is 42; y is |x|;"
        result = self.parser.parse(config)
        # Ожидаем, что y будет равно 42, так как |x| подставляется значением 42
        self.assertIn("y", result)
        self.assertEqual(result["y"], 42)

    def test_boolean(self):
        config = "debug is true;"
        result = self.parser.parse(config)
        # Ожидаем, что debug будет True
        self.assertIn("debug", result)
        self.assertTrue(result["debug"])

    def test_string(self):
        config = 'app_name is @"TestApp";'
        result = self.parser.parse(config)
        # Ожидаем, что app_name будет строкой "TestApp"
        self.assertIn("app_name", result)
        self.assertEqual(result["app_name"], "TestApp")


if __name__ == "__main__":
    unittest.main()
