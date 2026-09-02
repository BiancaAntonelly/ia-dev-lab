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

    def test_configurable_greeting_uses_pt_br_morning(self):
        greeting = hello.build_configurable_greeting(
            name="Bianca",
            language="pt-BR",
            period="manha",
        )

        self.assertEqual("Bom dia, Bianca!", greeting)

    def test_configurable_greeting_uses_default_name_for_blank_name(self):
        greeting = hello.build_configurable_greeting(
            name="   ",
            language="pt-BR",
            period="tarde",
        )

        self.assertEqual("Boa tarde, IA!", greeting)

    def test_configurable_greeting_falls_back_to_pt_br_for_unknown_language(self):
        greeting = hello.build_configurable_greeting(
            name="Bianca",
            language="es",
            period="noite",
        )

        self.assertEqual("Boa noite, Bianca!", greeting)

    def test_configurable_greeting_uses_neutral_message_for_unknown_period(self):
        greeting = hello.build_configurable_greeting(
            name="Bianca",
            language="pt-BR",
            period="madrugada",
        )

        self.assertEqual("Ola, Bianca!", greeting)

    def test_configurable_greeting_supports_english(self):
        greeting = hello.build_configurable_greeting(
            name="Ada",
            language="en",
            period="noite",
        )

        self.assertEqual("Good evening, Ada!", greeting)

    def test_main_prints_greeting(self):
        output = io.StringIO()

        with redirect_stdout(output):
            hello.main()

        self.assertIn("Ambiente de IA para desenvolvimento configurado", output.getvalue())


if __name__ == "__main__":
    unittest.main()
