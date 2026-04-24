class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert_and_count(self, word):
        node = self.root
        count_new_nodes = 0
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
                count_new_nodes += 1
            node = node.children[ch]
        return count_new_nodes

def countDistinctSubstrings(s):
    trie = Trie()
    result = 0

    # Insert all suffixes
    for i in range(len(s)):
        suffix = s[i:]
        result += trie.insert_and_count(suffix)

    # +1 for empty substring
    return result + 1