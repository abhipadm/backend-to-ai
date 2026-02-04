"""
Unit tests for NumPy Vector Operations - Week 3
"""

import sys
import os
import unittest
import numpy as np

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from numpy_demos.vector_ops import VectorOperations


class TestVectorOperations(unittest.TestCase):
    """Test cases for VectorOperations class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.v1 = np.array([1, 2, 3])
        self.v2 = np.array([4, 5, 6])
        self.v3 = np.array([3, 4])  # For magnitude test (3-4-5 triangle)
    
    def test_create_vector(self):
        """Test vector creation from list"""
        v = VectorOperations.create_vector([1, 2, 3])
        self.assertIsInstance(v, np.ndarray)
        np.testing.assert_array_equal(v, np.array([1, 2, 3]))
    
    def test_vector_add(self):
        """Test vector addition"""
        result = VectorOperations.vector_add(self.v1, self.v2)
        expected = np.array([5, 7, 9])
        np.testing.assert_array_equal(result, expected)
    
    def test_vector_add_dimension_mismatch(self):
        """Test vector addition with mismatched dimensions"""
        v_wrong = np.array([1, 2])
        with self.assertRaises(ValueError):
            VectorOperations.vector_add(self.v1, v_wrong)
    
    def test_vector_subtract(self):
        """Test vector subtraction"""
        result = VectorOperations.vector_subtract(self.v2, self.v1)
        expected = np.array([3, 3, 3])
        np.testing.assert_array_equal(result, expected)
    
    def test_scalar_multiply(self):
        """Test scalar multiplication"""
        result = VectorOperations.scalar_multiply(self.v1, 3)
        expected = np.array([3, 6, 9])
        np.testing.assert_array_equal(result, expected)
        
        # Test with float
        result_float = VectorOperations.scalar_multiply(self.v1, 0.5)
        expected_float = np.array([0.5, 1.0, 1.5])
        np.testing.assert_array_almost_equal(result_float, expected_float)
    
    def test_dot_product(self):
        """Test dot product calculation"""
        result = VectorOperations.dot_product(self.v1, self.v2)
        expected = 32  # 1*4 + 2*5 + 3*6
        self.assertEqual(result, expected)
    
    def test_magnitude(self):
        """Test magnitude calculation"""
        result = VectorOperations.magnitude(self.v3)
        expected = 5.0  # sqrt(3^2 + 4^2) = sqrt(25) = 5
        self.assertAlmostEqual(result, expected)
        
        # Test with v1
        result_v1 = VectorOperations.magnitude(self.v1)
        expected_v1 = np.sqrt(14)  # sqrt(1^2 + 2^2 + 3^2)
        self.assertAlmostEqual(result_v1, expected_v1)
    
    def test_normalize(self):
        """Test vector normalization"""
        result = VectorOperations.normalize(self.v3)
        expected = np.array([0.6, 0.8])  # [3/5, 4/5]
        np.testing.assert_array_almost_equal(result, expected)
        
        # Verify magnitude is 1
        mag = VectorOperations.magnitude(result)
        self.assertAlmostEqual(mag, 1.0)
    
    def test_normalize_zero_vector(self):
        """Test normalization of zero vector raises error"""
        zero_vec = np.array([0, 0, 0])
        with self.assertRaises(ValueError):
            VectorOperations.normalize(zero_vec)
    
    def test_cosine_similarity(self):
        """Test cosine similarity calculation"""
        # Test with parallel vectors
        v_parallel = np.array([2, 4, 6])  # Same direction as v1
        result = VectorOperations.cosine_similarity(self.v1, v_parallel)
        self.assertAlmostEqual(result, 1.0)
        
        # Test with perpendicular vectors
        v_perp = np.array([1, -1, 0])
        v_base = np.array([1, 1, 0])
        result_perp = VectorOperations.cosine_similarity(v_base, v_perp)
        self.assertAlmostEqual(result_perp, 0.0, places=5)
        
        # Test with opposite vectors
        v_opposite = np.array([-1, -2, -3])
        result_opposite = VectorOperations.cosine_similarity(self.v1, v_opposite)
        self.assertAlmostEqual(result_opposite, -1.0)
    
    def test_cosine_similarity_zero_vector(self):
        """Test cosine similarity with zero vector raises error"""
        zero_vec = np.array([0, 0, 0])
        with self.assertRaises(ValueError):
            VectorOperations.cosine_similarity(self.v1, zero_vec)
    
    def test_element_wise_multiply(self):
        """Test element-wise multiplication"""
        result = VectorOperations.element_wise_multiply(self.v1, self.v2)
        expected = np.array([4, 10, 18])  # [1*4, 2*5, 3*6]
        np.testing.assert_array_equal(result, expected)
    
    def test_euclidean_distance(self):
        """Test Euclidean distance calculation"""
        v_origin = np.array([0, 0])
        result = VectorOperations.euclidean_distance(v_origin, self.v3)
        expected = 5.0  # Distance from origin to (3, 4)
        self.assertAlmostEqual(result, expected)
        
        # Test with same vectors
        result_same = VectorOperations.euclidean_distance(self.v1, self.v1)
        self.assertAlmostEqual(result_same, 0.0)
    
    def test_mean_vector(self):
        """Test mean vector calculation"""
        vectors = [
            np.array([1, 2, 3]),
            np.array([4, 5, 6]),
            np.array([7, 8, 9])
        ]
        result = VectorOperations.mean_vector(vectors)
        expected = np.array([4, 5, 6])
        np.testing.assert_array_equal(result, expected)
    
    def test_vector_statistics(self):
        """Test comprehensive statistics calculation"""
        v = np.array([1, 2, 3, 4, 5])
        stats = VectorOperations.vector_statistics(v)
        
        # Verify all keys exist
        expected_keys = ['mean', 'median', 'std', 'var', 'min', 'max', 'sum', 'magnitude']
        for key in expected_keys:
            self.assertIn(key, stats)
        
        # Verify values
        self.assertEqual(stats['mean'], 3.0)
        self.assertEqual(stats['median'], 3.0)
        self.assertEqual(stats['min'], 1)
        self.assertEqual(stats['max'], 5)
        self.assertEqual(stats['sum'], 15)
    
    def test_empty_vector(self):
        """Test operations with empty vectors"""
        empty = np.array([])
        self.assertEqual(len(empty), 0)
        
        # Mean of empty should be nan
        self.assertTrue(np.isnan(np.mean(empty)))


class TestVectorOperationsEdgeCases(unittest.TestCase):
    """Test edge cases and special scenarios"""
    
    def test_single_element_vector(self):
        """Test operations on single-element vectors"""
        v1 = np.array([5])
        v2 = np.array([3])
        
        result_add = VectorOperations.vector_add(v1, v2)
        self.assertEqual(result_add[0], 8)
        
        result_dot = VectorOperations.dot_product(v1, v2)
        self.assertEqual(result_dot, 15)
    
    def test_large_vectors(self):
        """Test with high-dimensional vectors"""
        v1 = np.random.rand(1000)
        v2 = np.random.rand(1000)
        
        result = VectorOperations.vector_add(v1, v2)
        self.assertEqual(len(result), 1000)
        
        # Verify cosine similarity is in valid range
        cos_sim = VectorOperations.cosine_similarity(v1, v2)
        self.assertTrue(-1 <= cos_sim <= 1)
    
    def test_negative_values(self):
        """Test with negative vector values"""
        v1 = np.array([-1, -2, -3])
        v2 = np.array([1, 2, 3])
        
        result_add = VectorOperations.vector_add(v1, v2)
        expected = np.array([0, 0, 0])
        np.testing.assert_array_equal(result_add, expected)
    
    def test_floating_point_vectors(self):
        """Test with floating-point values"""
        v1 = np.array([1.5, 2.7, 3.9])
        v2 = np.array([0.5, 1.3, 2.1])
        
        result = VectorOperations.vector_add(v1, v2)
        expected = np.array([2.0, 4.0, 6.0])
        np.testing.assert_array_almost_equal(result, expected)


def run_tests():
    """Run all tests with detailed output"""
    print("=" * 60)
    print("Running NumPy Vector Operations Tests - Week 3")
    print("=" * 60 + "\n")
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add test classes
    suite.addTests(loader.loadTestsFromTestCase(TestVectorOperations))
    suite.addTests(loader.loadTestsFromTestCase(TestVectorOperationsEdgeCases))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "=" * 60)
    print(f"Tests run: {result.testsRun}")
    print(f"✅ Passed: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"❌ Failed: {len(result.failures)}")
    print(f"⚠️  Errors: {len(result.errors)}")
    print("=" * 60)
    
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
