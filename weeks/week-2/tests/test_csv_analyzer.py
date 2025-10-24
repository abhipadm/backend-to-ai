"""
Unit Tests for CSV Analyzer - Week 2
Tests for statistical analysis functions with your refactored architecture
"""

import unittest
import sys
from pathlib import Path

# Add src to path for imports
current_dir = Path(__file__).parent
src_path = current_dir.parent / 'src'
sys.path.insert(0, str(src_path))

from analyzers.csv_analyzer import analyse_csv_data

class TestCSVAnalyzer(unittest.TestCase):
    """Test cases for CSV data analysis functions"""
    
    def setUp(self):
        """Set up test data for analysis tests"""
        # Sample employee data for testing
        self.employee_data = [
            {"name": "Alice", "age": "25", "salary": "75000", "experience": "3"},
            {"name": "Bob", "age": "30", "salary": "80000", "experience": "5"},
            {"name": "Charlie", "age": "35", "salary": "90000", "experience": "10"},
            {"name": "Diana", "age": "28", "salary": "85000", "experience": "7"}
        ]
        
        # Data with missing values for edge case testing
        self.messy_data = [
            {"name": "Alice", "salary": "75000", "experience": "3"},
            {"name": "Bob", "salary": "", "experience": "5"},
            {"name": "Charlie", "salary": "90000", "experience": ""},
            {"name": "Diana", "salary": "NA", "experience": "7"},
            {"name": "Eve", "salary": "", "experience": None}
        ]
        
        # Non-numeric data for error testing
        self.text_data = [
            {"name": "Alice", "department": "Engineering", "level": "Senior"},
            {"name": "Bob", "department": "Marketing", "level": "Junior"},
            {"name": "Charlie", "department": "Sales", "level": "Manager"}
        ]
    
    def test_salary_analysis_basic(self):
        """Test basic salary analysis with clean data"""
        result = analyse_csv_data(self.employee_data, "salary")
        
        self.assertIsNotNone(result, "Should return analysis results")
        self.assertEqual(result["row_count"], 4, "Should count all rows")
        self.assertEqual(result["non_null_count"], 4, "Should count all valid salaries")
        
        # Test statistical calculations
        self.assertEqual(result["mean"], 82500.0, "Mean salary should be 82,500")
        self.assertEqual(result["min"], 75000.0, "Min salary should be 75,000")
        self.assertEqual(result["max"], 90000.0, "Max salary should be 90,000")
    
    def test_experience_analysis_basic(self):
        """Test basic experience analysis with clean data"""
        result = analyse_csv_data(self.employee_data, "experience")
        
        self.assertIsNotNone(result, "Should return analysis results")
        self.assertEqual(result["non_null_count"], 4, "Should count all valid experience values")
        
        # Test statistical calculations
        self.assertEqual(result["mean"], 6.25, "Mean experience should be 6.25 years")
        self.assertEqual(result["min"], 3.0, "Min experience should be 3 years")
        self.assertEqual(result["max"], 10.0, "Max experience should be 10 years")
    
    def test_analysis_with_missing_data(self):
        """Test analysis with missing/null/empty values"""
        result = analyse_csv_data(self.messy_data, "salary")
        
        self.assertIsNotNone(result, "Should handle messy data")
        self.assertEqual(result["row_count"], 5, "Should count all rows")
        self.assertEqual(result["non_null_count"], 2, "Should count only valid salaries (Alice, Charlie)")
        
        # Should calculate stats only on valid data (75000, 90000)
        self.assertEqual(result["mean"], 82500.0, "Mean should be calculated from valid data only")
        self.assertEqual(result["min"], 75000.0, "Min should be from valid data")
        self.assertEqual(result["max"], 90000.0, "Max should be from valid data")
    
    def test_analysis_with_non_numeric_data(self):
        """Test analysis with non-numeric column data"""
        result = analyse_csv_data(self.text_data, "department")
        
        self.assertIsNotNone(result, "Should return result even for non-numeric data")
        self.assertEqual(result["row_count"], 3, "Should count all rows")
        self.assertEqual(result["non_null_count"], 3, "Should count all non-null text values")
        
        # Non-numeric data should return N/A for statistical measures
        self.assertEqual(result["mean"], "N/A (non-numeric data)")
        self.assertEqual(result["min"], "N/A (non-numeric data)")
        self.assertEqual(result["max"], "N/A (non-numeric data)")
    
    def test_analysis_with_invalid_column(self):
        """Test analysis with non-existent column name"""
        result = analyse_csv_data(self.employee_data, "nonexistent_column")
        
        self.assertIsNotNone(result, "Should return result with basic info")
        self.assertEqual(result["row_count"], 4, "Should still count rows")
        
        # Should not have statistical data for invalid column
        self.assertNotIn("mean", result, "Should not have mean for invalid column")
        self.assertNotIn("min", result, "Should not have min for invalid column")
        self.assertNotIn("max", result, "Should not have max for invalid column")
    
    def test_analysis_with_empty_data(self):
        """Test analysis with empty dataset"""
        result = analyse_csv_data([], "salary")
        
        self.assertIsNone(result, "Should return None for empty data")
    
    def test_column_names_detection(self):
        """Test that column names are correctly detected"""
        result = analyse_csv_data(self.employee_data, "salary")
        
        expected_columns = ["name", "age", "salary", "experience"]
        self.assertEqual(sorted(result["column_names"]), sorted(expected_columns), 
                        "Should detect all column names correctly")
    
    def test_analysis_with_all_null_values(self):
        """Test analysis when all values in column are null/empty"""
        null_data = [
            {"name": "Alice", "salary": ""},
            {"name": "Bob", "salary": None},
            {"name": "Charlie", "salary": "NA"}
        ]
        
        result = analyse_csv_data(null_data, "salary")
        
        self.assertIsNotNone(result, "Should handle all-null data")
        self.assertEqual(result["non_null_count"], 0, "Should count zero non-null values")
        self.assertEqual(result["mean"], "N/A (no non-null values)")
        self.assertEqual(result["min"], "N/A (no non-null values)")
        self.assertEqual(result["max"], "N/A (no non-null values)")
    
    def test_data_cleaning_patterns(self):
        """Test that data cleaning identifies correct patterns"""
        # Test data with various null patterns
        mixed_data = [
            {"score": "85"},      # Valid
            {"score": "90"},      # Valid  
            {"score": ""},        # Empty string - should be filtered
            {"score": None},      # None - should be filtered
            {"score": "NA"},      # NA marker - should be filtered
            {"score": "95"}       # Valid
        ]
        
        result = analyse_csv_data(mixed_data, "score")
        
        # Should only count the valid numeric values (85, 90, 95)
        self.assertEqual(result["non_null_count"], 3, "Should filter out null patterns correctly")
        self.assertEqual(result["mean"], 90.0, "Mean should be calculated from clean data")

if __name__ == "__main__":
    unittest.main(verbosity=2)
