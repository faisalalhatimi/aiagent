from functions.run_python_file import run_python_file


def print_result(file_path: str, content: list[str] | None = None) -> None:
    result = run_python_file("calculator", file_path, content)
    print(result)

print_result("main.py")
print_result("main.py", ["3 + 5"])
print_result("tests.py")
print_result("../main.py")
print_result("nonexistent.py")
print_result("lorem.txt")
