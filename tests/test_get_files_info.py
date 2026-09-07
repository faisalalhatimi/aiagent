from functions.get_files_info import get_files_info


def print_result(directory: str, label: str | None=None) -> None:
    if label is None:
        label = directory
    result = get_files_info("calculator", directory)
    print(f"Result for '{label}' directory:\n{result}")


print_result(".", "current")
print_result("/bin")
print_result("../")
print_result("main.py")
print_result("render.py")
print_result("calculator.py")
