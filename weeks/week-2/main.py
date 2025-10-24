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

from src.file_handlers.csv_handler import read_csv_as_dicts, write_csv_from_dicts
from src.file_handlers.json_handler import read_json_file, write_json_file
from src.analyzers.csv_analyzer import analyse_csv_data

def main():
    """Main demonstration function for Week 2 concepts."""
    
    print("="*60)
    print("WEEK 2 DEMO: Python Modules, Functions & Data Analysis")
    print("="*60)
    
    # Demonstrate module imports and function usage
    print("\n1. Module Import Demo:")
    print("✅ Successfully imported from custom modules!")
    print("   - file_handlers.csv_handler")
    print("   - file_handlers.json_handler")
    
    # Load and display data using our modules
    print("\n2. CSV Data Loading Demo:")
    # Use correct path relative to main.py location
    data_path = Path(__file__).parent / "data" / "sample.csv"
    employees = read_csv_as_dicts(str(data_path))
    
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

    # Analyze salary data
    print("\n💰 SALARY ANALYSIS:")
    salary_stats = analyse_csv_data(employees, "salary")
    if salary_stats:
        print(f"  • Total employees: {salary_stats['row_count']}")
        print(f"  • Valid salary records: {salary_stats.get('non_null_count', 'N/A')}")
        print(f"  • Average salary: ${salary_stats.get('mean', 0):,.2f}")
        print(f"  • Minimum salary: ${salary_stats.get('min', 0):,.2f}")
        print(f"  • Maximum salary: ${salary_stats.get('max', 0):,.2f}")
    
    # Analyze experience data
    print("\n📈 EXPERIENCE ANALYSIS:")
    exp_stats = analyse_csv_data(employees, "experience")
    if exp_stats:
        print(f"  • Valid experience records: {exp_stats.get('non_null_count', 'N/A')}")
        print(f"  • Average experience: {exp_stats.get('mean', 0):.1f} years")
        print(f"  • Minimum experience: {exp_stats.get('min', 0)} years")
        print(f"  • Maximum experience: {exp_stats.get('max', 0)} years")
    
    print("\n" + "="*50)
    print("🎉 Week 2 Mini-task: CSV Summarizer - COMPLETED!")
    print("✅ Professional data analysis with error handling")
    print("✅ Clean, maintainable code structure")
    print("✅ Comprehensive statistical calculations")
    
    print("\n" + "="*60)
    print("Week 2 Module Structure:")
    print("src/")
    print("  ├── __init__.py              # Package initialization")
    print("  ├── file_handlers/           # File I/O module")
    print("  │   ├── __init__.py")
    print("  │   ├── json_handler.py     # JSON operations")
    print("  │   └── csv_handler.py      # CSV operations")
    print("  └── analyzers/              # Data analysis module")
    print("      ├── __init__.py")
    print("      └── csv_analyzer.py     # Statistical analysis")
    print("="*60)
    
    return employees

if __name__ == "__main__":
    employees = main()
    print(f"\n🎯 Ready for CSV Analysis with {len(employees) if employees else 0} records!")