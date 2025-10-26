"""
Group Anagrams - Practice Template
Group strings that are anagrams of each other together.

Problem: Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

Examples:
Input: ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Input: [""]
Output: [[""]]

Input: ["a"]  
Output: [["a"]]
"""

def group_anagrams(strs):
    """
    Group strings that are anagrams of each other.
    
    Think about it: How do you identify anagrams?
    - Same characters, same counts → anagrams
    - Different characters → different groups
    
    Key insight: Anagrams share the same "signature"
    What could be a good signature?
    
    YOUR CODE HERE
    """
    
    # Hint 1: You need a way to identify anagrams (signature/key)
    # Hint 2: Use a dictionary to group by signature  
    # Hint 3: What makes anagrams the same? (sorted letters? character counts?)
    # Hint 4: Dictionary structure: {signature: [list_of_anagrams]}
    
    pass

# Let's explore different approaches for learning!

def group_anagrams_sorting(strs):
    """
    Approach 1: Sorting as Signature
    Anagrams have the same letters → same sorted signature!
    
    Example: "eat" → sorted → "aet"
             "tea" → sorted → "aet"  ← Same signature!
             "bat" → sorted → "abt"  ← Different signature
    """
    # YOUR CODE HERE
    # Hint: Create dict where key = sorted(string), value = list of anagrams
    pass

def group_anagrams_counting(strs):
    """
    Approach 2: Character Count as Signature
    Use character frequency as the signature (like your Valid Anagram!)
    
    Example: "eat" → {'a':1, 'e':1, 't':1}
             "tea" → {'a':1, 'e':1, 't':1}  ← Same count!
    
    But dictionaries can't be keys... what to do?
    """
    # YOUR CODE HERE
    # Hint: Convert character count to something hashable (tuple?)
    pass

def group_anagrams_builtin(strs):
    """
    Approach 3: Using Counter from collections
    Python's Counter makes character counting easy!
    """
    from collections import Counter
    
    # YOUR CODE HERE
    # Hint: Counter can be converted to something hashable
    pass

# Helper function you might find useful
def get_char_count_signature(s):
    """
    Convert string to character count signature.
    
    Example: "eat" → (('a',1), ('e',1), ('t',1))
    This tuple can be used as a dictionary key!
    """
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Convert to sorted tuple of (char, count) pairs
    return tuple(sorted(char_count.items()))

# Test your solutions
if __name__ == "__main__":
    print("🔤 Group Anagrams Practice\n")
    
    # Test cases
    test_cases = [
        (["eat","tea","tan","ate","nat","bat"], 
         [["bat"],["nat","tan"],["ate","eat","tea"]]),
        
        ([""], [[""]]),
        
        (["a"], [["a"]]),
        
        (["abc","bca","cab","xyz","zyx","yxz"], 
         [["abc","bca","cab"],["xyz","zyx","yxz"]]),
        
        (["listen","silent","hello","world"], 
         [["listen","silent"],["hello"],["world"]]),
    ]
    
    for i, (strs, expected) in enumerate(test_cases, 1):
        print(f"Test Case {i}:")
        print(f"Input: {strs}")
        
        result = group_anagrams(strs)
        print(f"Your result: {result}")
        
        # Note: Order of groups and order within groups can vary
        # So we'll just check if the grouping is correct conceptually
        print(f"Number of groups: {len(result)}")
        print("-" * 60)

"""
💡 Key Insights for Group Anagrams:

1. Signature Strategy:
   - Need a way to identify anagrams
   - Same signature = same group
   - Different signature = different group

2. Possible Signatures:
   - Sorted string: "eat" → "aet"
   - Character count: "eat" → {'a':1,'e':1,'t':1}
   - Tuple of counts: "eat" → (('a',1),('e',1),('t',1))

3. Algorithm Pattern:
   groups = {}
   for string in strings:
       signature = get_signature(string)
       if signature not in groups:
           groups[signature] = []
       groups[signature].append(string)
   return list(groups.values())

4. Connection to Your Skills:
   - Like your CSV analyzer grouping data by categories
   - Like your anagram detection but for multiple strings
   - Dictionary grouping pattern (key → list of values)

Which approach feels most natural to you?
"""