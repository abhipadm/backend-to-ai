#!/usr/bin/env python3
"""
Test Runner for Week 2 - AI Engineer Roadmap
Runs all unit tests for the refactored file handlers and CSV analyzer
"""

import sys
import unittest
from pathlib import Path

# Add src to path for imports
current_dir = Path(__file__).parent
src_path = current_dir.parent / 'src'
sys.path.insert(0, str(src_path))

def run_all_tests():
    """Discover and run all tests in the tests directory."""
    
    print("="*60)
    print("🧪 RUNNING UNIT TESTS - Week 2 AI Engineer Roadmap")
    print("="*60)
    
    # Discover tests in current directory
    loader = unittest.TestLoader()
    test_dir = Path(__file__).parent
    suite = loader.discover(str(test_dir), pattern='test_*.py')
    
    # Run tests with detailed output
    runner = unittest.TextTestRunner(
        verbosity=2,
        descriptions=True,
        failfast=False
    )
    
    print("\n🚀 Starting test execution...\n")
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "="*60)
    print("📊 TEST SUMMARY")
    print("="*60)
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Skipped: {len(result.skipped) if hasattr(result, 'skipped') else 0}")
    
    if result.wasSuccessful():
        print("\n🎉 ALL TESTS PASSED! Your code is solid! ✅")
    else:
        print("\n❌ Some tests failed. Check the output above for details.")
        
    return result.wasSuccessful()

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
