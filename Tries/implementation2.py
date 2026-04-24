from os import *
from sys import *
from collections import *
from math import *
class TrieNode():
    def __init__(self):
        self.children = {}
        self.end_count = 0
        self.c_prefix = 0
class Trie:
    def __init__(self):
        # Write your code here.
        self.root = TrieNode()
    def insert(self, word):
        # Write your code here.
        node = self.root
        for char in word :
            if char not in node.children :
                node.children[char] = TrieNode()
            node = node.children[char]
            node.c_prefix += 1
        node.end_count += 1
    def countWordsEqualTo(self, word):
        node = self.root
        for char in word :
            if char not in node.children :
                return 0
            node = node.children[char]
        return node.end_count

    def countWordsStartingWith(self, word):
        node = self.root
        for char in word :
            if char not in node.children :
                return 0
            node = node.children[char]
        return node.c_prefix 

    def erase(self, word):
        # Write your code here.
        node = self.root
        for char in word :
            if char not in node.children :
                return
            node = node.children[char]
            node.c_prefix -= 1
        node.end_count -= 1
