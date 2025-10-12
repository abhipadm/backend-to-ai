import json
from pathlib import Path
from typing import Any, Union

def read_json_file(file_path: Union[str, Path]) -> dict | list | None:
    """Reads a JSON file and returns its content as a Python object (dict, list, etc.)."""
    try:
        # Handle both absolute and relative paths correctly
        if Path(file_path).is_absolute():
            full_path = Path(file_path)
        else:
            # Get the directory where the script is located
            script_dir = Path(__file__).parent
            full_path = script_dir / file_path
        
        with open(full_path, 'r') as file:
            data = json.load(file)
        return data
    
    except FileNotFoundError as file_not_found_error:
        print(f"Error: The file {file_path} was not found. Error details: {file_not_found_error}")
    except json.JSONDecodeError as json_decode_error:
        print(f"Error: The file {file_path} is not a valid JSON file. Error details: {json_decode_error}")
    except PermissionError as permission_error:
        print(f"Error: Permission denied to read {file_path}. Error details: {permission_error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return None

def write_json_file(data: Any, file_path: Union[str, Path]) -> bool:
    """function to write a Python object (dict, list, etc.) to a JSON file."""
    try:
        if Path(file_path).is_absolute():
            full_path = Path(file_path)
        else:
            script_dir = Path(__file__).parent
            full_path = script_dir / file_path
        
        # Create parent directories if they don't exist
        full_path.parent.mkdir(parents=True, exist_ok=True)

        with open(full_path, 'w') as file:
            json.dump(data, file, indent=2)
        return True
    except PermissionError as permission_error:
        print(f"Error: Permission denied to write to {file_path}. Error details: {permission_error}")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

    return False



if __name__ == "__main__":
    print("\n" + "="*50)
    print("Testing JSON Writer with Auto-Directory Creation")
    # Test data
    test_data = {
        "project": "Backend to AI Learning",
        "author": "Abhi",
        "skills_learned": ["JSON reading", "JSON writing", "Path handling"],
        "date": "2024-10-09"
    }

    # Test writing to a new file in a nested directory
    success = write_json_file(test_data, "../../data/output/test_output.json")

    if success:
        print("✅ Successfully created file with new directories!")
    
    # Read it back to verify
    verification = read_json_file("../../data/output/test_output.json")
    if verification:
        print("✅ Round-trip test successful!")
        print("Data:", verification)


    # # Test with the existing sample.json
    # result = read_json_file("../../data/sample.json")
    # if result:
    #     print("Successfully loaded JSON:")
    #     print(result)
    #     print(f"Type: {type(result)}")