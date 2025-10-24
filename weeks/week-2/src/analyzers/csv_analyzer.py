import csv
import sys
import os
from pathlib import Path
from typing import Union, List, Dict, Any, Optional

# Add the parent directory to the path so we can import our modules
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from file_handlers.csv_handler import read_csv_as_dicts

def analyse_csv_data(csv_data: List[Dict[str, Any]], column_name: str) -> Optional[Dict[str, Any]]:
    """Reads a CSV file and provides basic analysis like row count and column names."""

    if csv_data is not None:
        if not csv_data:
            print("The CSV file is empty.")
            return None

        # Basic analysis
        row_count = len(csv_data)
        column_names = list(csv_data[0].keys())

        analysis = {
            "row_count": row_count,
            "column_names": column_names,
        }

        if column_name in column_names:
            non_null_values = [row[column_name] for row in csv_data if row[column_name] not in (None, '', 'NA')]
            analysis["non_null_count"] = len(non_null_values)
            if non_null_values:
                try:
                    numeric_values = [float(value) for value in non_null_values]
                    analysis["mean"] = sum(numeric_values) / len(numeric_values)
                    analysis["min"] = min(numeric_values)
                    analysis["max"] = max(numeric_values)
                except ValueError:
                    analysis["mean"] = analysis["min"] = analysis["max"] = "N/A (non-numeric data)"
            else:
                analysis["mean"] = analysis["min"] = analysis["max"] = "N/A (no non-null values)"
        else:
            print(f"Column '{column_name}' not found in the CSV file.")
        
        return analysis

    return None


if __name__ == "__main__":
    print("=== CSV Analyzer Demo ===\n")
    
    # Test with your employee data
    data_path = "../../data/sample.csv"
    
    print("📊 Analyzing Employee Salary Data:")
    salary_analysis = analyse_csv_data(data_path, "salary")
    if salary_analysis:
        print(f"✅ Total employees: {salary_analysis['row_count']}")
        print(f"✅ Available columns: {salary_analysis['column_names']}")
        print(f"✅ Valid salary records: {salary_analysis.get('non_null_count', 'N/A')}")
        print(f"💰 Average salary: ${salary_analysis.get('mean', 'N/A'):,.2f}" if isinstance(salary_analysis.get('mean'), (int, float)) else f"💰 Average salary: {salary_analysis.get('mean', 'N/A')}")
        print(f"📉 Minimum salary: ${salary_analysis.get('min', 'N/A'):,.2f}" if isinstance(salary_analysis.get('min'), (int, float)) else f"📉 Minimum salary: {salary_analysis.get('min', 'N/A')}")
        print(f"📈 Maximum salary: ${salary_analysis.get('max', 'N/A'):,.2f}" if isinstance(salary_analysis.get('max'), (int, float)) else f"📈 Maximum salary: {salary_analysis.get('max', 'N/A')}")
    
    print("\n" + "="*50 + "\n")
    
    print("📊 Analyzing Employee Experience Data:")
    experience_analysis = analyse_csv_data(data_path, "experience")
    if experience_analysis:
        print(f"✅ Valid experience records: {experience_analysis.get('non_null_count', 'N/A')}")
        print(f"📊 Average experience: {experience_analysis.get('mean', 'N/A'):.1f} years" if isinstance(experience_analysis.get('mean'), (int, float)) else f"📊 Average experience: {experience_analysis.get('mean', 'N/A')}")
        print(f"👶 Minimum experience: {experience_analysis.get('min', 'N/A')} years" if isinstance(experience_analysis.get('min'), (int, float)) else f"👶 Minimum experience: {experience_analysis.get('min', 'N/A')}")
        print(f"🧓 Maximum experience: {experience_analysis.get('max', 'N/A')} years" if isinstance(experience_analysis.get('max'), (int, float)) else f"🧓 Maximum experience: {experience_analysis.get('max', 'N/A')}")
    
    print("\n" + "="*50 + "\n")
    
    print("🔍 Testing with invalid column:")
    invalid_test = analyse_csv_data(data_path, "nonexistent_column")
    print("Result:", invalid_test)