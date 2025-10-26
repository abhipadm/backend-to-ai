"""
Contains Duplicate - Practice Template
Check if any value appears at least twice in an array.

Problem: Given an integer array nums, return true if any value appears 
at least twice in the array, and return false if every element is distinct.

Examples:
- [1,2,3,1] → True (1 appears twice)
- [1,2,3,4] → False (all distinct)  
- [1,1,1,3,3,4,3,2,4,2] → True (multiple duplicates)
"""

def contains_duplicate(nums):
    """
    Check if array contains any duplicates.
    
    Think about it: What's the fastest way to detect duplicates?
    - Compare array length with unique elements?
    - Track what you've seen while iterating?
    - Sort first and check adjacent elements?
    """
    # return contains_duplicate_set_length(nums)
    return  contains_duplicate_seen_tracking(nums)

# Let's explore different approaches for learning!

def contains_duplicate_set_length(nums):
    """
    Approach 1: Set Length Comparison
    If array has duplicates, converting to set will be shorter!
    
    Example: [1,2,3,1] → set([1,2,3,1]) = {1,2,3}
    Length: 4 vs 3 → Duplicate found!
    """
    # YOUR CODE HERE
    return len(nums) != len(set(nums))

def contains_duplicate_seen_tracking(nums):
    """
    Approach 2: Track What You've Seen (like Two Sum!)
    Use a set to remember elements you've already encountered.
    
    This is like your dictionary approach but simpler!
    """
    
    seen = set()
    for num in nums:
        # If current number already in set → duplicate!
        if num in seen:
            return True
        # Otherwise, add it to set
        seen.add(num)
    return False

def contains_duplicate_sorting(nums):
    """
    Approach 3: Sort and Check Adjacent
    If there are duplicates, they'll be next to each other after sorting.
    
    Example: [1,3,1,2] → sorted → [1,1,2,3]
    Check adjacent: nums[i] == nums[i+1]?
    """
    # YOUR CODE HERE
    # Hint: Sort the array first
    # Then check if any adjacent elements are equal
    pass

# Test your solutions
if __name__ == "__main__":
    print("🔍 Contains Duplicate Practice\n")
    
    # Test cases
    test_cases = [
        ([1,2,3,1], True),              # Basic duplicate
        ([1,2,3,4], False),             # All distinct
        ([1,1,1,3,3,4,3,2,4,2], True),  # Multiple duplicates
        ([], False),                    # Empty array
        ([1], False),                   # Single element
        ([1,2,3,4,5,6,7,8,9,0], False), # Large distinct array
    ]
    
    for nums, expected in test_cases:
        print(f"nums = {nums}")
        print(f"Expected: {expected}")
        
        # Test your main function
        result = contains_duplicate(nums)
        print(f"Your result: {result}")
        print(f"✅ Correct!" if result == expected else "❌ Try again!")
        print("-" * 50)

"""
💡 Think About These Approaches:

1. Set Length Comparison:
   - Pro: One line of code!
   - Con: Creates entire set even if duplicate found early
   
2. Seen Tracking:
   - Pro: Can exit early when duplicate found
   - Con: Requires loop and condition checking
   
3. Sorting:
   - Pro: Clear logic, works in-place
   - Con: Changes original array, O(n log n) time

Which approach appeals to you most?

🔗 Connection to Your Skills:
- Like your Two Sum dictionary for fast lookups
- Like your Anagram character counting
- Similar pattern: "Have I seen this before?"

Performance Comparison:
- Set length: O(n) time, O(n) space
- Seen tracking: O(n) time, O(n) space (but faster in practice)
- Sorting: O(n log n) time, O(1) space (if in-place)
"""