import csv
from pathlib import Path
from typing import Union, List, Dict, Any, Optional

def read_csv_as_dicts(file_path: Union[str, Path]) -> Optional[List[Dict[str, Any]]]:
    """Reads CSV file and returns list of dictionaries (each row as dict)."""
    try:
        if Path(file_path).is_absolute():
            full_path = Path(file_path)
        else:
            script_dir = Path(__file__).parent
            full_path = script_dir / file_path
        #newline='' parameter - This is important for CSV files! Shows you understand CSV nuances
        with open(full_path, mode='r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            data = [dict(row) for row in reader]
        return data
    
    except FileNotFoundError as fnf_error:
        print(f"Error: The file {file_path} was not found. Error details: {fnf_error}")
    except PermissionError as perm_error:
        print(f"Error: Permission denied to read {file_path}. Error details: {perm_error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    return None

def write_csv_from_dicts(data: List[Dict[str, Any]], file_path: Union[str, Path], fieldnames: Optional[List[str]] = None) -> bool:
    """Writes list of dictionaries to CSV file."""
    try:
        if Path(file_path).is_absolute():
            full_path = Path(file_path)
        else:
            script_dir = Path(__file__).parent
            full_path = script_dir / file_path
        
        # Create parent directories if they don't exist
        full_path.parent.mkdir(parents=True, exist_ok=True)

        if not fieldnames and data:
            fieldnames = list(data[0].keys())

        if not fieldnames:
            raise ValueError("No fieldnames provided and data is empty.")

        with open(full_path, mode='w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        return True
    
    except PermissionError as perm_error:
        print(f"Error: Permission denied to write to {file_path}. Error details: {perm_error}")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")
    
    return False

if __name__ == "__main__":

    employees = read_csv_as_dicts("../../data/sample.csv")
    if employees:
        for employee in employees:
            print(f"{employee['name']} works as {employee['role']}")  # Easy access!
    else:
        print("No data found or error reading the CSV file.")
    
    # Test writing to a new CSV file
    print("\n" + "="*50)
    print("Testing CSV Writer with Auto-Directory Creation and read-back verification")
    print("\n")

    new_employees = [
        {"name": "Charlie", "role": "Manager"},
        {"name": "Diana", "role": "Designer"}
    ]
    success = write_csv_from_dicts(new_employees, "../../data/output/new_employees.csv")
    if success:
        print("Successfully wrote new_employees.csv")
    else:
        print("Failed to write new_employees.csv")
    print("\n" + "-"*50)

    # Read back the written file to verify
    verified_data = read_csv_as_dicts("../../data/output/new_employees.csv")
    if verified_data:
        print("Verified written data:")
        for emp in verified_data:
            print(f"{emp['name']} works as {emp['role']}")
    else:
        print("Failed to read back the written CSV file.")
    print("="*50 + "\n")