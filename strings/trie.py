"""
Problem Statement: Implement a Trie (Prefix Tree) Data Structure

A Trie is a tree-like data structure used to store a dynamic set of strings, 
where the keys are usually strings. Unlike a binary search tree, no node in the 
tree stores the key associated with that node; instead, its position in the tree 
defines the key with which it is associated. All the descendants of a node have a 
common prefix of the string associated with that node, and the root is associated 
with the empty string.

Operations to implement:
1. Insert a word into the trie
2. Search for a word in the trie
3. Check if a prefix exists in the trie
4. Delete a word from the trie (optional)

Applications:
- Autocomplete features
- Spell checkers
- IP routing (longest prefix matching)
- Predictive text
"""

class TrieNode:
    """A node in the trie structure"""
    
    def __init__(self):
        # Dictionary to store children nodes
        # Key: character, Value: TrieNode
        self.children = {}
        
        # Flag to mark the end of a word
        self.is_end_of_word = False


class Trie:
    """Trie data structure implementation"""
    
    def __init__(self):
        """Initialize the trie with an empty root node"""
        self.root = TrieNode()
    
    def insert(self, word):
        """
        Insert a word into the trie
        
        Args:
            word (str): The word to insert
        """
        node = self.root
        
        # Traverse the trie for each character in the word
        for char in word:
            # If the character is not found in the current node's children,
            # add a new node for this character
            if char not in node.children:
                node.children[char] = TrieNode()
            
            # Move to the child node
            node = node.children[char]
        
        # Mark the end of the word
        node.is_end_of_word = True
    
    def search(self, word):
        """
        Search for a word in the trie
        
        Args:
            word (str): The word to search for
            
        Returns:
            bool: True if the word exists in the trie, False otherwise
        """
        node = self.root
        
        # Traverse the trie for each character in the word
        for char in word:
            # If the character is not found in the current node's children,
            # the word does not exist in the trie
            if char not in node.children:
                return False
            
            # Move to the child node
            node = node.children[char]
        
        # Return True if we've reached the end of a word, False otherwise
        return node.is_end_of_word
    
    def starts_with(self, prefix):
        """
        Check if there is any word in the trie that starts with the given prefix
        
        Args:
            prefix (str): The prefix to check
            
        Returns:
            bool: True if there is any word with the given prefix, False otherwise
        """
        node = self.root
        
        # Traverse the trie for each character in the prefix
        for char in prefix:
            # If the character is not found in the current node's children,
            # no word with the given prefix exists in the trie
            if char not in node.children:
                return False
            
            # Move to the child node
            node = node.children[char]
        
        # If we've traversed all characters in the prefix, return True
        return True
    
    def get_words_with_prefix(self, prefix):
        """
        Get all words in the trie that start with the given prefix
        
        Args:
            prefix (str): The prefix to search for
            
        Returns:
            list: A list of words that start with the given prefix
        """
        result = []
        node = self.root
        
        # Traverse to the node corresponding to the prefix
        for char in prefix:
            if char not in node.children:
                return result
            node = node.children[char]
        
        # Use DFS to find all words starting from the prefix node
        self._dfs(node, prefix, result)
        return result
    
    def _dfs(self, node, prefix, result):
        """
        Helper method for DFS traversal to find all words with a given prefix
        
        Args:
            node (TrieNode): Current node in the traversal
            prefix (str): Current prefix formed by the path from root to node
            result (list): List to store the words found
        """
        if node.is_end_of_word:
            result.append(prefix)
        
        for char, child_node in node.children.items():
            self._dfs(child_node, prefix + char, result)


# Example usage
if __name__ == "__main__":
    trie = Trie()
    
    # Insert words
    words = ["apple", "app", "application", "banana", "ball", "bat"]
    for word in words:
        trie.insert(word)
    
    # Search for words
    print(f"Search 'apple': {trie.search('apple')}")  # True
    print(f"Search 'app': {trie.search('app')}")  # True
    print(f"Search 'orange': {trie.search('orange')}")  # False
    
    # Check prefixes
    print(f"Prefix 'app': {trie.starts_with('app')}")  # True
    print(f"Prefix 'ban': {trie.starts_with('ban')}")  # True
    print(f"Prefix 'ora': {trie.starts_with('ora')}")  # False
    
    # Get words with prefix
    print(f"Words with prefix 'app': {trie.get_words_with_prefix('app')}")  # ['apple', 'app', 'application']
    print(f"Words with prefix 'ba': {trie.get_words_with_prefix('ba')}")  # ['banana', 'ball', 'bat']
