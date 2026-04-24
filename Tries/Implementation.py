class TrieNode:
    def __init__(self):
        # Each node holds up to 26 children (a-z), using a dict for flexibility
        self.children = {}
        # Flag to mark the end of a complete word
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        # Root node doesn't contain any character itself
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            # Create a new node if this character path doesn't exist
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        # Mark the final node as the end of a word
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        # Return True only if the complete word exists (i.e., is marked as ended here)
        return node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        # If traversal succeeds, the prefix exists
        return True






# class TrieNode :
#     def __init__(self):
#         self.children = {}
#         self.is_end = False
# class Trie:
#     def __init__(self):
#         self.root = TrieNode()

#     def insert(self, word: str) -> None:
#         node = self.root
#         for char in word :
#             if char not in node.children :
#                 node.children[char] = TrieNode()
#             node = node.children[char]
#         node.is_end = True

#     def search(self, word: str) -> bool:
#         node = self.root
#         for char in word :
#             if char not in node.children :
#                 return False
#             node = node.children[char]
#         return node.is_end
        
#     def startsWith(self, prefix: str) -> bool:
#         node = self.root
#         for char in prefix :
#             if char not in node.children:
#                 return False
#             node = node.children[char]
#         return True
# # Your Trie object will be instantiated and called as such:
# # obj = Trie()
# # obj.insert(word)
# # param_2 = obj.search(word)
# # param_3 = obj.startsWith(prefix)