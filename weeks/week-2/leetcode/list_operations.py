"""
Python List Operations - Essential for LeetCode & Data Analysis
Practice these operations - they're used everywhere in programming!
"""

def basic_list_operations():
    """Basic list operations you'll use constantly"""
    
    # Creating lists
    nums = [1, 2, 3, 4, 5]
    empty_list = []
    
    # Accessing elements
    first = nums[0]        # First element: 1
    last = nums[-1]        # Last element: 5  
    middle = nums[2]       # Third element: 3
    
    # Slicing (super powerful!)
    first_three = nums[:3]     # [1, 2, 3]
    last_two = nums[-2:]       # [4, 5]
    middle_slice = nums[1:4]   # [2, 3, 4]
    
    print("Basic Operations:")
    print(f"Original: {nums}")
    print(f"First three: {first_three}")
    print(f"Last two: {last_two}")
    print()

def list_methods():
    """Important list methods for problem solving"""
    
    nums = [3, 1, 4, 1, 5, 9, 2, 6]
    
    # Adding elements
    nums.append(8)           # Add to end: [3, 1, 4, 1, 5, 9, 2, 6, 8]
    nums.insert(2, 99)       # Insert at index 2: [3, 1, 99, 4, 1, 5, 9, 2, 6, 8]
    
    # Removing elements  
    nums.remove(99)          # Remove first occurrence of 99
    popped = nums.pop()      # Remove and return last element
    
    # Finding elements
    index_of_4 = nums.index(4)  # Find index of first occurrence
    count_of_1 = nums.count(1)  # Count occurrences
    
    # Sorting (very common in LeetCode!)
    sorted_nums = sorted(nums)    # Returns new sorted list
    nums.sort()                   # Sorts in-place
    nums.reverse()               # Reverse in-place
    
    print("List Methods:")
    print(f"After operations: {nums}")
    print(f"Index of 4: {index_of_4}")
    print(f"Count of 1: {count_of_1}")
    print()

def enumerate_and_zip():
    """enumerate() and zip() - super useful for LeetCode!"""
    
    names = ["Alice", "Bob", "Charlie"]
    scores = [85, 92, 78]
    
    # enumerate - get both index and value (perfect for Two Sum!)
    print("Using enumerate():")
    for i, name in enumerate(names):
        print(f"  Index {i}: {name}")
    
    # zip - combine two lists
    print("\nUsing zip():")
    for name, score in zip(names, scores):
        print(f"  {name}: {score}")
    
    # Create dict from two lists (super common pattern!)
    name_score_dict = dict(zip(names, scores))
    print(f"\nDict from zip: {name_score_dict}")
    print()

def list_comprehensions():
    """List comprehensions - you're already using these! 🔥"""
    
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Basic comprehension
    squares = [x**2 for x in nums]
    
    # With condition (like your CSV data cleaning!)
    evens = [x for x in nums if x % 2 == 0]
    
    # Transform and filter together
    even_squares = [x**2 for x in nums if x % 2 == 0]
    
    # Nested comprehension (2D lists)
    matrix = [[i*j for j in range(3)] for i in range(3)]
    
    print("List Comprehensions:")
    print(f"Original: {nums}")
    print(f"Squares: {squares}")
    print(f"Evens: {evens}")
    print(f"Even squares: {even_squares}")
    print(f"Matrix: {matrix}")
    print()

def two_sum_helpful_operations():
    """Operations specifically useful for Two Sum problem"""
    
    nums = [2, 7, 11, 15]
    target = 9
    
    # Method 1: Using enumerate (index + value)
    print("Two Sum relevant operations:")
    print("Using enumerate for index tracking:")
    for i, num in enumerate(nums):
        print(f"  Index {i}: value {num}, need {target - num}")
    
    # Method 2: Using range and len for nested loops
    print("\nUsing range for nested loops:")
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                print(f"  Found! indices [{i}, {j}]: {nums[i]} + {nums[j]} = {target}")
    
    # Method 3: Dictionary for fast lookups
    seen = {}
    print("\nUsing dict for fast lookups:")
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            print(f"  Found! complement {complement} at index {seen[complement]}")
            print(f"  Current {num} at index {i}")
        seen[num] = i
    print()

def common_patterns():
    """Common list patterns you'll see in LeetCode"""
    
    nums = [1, 2, 2, 3, 4, 4, 5]
    
    # Check for duplicates
    has_duplicates = len(nums) != len(set(nums))
    
    # Find unique elements
    unique_nums = list(set(nums))
    
    # Two pointers technique setup
    left, right = 0, len(nums) - 1
    
    # Sliding window setup
    window_size = 3
    for i in range(len(nums) - window_size + 1):
        window = nums[i:i + window_size]
        print(f"Window {i}: {window}")
    
    print(f"\nCommon Patterns:")
    print(f"Has duplicates: {has_duplicates}")
    print(f"Unique elements: {unique_nums}")
    print(f"Two pointers: left={left}, right={right}")
    print()

if __name__ == "__main__":
    print("🐍 Python List Operations for LeetCode & Data Analysis")
    print("=" * 60)
    
    basic_list_operations()
    list_methods() 
    enumerate_and_zip()
    list_comprehensions()
    two_sum_helpful_operations()
    common_patterns()
    
    print("💡 Key Takeaways:")
    print("✅ enumerate() gives you both index and value")
    print("✅ List comprehensions are powerful and Pythonic")
    print("✅ Slicing creates new lists: nums[start:end]") 
    print("✅ Dictionaries are great for fast lookups")
    print("✅ Two pointers: left=0, right=len(nums)-1")
    print("\n🎯 Now you're ready to tackle Two Sum! Try it yourself!")