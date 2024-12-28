import os
import ast


######################################################
def extract_lists_from_file(file_path: str) -> list:
    lists = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            file_content = file.read()

            # Parse the file content into an AST
            tree = ast.parse(file_content, filename=file_path)

            # Walk through the nodes and look for list objects
            for node in ast.walk(tree):
                if isinstance(node, ast.List):
                    # Attempt to resolve elements of the list
                    elements = []
                    for element in node.elts:
                        try:
                            elements.append(ast.literal_eval(element))
                        except Exception:
                            elements.append("Unresolved_Element")

                    lists.append(elements)
    except (SyntaxError, ValueError, FileNotFoundError, OSError) as e:
        print(f"Error processing {file_path}: {e}")

    return lists

######################################################
def scan_directory_for_lists(directory: str) -> dict[str, list]:
    results = {}

    # Walk through the directory
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                lists = extract_lists_from_file(file_path)
                if lists:
                    results[file_path] = lists

    return results

######################################################
def get_variable_values_from_files(directory: str, variable_names: list) -> dict:

    results = {}
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r') as f:
                        file_contents = f.read()

                    module = {}
                    exec(file_contents, module)

                    file_results = {}
                    for var_name in variable_names:
                        if var_name in module:
                            file_results[var_name] = module[var_name]
                        else:
                            file_results[var_name] = None

                    results[file_path] = file_results

                except Exception as e:
                    print(f"Error processing {file_path}: {e}")

    return results

######################################################
def process_list_screen(input_list: list, dummy_list: list) -> list:

  result = input_list[:3]  # Get the first 3 items (if available)

  # Fill with dummy items if the list is too short
  while len(result) < 3:
    result.append(dummy_list)

  return result

######################################################
def exit_with_message(message: str, exit_code=0):
  """
  Exits the program with a given message and exit code.

  Args:
    message: The message to be printed before exiting.
    exit_code: The exit code to be returned (default: 0 for success).
  """
  print(message)
  sys.exit(exit_code)