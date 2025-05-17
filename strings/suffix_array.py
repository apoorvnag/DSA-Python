"""
Problem Statement: Implement a Suffix Array Data Structure

A suffix array is a sorted array of all suffixes of a given string. It is a 
space-efficient data structure that allows for fast substring searches.

For a string of length n, there are n suffixes, and the suffix array contains
the starting positions of these suffixes in lexicographically sorted order.

For example, for the string "banana":
- Suffixes: "banana", "anana", "nana", "ana", "na", "a"
- Suffix array: [5, 3, 1, 0, 4, 2] (positions in the original string)

Operations to implement:
1. Build a suffix array for a given string
2. Search for a pattern in the string using the suffix array (binary search)

Applications:
- Pattern matching
- Finding the longest common substring
- Data compression algorithms
- Bioinformatics (DNA sequence analysis)
"""

def build_suffix_array_naive(text):
    """
    Build a suffix array for the given text using a naive approach (O(n²log(n)) time complexity)
    
    Args:
        text (str): The input string
        
    Returns:
        list: The suffix array
    """
    n = len(text)
    
    # Create a list of (suffix, index) pairs
    suffixes = [(text[i:], i) for i in range(n)]
    
    # Sort the suffixes lexicographically
    suffixes.sort()
    
    # Extract the indices to form the suffix array
    suffix_array = [index for _, index in suffixes]
    
    return suffix_array


def build_suffix_array(text):
    """
    Build a suffix array for the given text using a more efficient approach
    This is a simplified implementation of the algorithm
    
    Args:
        text (str): The input string
        
    Returns:
        list: The suffix array
    """
    # For simplicity, we'll use the naive approach
    # In practice, more efficient algorithms like SA-IS or DC3 would be used
    return build_suffix_array_naive(text)


def search_pattern(text, pattern, suffix_array):
    """
    Search for a pattern in the text using the suffix array (binary search)
    
    Args:
        text (str): The input string
        pattern (str): The pattern to search for
        suffix_array (list): The suffix array of the text
        
    Returns:
        list: Indices where the pattern occurs in the text
    """
    n = len(text)
    m = len(pattern)
    result = []
    
    # Binary search for the lower bound
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        suffix_start = suffix_array[mid]
        
        # Compare the pattern with the suffix
        suffix = text[suffix_start:suffix_start + m]
        
        if pattern > suffix:
            left = mid + 1
        else:
            right = mid - 1
    
    # Lower bound
    lower_bound = left
    
    # Binary search for the upper bound
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        suffix_start = suffix_array[mid]
        
        # Compare the pattern with the suffix
        suffix = text[suffix_start:suffix_start + min(m, n - suffix_start)]
        
        if pattern < suffix:
            right = mid - 1
        else:
            left = mid + 1
    
    # Upper bound
    upper_bound = right
    
    # Collect all occurrences
    for i in range(lower_bound, upper_bound + 1):
        suffix_start = suffix_array[i]
        if text[suffix_start:suffix_start + m] == pattern:
            result.append(suffix_start)
    
    return result


def longest_common_prefix(text, i, j, suffix_array):
    """
    Find the length of the longest common prefix between two suffixes
    
    Args:
        text (str): The input string
        i (int): Index of the first suffix in the suffix array
        j (int): Index of the second suffix in the suffix array
        suffix_array (list): The suffix array of the text
        
    Returns:
        int: Length of the longest common prefix
    """
    n = len(text)
    a = suffix_array[i]
    b = suffix_array[j]
    
    lcp = 0
    while a + lcp < n and b + lcp < n and text[a + lcp] == text[b + lcp]:
        lcp += 1
    
    return lcp


def longest_common_substring(str1, str2):
    """
    Find the longest common substring between two strings using suffix arrays
    
    Args:
        str1 (str): First string
        str2 (str): Second string
        
    Returns:
        str: The longest common substring
    """
    # Concatenate the strings with a unique separator
    combined = str1 + "#" + str2
    n = len(combined)
    
    # Build the suffix array
    suffix_array = build_suffix_array(combined)
    
    # Find the longest common prefix between adjacent suffixes
    max_length = 0
    max_index = 0
    
    for i in range(1, n):
        # Check if the adjacent suffixes come from different strings
        curr_suffix = suffix_array[i]
        prev_suffix = suffix_array[i - 1]
        
        # One suffix is from str1 and the other is from str2
        if (curr_suffix < len(str1)) != (prev_suffix < len(str1)):
            lcp_length = longest_common_prefix(combined, i - 1, i, suffix_array)
            
            if lcp_length > max_length:
                max_length = lcp_length
                max_index = min(curr_suffix, prev_suffix)
    
    # Return the longest common substring
    if max_length == 0:
        return ""
    else:
        return combined[max_index:max_index + max_length]


# Example usage
if __name__ == "__main__":
    text = "banana"
    
    # Build the suffix array
    suffix_array = build_suffix_array(text)
    print(f"Text: {text}")
    print(f"Suffix Array: {suffix_array}")
    
    # Search for patterns
    patterns = ["ana", "nan", "an", "xyz"]
    for pattern in patterns:
        occurrences = search_pattern(text, pattern, suffix_array)
        if occurrences:
            print(f"Pattern '{pattern}' found at positions: {occurrences}")
        else:
            print(f"Pattern '{pattern}' not found")
    
    # Find the longest common substring
    str1 = "abcdefg"
    str2 = "bcdefxy"
    lcs = longest_common_substring(str1, str2)
    print(f"Longest common substring between '{str1}' and '{str2}': '{lcs}'")
