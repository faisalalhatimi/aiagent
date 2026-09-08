import os
import subprocess


def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    working_directory_abs = os.path.abspath(working_directory)
    target_file_path = os.path.normpath(os.path.join(working_directory_abs, file_path))
    valid_file_path = os.path.commonpath([working_directory_abs, target_file_path]) == working_directory_abs
    valid_file = os.path.isfile(target_file_path)
    command = ["python", target_file_path]
    output: list[str] = []
    try:
        if not valid_file_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        elif not valid_file:
            return f'Error: "{file_path}" does not exist or is not a regular file'
        elif not file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'
        if args != None:
            command.extend(args)
        result = subprocess.run(command, cwd=working_directory_abs, capture_output=True, text=True, timeout=30)
        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")
        if result.stdout == "" and result.stderr == "":
            output.append("No output produced")
        if result.stdout:
            output.append(f"STDOUT: {result.stdout}")
        if result.stderr:
            output.append(f"STDERR: {result.stderr}")
        return "\n".join(output)
    except Exception as e:
        return f"Error: executing Python file: {e}"

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Executes a Python file relative to the working directory with optional command-line arguments and returns its output",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the Python file to execute, relative to the working directory",
                },
                "args": {
                    "type": "array",
                    "items": {
                        "type": "string",
                    },
                    "description": "Optional command-line arguments to pass to the Python file",
                },
            },
            "required": ["file_path"],
        },
    },
}
