def write_file(file_path, content):
    try:
        with open(file_path, "w") as file:
            file.write(content)
        return f"File '{file_path}' written successfully."
    except Exception as e:
        return f"Error writing file: {e}"