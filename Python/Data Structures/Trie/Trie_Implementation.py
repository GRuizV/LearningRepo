class TrieNode:

    def __init__(self):

        self.values = {}
        self.is_word = False
        self.parent = None


class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    # # RECURSIVE VERSION
    # def rec_insert(self, word: str, curr_node=None) -> None:
        
    #     # If no node is passed
    #     if not curr_node:
    #         curr_node = self.root

    #     # Base Case
    #     if not word:
    #         curr_node.is_word = True              
    #         return
        
    #     # Recursive Case
    #     char = word[0]
    
    #     # If the character node doesn't exist, create a new one
    #     if char not in curr_node.values:
    #         curr_node.values[char] = TrieNode()       
        
    #     # Recur for the next character
    #     self.insert(word[1:], curr_node=curr_node.values[char])
   

    def insert(self, word: str) -> None:

        node = self.root

        for char in word:

            if char not in node.values:
                new_node = TrieNode()
                new_node.parent = node
                node.values[char] = new_node
           
            node = node.values[char]

        node.is_word = True


    def search(self, word: str) -> bool:
        
        node = self.root

        for char in word:          
                    
            if char not in node.values:
                return False
            
            node = node.values[char]
        
        return node.is_word


    def startsWith(self, prefix: str) -> bool:
        
        node = self.root

        for char in prefix:

            if char not in node.values:
                return False
            
            node = node.values[char]
        
        return True
    

    def delete(self, word: str) -> None:

        if not self.search(word):
            return  # Word not found, nothing to delete
        
        # Traverse up to the last character
        node = self.root
        for char in word:
            node = node.values[char]

        node.is_word = False  # Unmark the end of the word
        
        # Backtracking to delete unnecessary nodes
        for char in reversed(word):

            parent = node.parent

            if not node.values and not node.is_word:
                del parent.values[char]

            node = parent
        


# IMPLEMENTATION TESTIING

new_trie = Trie()

new_trie.insert('Car')
print('-Car- inserted')
new_trie.insert('Carrot')
print('-Carrot- inserted')

print(f'Search result for -Car-: {new_trie.search('Car')}')
print(f'Search result for -Carrot-: {new_trie.search('Carrot')}')

new_trie.delete('Car')
print('-Car- deleted')

print(f'Search result for -Car-: {new_trie.search('Car')}')
print(f'Search result for -Carrot-: {new_trie.search('Carrot')}')