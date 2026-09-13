import ast
from pathlib import Path


SRC_DIR = Path("src")
TESTS_DIR = Path("tests")


def public_functions(path):
    tree = ast.parse(path.read_text())
    return [
        node.name
        for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef) and not node.name.startswith("_")
    ]


def test_text():
    return "\n".join(path.read_text() for path in TESTS_DIR.glob("test_*.py"))


def main():
    tests = test_text()
    findings = []

    for source_path in SRC_DIR.glob("*.py"):
        for function_name in public_functions(source_path):
            if function_name not in tests:
                findings.append(f"{source_path}:{function_name} sem teste dedicado")

    if findings:
        print("Possiveis sinais de divida tecnica:")
        for finding in findings:
            print(f"- {finding}")
    else:
        print("Nenhuma funcao publica sem teste dedicado foi encontrada.")


if __name__ == "__main__":
    main()
