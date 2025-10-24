"""
Unit Tests for File Handlers - Week 2
Tests for CSV and JSON file operations with comprehensive error scenarios
"""

import unittest
import tempfile
import json
import csv
from pathlib import Path
import sys

# Add src to path for imports
current_dir = Path(__file__).parent
src_path = current_dir.parent / 'src'
sys.path.insert(0, str(src_path))

from file_handlers.csv_handler import read_csv_as_dicts, write_csv_from_dicts
from file_handlers.json_handler import read_json_file, write_json_file

class TestCSVHandler(unittest.TestCase):
    """Test cases for CSV file operations"""
    
    def setUp(self):
        """Set up test data for each test case"""
        self.test_data = [
            {"name": "Alice", "age": "25", "salary": "75000"},
            {"name": "Bob", "age": "30", "salary": "80000"},
            {"name": "Charlie", "age": "35", "salary": "90000"}
        ]
        
        # Create temporary directory for test files
        self.temp_dir = tempfile.mkdtemp()
        self.temp_path = Path(self.temp_dir)
    
    def tearDown(self):
        """Clean up temporary files after tests"""
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    def test_write_and_read_csv_round_trip(self):
        """Test writing CSV data and reading it back (round-trip test)"""
        csv_file = self.temp_path / "test_employees.csv"
        
        # Write data (note: your function expects data first, then file_path)
        result = write_csv_from_dicts(self.test_data, str(csv_file))
        self.assertTrue(result, "CSV write should succeed")
        
        # Read data back
        read_data = read_csv_as_dicts(str(csv_file))
        
        # Verify data integrity
        self.assertIsNotNone(read_data, "Should read CSV data successfully")
        self.assertEqual(len(read_data), 3, "Should have 3 records")
        self.assertEqual(read_data[0]["name"], "Alice", "First record name should match")
        self.assertEqual(read_data[1]["salary"], "80000", "Second record salary should match")
    
    def test_read_nonexistent_csv_file(self):
        """Test reading a file that doesn't exist"""
        nonexistent_file = self.temp_path / "nonexistent.csv"
        result = read_csv_as_dicts(str(nonexistent_file))
        self.assertIsNone(result, "Should return None for nonexistent file")
    
    def test_empty_csv_data_write(self):
        """Test writing empty data"""
        csv_file = self.temp_path / "empty.csv"
        result = write_csv_from_dicts([], str(csv_file))
        self.assertFalse(result, "Should return False for empty data")
    
    def test_csv_with_pathlib_path(self):
        """Test CSV operations with pathlib.Path objects"""
        csv_file = self.temp_path / "pathlib_test.csv"
        
        # Test with Path object
        result = write_csv_from_dicts(self.test_data, csv_file)
        self.assertTrue(result, "Should work with pathlib.Path")
        
        read_data = read_csv_as_dicts(csv_file)
        self.assertIsNotNone(read_data, "Should read with pathlib.Path")
        self.assertEqual(len(read_data), 3, "Should have correct number of records")

class TestJSONHandler(unittest.TestCase):
    """Test cases for JSON file operations"""
    
    def setUp(self):
        """Set up test data for each test case"""
        self.test_data = {
            "employees": [
                {"name": "Alice", "age": 25, "salary": 75000},
                {"name": "Bob", "age": 30, "salary": 80000}
            ],
            "company": "TechCorp",
            "location": "Mumbai"
        }
        
        # Create temporary directory for test files
        self.temp_dir = tempfile.mkdtemp()
        self.temp_path = Path(self.temp_dir)
    
    def tearDown(self):
        """Clean up temporary files after tests"""
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    def test_write_and_read_json_round_trip(self):
        """Test writing JSON data and reading it back"""
        json_file = self.temp_path / "test_company.json"
        
        # Write data (note: your function expects data first, then file_path)
        result = write_json_file(self.test_data, str(json_file))
        self.assertTrue(result, "JSON write should succeed")
        
        # Read data back
        read_data = read_json_file(str(json_file))
        
        # Verify data integrity
        self.assertIsNotNone(read_data, "Should read JSON data successfully")
        self.assertEqual(read_data["company"], "TechCorp", "Company name should match")
        self.assertEqual(len(read_data["employees"]), 2, "Should have 2 employees")
        self.assertEqual(read_data["employees"][0]["name"], "Alice", "First employee name should match")
    
    def test_read_nonexistent_json_file(self):
        """Test reading a JSON file that doesn't exist"""
        nonexistent_file = self.temp_path / "nonexistent.json"
        result = read_json_file(str(nonexistent_file))
        self.assertIsNone(result, "Should return None for nonexistent file")
    
    def test_json_with_pathlib_path(self):
        """Test JSON operations with pathlib.Path objects"""
        json_file = self.temp_path / "pathlib_test.json"
        
        # Test with Path object
        result = write_json_file(self.test_data, json_file)
        self.assertTrue(result, "Should work with pathlib.Path")
        
        read_data = read_json_file(json_file)
        self.assertIsNotNone(read_data, "Should read with pathlib.Path")
        self.assertEqual(read_data["location"], "Mumbai", "Should have correct location")
    
    def test_json_with_different_data_types(self):
        """Test JSON with various data types"""
        complex_data = {
            "string": "hello",
            "integer": 42,
            "float": 3.14,
            "boolean": True,
            "null": None,
            "list": [1, 2, 3],
            "nested": {"key": "value"}
        }
        
        json_file = self.temp_path / "complex.json"
        
        # Write and read complex data
        write_result = write_json_file(complex_data, str(json_file))
        self.assertTrue(write_result, "Should write complex data")
        
        read_data = read_json_file(str(json_file))
        self.assertEqual(read_data["integer"], 42, "Integer should be preserved")
        self.assertEqual(read_data["float"], 3.14, "Float should be preserved")
        self.assertTrue(read_data["boolean"], "Boolean should be preserved")
        self.assertIsNone(read_data["null"], "None should be preserved")

if __name__ == "__main__":
    unittest.main(verbosity=2)
