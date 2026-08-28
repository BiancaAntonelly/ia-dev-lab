import io
import unittest
from contextlib import redirect_stdout

from src import hello


class HelloTest(unittest.TestCase):
    def test_build_greeting_uses_name(self):
        greeting = hello.build_greeting("Bianca")

        self.assertIn("Ola, Bianca!", greeting)

    def test_build_greeting_uses_default_for_blank_name(self):
        greeting = hello.build_greeting("   ")

        self.assertIn("Ola, IA!", greeting)

    def test_main_prints_greeting(self):
        output = io.StringIO()

        with redirect_stdout(output):
            hello.main()

        self.assertIn("Ambiente de IA para desenvolvimento configurado", output.getvalue())


if __name__ == "__main__":
    unittest.main()
