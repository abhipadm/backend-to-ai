"""
Two Sum - Practice Template
Fill in the blanks and implement your solution!
"""

def two_sum(nums, target):
    """
    Given a list of integers and a target, return indices of two numbers that add up to target.
    
    Example: nums = [2, 7, 11, 15], target = 9
    Return: [0, 1] because nums[0] + nums[1] = 2 + 7 = 9
    """
    
    # YOUR CODE HERE
    seen = {}
    for (i, num) in enumerate(nums):
        n = target - num

        if n in seen:
            print(f"Found {num} + {n}")
            return [i, seen[n]]
        seen[num] = i

# Test your solution
if __name__ == "__main__":
    # Test cases - run these to check your solution
    test_cases = [
        ([2, 7, 11, 15], 9),      # Should return [0, 1]
        ([3, 2, 4], 6),           # Should return [1, 2] 
        ([3, 3], 6),              # Should return [0, 1]
    ]
    
    for nums, target in test_cases:
        result = two_sum(nums, target)
        print(f"nums = {nums}, target = {target}")
        print(f"Your result: {result}")
        
        # Verify the result works
        if result and len(result) == 2:
            i, j = result[0], result[1]
            if i < len(nums) and j < len(nums):
                sum_check = nums[i] + nums[j] 
                print(f"Check: nums[{i}] + nums[{j}] = {nums[i]} + {nums[j]} = {sum_check}")
                print(f"✅ Correct!" if sum_check == target else "❌ Wrong sum")
        print("-" * 40)

"""
💡 Approach Ideas:

Method 1 - Brute Force:
- Use two nested loops
- Check every possible pair
- Return indices when sum equals target

Method 2 - Hash Map (Dictionary):  
- Use one loop with enumerate()
- For each number, calculate what you need (target - current)
- Check if you've seen that number before
- Store numbers you've seen in a dictionary

Which approach do you want to try first?
"""