import unittest

from src.prompt_validator import validate_prompt


class PromptValidatorTest(unittest.TestCase):
    def test_complete_prompt_is_valid(self):
        prompt = (
            "No contexto do projeto ia-dev-lab, implemente um validador de prompts. "
            "Restricoes: nao adicione dependencias externas. "
            "Validacao: rode os testes com unittest."
        )

        result = validate_prompt(prompt)

        self.assertTrue(result["is_valid"])
        self.assertEqual([], result["missing"])

    def test_generic_prompt_is_invalid(self):
        result = validate_prompt("crie uma funcao")

        self.assertFalse(result["is_valid"])
        self.assertIn("contexto", result["missing"])
        self.assertIn("restricoes", result["missing"])
        self.assertIn("validacao", result["missing"])

    def test_partial_prompt_reports_missing_validation(self):
        prompt = "No contexto do projeto ia-dev-lab, crie uma tarefa simples com restricoes claras."

        result = validate_prompt(prompt)

        self.assertFalse(result["is_valid"])
        self.assertIn("validacao", result["missing"])

    def test_non_text_prompt_is_invalid(self):
        result = validate_prompt(None)

        self.assertFalse(result["is_valid"])
        self.assertEqual(
            ["contexto", "tarefa", "restricoes", "validacao"],
            result["missing"],
        )


if __name__ == "__main__":
    unittest.main()
