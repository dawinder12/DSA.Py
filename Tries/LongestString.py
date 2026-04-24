#longest String that contain all the prefix

from sys import *
from collections import *
from math import *

from typing import *

class TrieNode :
    def __init__(self):
        self.children = {}
        self.is_end = False
class Trie :
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self,word):
        node = self.root 
        for char in word :
            if char not in node.children :
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True 
    
    def check_all_prefix(self,word):
        node = self.root
        for char in word :
            if char not in node.children :
                return False 
            node = node.children[char]
            if node.is_end == False : # uske sare present h so all true
                return False        
        return True

def completeString(n: int, a: List[str])-> str:
    
    # Write your Code here
    trie = Trie()
    for char in a :
        trie.insert(char)
    
    ans = ""
    for ch in a :
        if trie.check_all_prefix(ch) :
            if len(ch) >len(ans) or (len(ch) == len(ans) and ch < ans ):
                ans = ch 
    return ans if ans != "" else None

    



















    