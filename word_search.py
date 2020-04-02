class TrieTree:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieTree()

    def addWord(self, word):
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieTree()
            node = node.children[letter]
        node.is_word = True

    def find(self, word):
        node = self.root
        for letter in word:
            node = node.children.get(letter)
            if node is None:
                return None
        return node

    def search(self, word):
        node = self.find(word)
        return node is not None and node.is_word == True


class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """

    def wordSearchII(self, board, words):
        # write your code here
        if not words or not board:
            return []
        trie = Trie()
        for word in words:
            trie.addWord(word)
        result = set([])
        x_length, y_length = len(board), len(board[0])
        for x_index in range(x_length):
            for y_index in range(y_length):
                self.dfs(x_index, y_index, trie, board[x_index][y_index], \
                         result, board, set([(x_index, y_index)]))
        return list(result)

    def dfs(self, x, y, trie, word, result, matrix, path):
        if trie.search(word):
            result.add(word)
        if not trie.find(word):
            return
        for dx, dy in {(1, 0), (-1, 0), (0, 1), (0, -1)}:
            next_x = dx + x
            next_y = dy + y
            if self.is_valid(next_x, next_y, matrix, path):
                next_letter = matrix[next_x][next_y]
                path.add((next_x, next_y))
                self.dfs(next_x, next_y, trie, word + next_letter, result, matrix, path)
                path.remove((next_x, next_y))

    def is_valid(self, x, y, matrix, path):
        return 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and (x, y) not in path


