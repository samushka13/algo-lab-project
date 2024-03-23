from collections import defaultdict
import random

class TrieNode:
    """
    A trie node.
    """
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_end = False

class Trie:
    """
    Class for handling trie insert and search operations.
    """
    def __init__(self):
        self.root = TrieNode()

    def insert(self, notes: list) -> None:
        """
        Inserts notes into the trie.
        """
        current = self.root
        for note in notes:
            current = current.children[note]
        current.is_end = True

    def search(self, notes: list) -> bool:
        """
        Looks up a note from the trie.

        Returns:
            If the current node has children.
        """
        current = self.root
        for note in notes:
            current = current.children.get(note)
            if current is None:
                return False
        return current.is_end

    def __str__(self):
        """
        Prints the trie as an indentation-based visualization.

        Returns:
            The current node's position in the trie.
        """
        def print_line(node: TrieNode, indent: str):
            return "".join(indent + str(key) + print_line(child, indent + "  ")
                for key, child in node.children.items())

        return print_line(self.root, "\n")

if __name__ == "__main__":
    random.seed(13)
    melodies = [[random.randint(50, 54) for x in range(5)] for y in range(20)]
    trie = Trie()
    for melody in melodies:
        trie.insert(melody)
    print(trie)
