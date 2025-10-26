"""
Valid Anagram - Practice Template
An anagram uses exactly the same letters, just rearranged!

Problem: Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Examples:
- "anagram" and "nagaram" → True (same letters, different order)  
- "rat" and "car" → False (different letters)
- "listen" and "silent" → True (perfect anagram!)
"""

def is_anagram(s, t):
    """
    Check if two strings are anagrams of each other.
    
    Think about it: What makes two strings anagrams?
    - Same length?
    - Same letters?  
    - Same COUNT of each letter?
    
    YOUR CODE HERE
    """
    # return is_anagram_sorting(s, t)
    # return is_anagram_builtin(s, t)  
    return is_anagram_counter(s, t)
    # return is_anagram_set(s, t)

def is_anagram_set(s, t):
    if len(s) != len(t): return False
    # set uniques the letters using set function
    # then we count occurrences in both strings
    # less efficient approach as we count multiple times
    for l in set(s):
        if s.count(l) != t.count(l): return False
    return True

def is_anagram_sorting(s, t):
    """
    Approach 1: Sorting
    If both strings have same letters, sorting them should give same result!
    
    Example: "anagram" → sorted → "aaagmnr"
             "nagaram" → sorted → "aaagmnr"  ✅ Same!
    """
    # YOUR CODE HERE
    # 'sorted(string)' returns a sorted list of characters
    if sorted(s) == sorted(t):
        return True
    else:
        return False

def is_anagram_counter(s, t):
    """
    Approach 2: Character counting (like your CSV data analysis!)
    Count frequency of each character in both strings
    
    Example: "anagram" → {'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1}
             "nagaram" → {'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1} ✅ Same!
    """
    # YOUR CODE HERE
    # Use a dictionary to count characters
    if len(s) != len(t):
        return False
    char_count_s = {}
    char_count_t = {}
    for char in s:
        char_count_s[char] = char_count_s.get(char, 0) + 1
    for char in t:
        char_count_t[char] = char_count_t.get(char, 0) + 1
    return char_count_s == char_count_t

def is_anagram_builtin(s, t):
    """
    Approach 3: Using Python's Counter (from collections)
    Counter automatically counts elements for you!
    """
    from collections import Counter
    
    # YOUR CODE HERE
    # Counter(s) creates a count dictionary
    if Counter(s) == Counter(t):
        return True
    else:
        return False

# Test your solutions
if __name__ == "__main__":
    print("🔤 Valid Anagram Practice\n")
    
    # Test cases
    test_cases = [
        ("anagram", "nagaram", True),   # Classic anagram
        ("rat", "car", False),          # Different letters
        ("listen", "silent", True),     # Another classic
        ("hello", "bello", False),      # One letter different
        ("", "", True),                 # Empty strings
        ("a", "ab", False),            # Different lengths
    ]
    
    for s, t, expected in test_cases:
        print(f"s = '{s}', t = '{t}' → Expected: {expected}")
        
        # Test your main function
        result = is_anagram(s, t)
        print(f"Your result: {result}")
        print(f"✅ Correct!" if result == expected else "❌ Try again!")
        print("-" * 40)