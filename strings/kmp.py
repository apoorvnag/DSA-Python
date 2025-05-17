"""
Problem Statement: Implement the Knuth-Morris-Pratt (KMP) String Matching Algorithm

The KMP algorithm is an efficient string matching algorithm that uses the information
about the pattern itself to minimize the number of comparisons needed when searching
for a pattern in a text. It avoids unnecessary character comparisons by utilizing a
preprocessed array called the Longest Proper Prefix which is also Suffix (LPS) array.

The key insight of KMP is that when a mismatch occurs, we already know some of the
characters in the text (since they matched the pattern characters up to the mismatch).
This information can be used to determine where the next match could potentially begin,
avoiding the need to recheck characters we already know.

Operations to implement:
1. Compute the LPS array for a given pattern
2. Use the KMP algorithm to find all occurrences of a pattern in a text

Applications:
- Efficient string searching
- Text editors (find/replace functionality)
- Bioinformatics (DNA sequence matching)
- Network intrusion detection systems
"""

def compute_lps_array(pattern, m, lps):
    """
    Compute the Longest Proper Prefix which is also Suffix (LPS) array

    Args:
        pattern (str): The pattern string
        m (int): Length of the pattern
        lps (list): Array to store the LPS values
    """
    i = 0  # Length of the previous longest prefix & suffix

    for q in range(1, m):
        # If characters match, extend the current prefix & suffix
        if pattern[i] == pattern[q]:
            i = i + 1

        # If characters don't match, find the next longest prefix & suffix
        while i > 0 and pattern[i] != pattern[q]:
            i = lps[i - 1]

        # Set the LPS value for the current position
        lps[q] = i


def kmp_search(pattern, message):
    """
    Search for all occurrences of a pattern in a text using the KMP algorithm

    Args:
        pattern (str): The pattern to search for
        message (str): The text to search in

    Returns:
        list: Indices where the pattern occurs in the text
    """
    m = len(pattern)
    n = len(message)

    # Store the results
    results = []

    # Create LPS array
    lps = [0] * m

    # Index for pattern
    j = 0  # It keeps the currently matched length

    # Preprocess the pattern
    compute_lps_array(pattern, m, lps)

    # Index for text
    i = 0

    while i < n:
        # If current characters match, move both pointers
        if pattern[j] == message[i]:
            i += 1
            j += 1

        # If we've found a complete match
        if j == m:
            results.append(i - j)
            print('Found the pattern at index {}'.format(i - j))
            # Look for the next match, starting after a prefix of the current match
            j = lps[j - 1]
        # If characters don't match
        elif i < n and pattern[j] != message[i]:
            # If we have matched some characters, use the LPS array to skip comparisons
            if j != 0:
                j = lps[j - 1]
            # If we haven't matched any characters, move to the next character in the text
            else:
                i += 1

    return results


if __name__ == '__main__':
    txt = 'ABABDABACDABABCABAB'
    pat = 'ABABCABAB'

    # Find all occurrences of the pattern in the text
    occurrences = kmp_search(pat, txt)

    # Print the results
    if occurrences:
        print(f"Pattern '{pat}' found at positions: {occurrences}")
    else:
        print(f"Pattern '{pat}' not found in the text")
