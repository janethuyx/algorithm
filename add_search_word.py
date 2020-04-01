
class TrieTree:
    def __init__(self):
        self.children = {}
        self.is_word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieTree()

    """
    @param: word: Adds a word into the data structure.
    @return: nothing
    """

    def addWord(self, word):
        # write your code here
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieTree()
            node = node.children[letter]
        node.is_word = True

    """
    @param: word: A word could contain the dot character '.' to represent any one letter.
    @return: if the word is in the data structure.
    """

    def find(self, node, word, index):
        if node is None:
            return False
        if index >= len(word):
            return node.is_word

        char = word[index]
        if char != '.':
            return self.find(node.children.get(char), word, index + 1)

        for child in node.children:
            if self.find(node.children[child], word, index + 1):
                return True
        return False

    def search(self, word):
        # write your code here
        if word is None:
            return False
        return self.find(self.root, word, 0)


