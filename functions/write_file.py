import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    working_directory_abs = os.path.abspath(working_directory)
    target_file_path = os.path.normpath(os.path.join(working_directory_abs, file_path))
    valid_file_path = os.path.commonpath([working_directory_abs, target_file_path]) == working_directory_abs
    valid_directory = os.path.isdir(target_file_path)

    try:
        if not valid_file_path:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        elif valid_directory:
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        os.makedirs(os.path.dirname(target_file_path), exist_ok=True)
        with open(target_file_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"
