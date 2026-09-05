from functions.get_file_content import get_file_content


lorem_result = get_file_content("calculator", "lorem.txt")
print(f"lorem.txt length: {len(lorem_result)}")
print(f"lorem.txt truncated: {'truncated' in lorem_result}")


def print_result(file_path: str, label: str |None=None) -> None:
    if label is None:
        label = file_path
    result = get_file_content("calculator", file_path)
    print(f" Result for {label} file:\n{result}")


print_result("main.py")
print_result("pkg/calculator.py")
print_result("/bin/cat")
print_result("pkg/does_not_exist.py")
