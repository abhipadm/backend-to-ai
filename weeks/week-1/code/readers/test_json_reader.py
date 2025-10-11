import unittest
import tempfile
from pathlib import Path
from json_reader import read_json_file, write_json_file


class TestJsonReader(unittest.TestCase):
    """Unit tests for JSON reader and writer functions."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        # Create a temporary directory for test files
        self.test_dir = tempfile.mkdtemp()
        self.test_file_path = Path(self.test_dir) / "test.json"
        
        # Sample test data
        self.sample_dict = {
            "name": "Test User",
            "age": 25,
            "active": True,
            "scores": [85, 90, 78]
        }
        
        self.sample_list = [
            {"id": 1, "name": "Alice"},
            {"id": 2, "name": "Bob"}
        ]
    
    def tearDown(self):
        """Clean up after each test method."""
        # Remove test files and directory
        import shutil
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def _assert_write_and_read_scenario(self, test_data, description):
        """Helper method to test write-then-read round trip."""
        # Act
        write_success = write_json_file(test_data, self.test_file_path)
        read_data = read_json_file(self.test_file_path)
        
        # Assert
        self.assertTrue(write_success, f"Failed to write {description} to JSON file.")
        self.assertIsNotNone(read_data, f"Failed to read {description} from JSON file.")
        self.assertEqual(read_data, test_data, f"Read data does not match written {description}.")

    def test_write_and_read_various_data_types(self):
        """Test writing and reading various data types to/from a JSON file."""
        scenarios = {
            "dict": self.sample_dict,
            "list": self.sample_list,
            "empty_list": []
        }
        for data_type, data in scenarios.items():
            with self.subTest(data_type=data_type):
                self._assert_write_and_read_scenario(data, data_type)

    def test_read_invalid_json(self):
        """Test reading from a file with invalid JSON content."""
        # Arrange
        invalid_json_content = "{name: 'Missing quotes around key'}"
        with open(self.test_file_path, 'w') as file:
            file.write(invalid_json_content)
        
        # Act
        result = read_json_file(self.test_file_path)
        
        # Assert
        self.assertIsNone(result, "Expected None when reading invalid JSON content.")

    def test_read_nonexistent_file(self):
        """Test reading from a non-existent file."""
        # Arrange
        nonexistent_path = Path(self.test_dir) / "nonexistent.json"
        
        # Act
        result = read_json_file(nonexistent_path)
        
        # Assert
        self.assertIsNone(result, "Expected None when reading a non-existent file.")

if __name__ == "__main__":
    unittest.main()