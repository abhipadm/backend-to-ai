"""
File Handlers Module

Provides utilities for handling different file formats:
- JSON files with error handling and type safety
- CSV files with dictionary-based access

Renamed from 'readers' to 'file_handlers' to better reflect 
the bidirectional nature of operations (both reading AND writing).
"""

from .json_handler import read_json_file, write_json_file
from .csv_handler import read_csv_as_dicts, write_csv_from_dicts

__all__ = [
    'read_json_file',
    'write_json_file',
    'read_csv_as_dicts', 
    'write_csv_from_dicts'
]