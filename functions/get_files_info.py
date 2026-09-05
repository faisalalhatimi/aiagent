import os


def get_files_info(working_directory: str, directory: str=".") -> str:
    working_directory_abs = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_directory_abs, directory))
    valid_target_dir = os.path.commonpath([working_directory_abs, target_dir]) == working_directory_abs
    valid_dir = os.path.isdir(target_dir)
    target_dir_content: list[str] = []

    try:
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        elif not valid_dir:
            return f'Error: "{directory}" is not a directory'
        for content in os.listdir(target_dir):
            content_string = f"- {content}: file_size={os.path.getsize(os.path.join(target_dir, content))}, is_dir={os.path.isdir(os.path.join(target_dir, content))}"
            target_dir_content.append(content_string)
        return "\n".join(target_dir_content)
    except Exception as e:
        return f"Error: {e}"
