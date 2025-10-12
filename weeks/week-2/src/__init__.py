"""
Week 2 Learning Package - Python Functions, Modules, and Data Analysis

This package contains:
- file_handlers: JSON and CSV file I/O utilities (renamed from 'readers')
- analyzers: Data analysis and statistics utilities
- tests: Comprehensive test suite

Week 2 Goals:
- Python functions and modules
- File I/O operations  
- CSV data analysis (avg, min, max)
- LeetCode practice problems
"""

__version__ = "1.0.0"
__author__ = "Abhi"

# Make key functions available at package level
from .file_handlers.json_handler import read_json_file, write_json_file
from .file_handlers.csv_handler import read_csv_as_dicts, write_csv_from_dicts

__all__ = [
    'read_json_file',
    'write_json_file', 
    'read_csv_as_dicts',
    'write_csv_from_dicts'
]