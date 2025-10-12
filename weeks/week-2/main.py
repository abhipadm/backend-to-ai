"""
Week 2 Main Demo - Python Modules and Functions

Demonstrates:
1. Importing and using custom modules
2. Function organization and modularity  
3. Professional Python project structure
4. CSV data analysis workflow

Run this to see Week 2 concepts in action!
"""

import sys
from pathlib import Path

# Add src to path for imports
src_path = Path(__file__).parent / 'src'
sys.path.insert(0, str(src_path))

from src.readers import read_csv_as_dicts, write_csv_from_dicts
from src.readers import read_json_file, write_json_file

def main():
    """Main demonstration function for Week 2 concepts."""
    
    print("="*60)
    print("WEEK 2 DEMO: Python Modules, Functions & Data Analysis")
    print("="*60)
    
    # Demonstrate module imports and function usage
    print("\n1. Module Import Demo:")
    print("✅ Successfully imported from custom modules!")
    print("   - readers.csv_reader")
    print("   - readers.json_reader")
    
    # Load and display data using our modules
    print("\n2. CSV Data Loading Demo:")
    employees = read_csv_as_dicts("data/sample.csv")
    
    if employees:
        print(f"✅ Loaded {len(employees)} employee records")
        print("Sample records:")
        for emp in employees[:3]:  # Show first 3
            print(f"   {emp['name']}: {emp['role']} ({emp['experience']} years)")
    
    # Demonstrate function modularity  
    print("\n3. Function Modularity Demo:")
    print("✅ Each operation is cleanly separated:")
    print("   - File reading: isolated function")
    print("   - Data processing: dedicated functions") 
    print("   - Error handling: consistent across modules")
    
    print("\n" + "="*60)
    print("Week 2 Module Structure:")
    print("src/")
    print("  ├── __init__.py          # Package initialization")
    print("  ├── readers/             # File I/O module")
    print("  │   ├── __init__.py")
    print("  │   ├── json_reader.py")
    print("  │   └── csv_reader.py")
    print("  └── analyzers/           # Data analysis module (next)")
    print("      └── __init__.py")
    print("="*60)
    
    return employees

if __name__ == "__main__":
    employees = main()
    print(f"\n🎯 Ready for CSV Analysis with {len(employees) if employees else 0} records!")