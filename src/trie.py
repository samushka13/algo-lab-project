from collections import defaultdict
import random

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, pitches: list) -> None:
        current = self.root
        for pitch in pitches:
            current = current.children[pitch]
        current.is_end = True

    def search(self, pitches: list) -> bool:
        current = self.root
        for pitch in pitches:
            current = current.children.get(pitch)
            if current is None:
                return False
        return current.is_end

    def __str__(self):
        def print_line(node: TrieNode, indent: str):
            return "".join(indent + str(key) + print_line(child, indent + "  ")
                for key, child in node.children.items())

        return print_line(self.root, "\n")

if __name__ == "__main__":
    trie = Trie()
    random.seed(13)
    melodies = [[random.randint(50, 54) for x in range(5)] for y in range(20)]
    for melody in melodies:
        trie.insert(melody)
    print(trie)
