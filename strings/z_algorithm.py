"""
Problem Statement: Implement the Z-Algorithm for Pattern Matching

The Z-Algorithm is a linear time string matching algorithm that finds all occurrences
of a pattern in a text in O(n+m) time, where n is the length of the text and m is the
length of the pattern.

The Z-Algorithm works by calculating a Z-array for a string, where Z[i] represents the
length of the longest substring starting at position i that is also a prefix of the string.

For pattern matching, we concatenate the pattern, a special character (that doesn't appear
in the text or pattern), and the text, then compute the Z-array for this concatenated string.
The positions where Z[i] equals the pattern length indicate matches.

Operations to implement:
1. Compute the Z-array for a given string
2. Use the Z-algorithm for pattern matching

Applications:
- Efficient string matching
- Finding all occurrences of a pattern in a text
- String compression
- Palindrome detection
"""

def compute_z_array(string):
    """
    Compute the Z-array for a given string
    
    The Z-array Z[i] represents the length of the longest substring starting at
    position i that is also a prefix of the string.
    
    Args:
        string (str): The input string
        
    Returns:
        list: The Z-array
    """
    n = len(string)
    z = [0] * n
    
    # Z[0] is meaningless as it would always be equal to n
    # We start from index 1
    
    # [L, R] represents the rightmost Z-box (substring match)
    L, R = 0, 0
    
    for i in range(1, n):
        # If i is outside the current Z-box, we compute Z[i] naively
        if i > R:
            L = R = i
            
            # Naive computation: compare characters starting from the beginning
            while R < n and string[R - L] == string[R]:
                R += 1
            
            z[i] = R - L
            R -= 1  # Adjust R to point to the last matched character
        else:
            # i is inside the current Z-box
            k = i - L
            
            # If Z[k] is less than the remaining length of the Z-box,
            # then Z[i] = Z[k]
            if z[k] < R - i + 1:
                z[i] = z[k]
            else:
                # Otherwise, we need to extend the Z-box
                L = i
                
                # Start matching from R+1
                while R < n and string[R - L] == string[R]:
                    R += 1
                
                z[i] = R - L
                R -= 1  # Adjust R to point to the last matched character
    
    return z


def z_algorithm_pattern_matching(text, pattern):
    """
    Find all occurrences of a pattern in a text using the Z-Algorithm
    
    Args:
        text (str): The text to search in
        pattern (str): The pattern to search for
        
    Returns:
        list: Indices where the pattern occurs in the text
    """
    # Concatenate pattern, a special character, and text
    # The special character should not appear in either the pattern or text
    # For simplicity, we use '$' as the special character
    concatenated = pattern + "$" + text
    
    # Compute the Z-array for the concatenated string
    z = compute_z_array(concatenated)
    
    # Find all occurrences of the pattern in the text
    pattern_length = len(pattern)
    result = []
    
    # Check Z-values starting from the position after the special character
    for i in range(pattern_length + 1, len(concatenated)):
        if z[i] == pattern_length:
            # Found a match at position i - (pattern_length + 1) in the original text
            result.append(i - (pattern_length + 1))
    
    return result


def find_longest_palindromic_substring(string):
    """
    Find the longest palindromic substring in a given string using the Z-Algorithm
    
    Args:
        string (str): The input string
        
    Returns:
        str: The longest palindromic substring
    """
    # Create a new string by concatenating the original string,
    # a special character, and the reversed string
    reversed_string = string[::-1]
    concatenated = string + "$" + reversed_string
    
    # Compute the Z-array for the concatenated string
    z = compute_z_array(concatenated)
    
    # Find the maximum Z-value and its position
    max_z = 0
    max_z_index = 0
    
    for i in range(len(string) + 1, len(concatenated)):
        # Check if the current Z-value is greater than the maximum
        if z[i] > max_z:
            # Make sure the palindrome doesn't overlap with the reversed part
            # The palindrome should be contained entirely within the original string
            if i + z[i] <= 2 * len(string) + 1:
                max_z = z[i]
                max_z_index = i
    
    # Extract the longest palindromic substring
    if max_z == 0:
        return string[0]  # Return the first character if no palindrome is found
    
    # Calculate the starting position of the palindrome in the original string
    start = len(string) - (max_z_index - len(string) - 1) - max_z
    
    return string[start:start + max_z]


# Example usage
if __name__ == "__main__":
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    
    # Find all occurrences of the pattern in the text
    occurrences = z_algorithm_pattern_matching(text, pattern)
    
    if occurrences:
        print(f"Pattern '{pattern}' found at positions: {occurrences}")
    else:
        print(f"Pattern '{pattern}' not found in the text")
    
    # Test the Z-array computation
    test_string = "aabcaabxaaaz"
    z_array = compute_z_array(test_string)
    print(f"String: {test_string}")
    print(f"Z-array: {z_array}")
    
    # Test finding the longest palindromic substring
    test_strings = ["babad", "cbbd", "racecar", "banana"]
    for s in test_strings:
        longest_palindrome = find_longest_palindromic_substring(s)
        print(f"Longest palindromic substring in '{s}': '{longest_palindrome}'")
