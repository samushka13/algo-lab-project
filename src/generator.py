from collections import Counter
import random

class Generator:
    """
    Generates a melody based on given notes.

    Attributes:
        start: The midi note used as the starting point.
        notes: The midi notes used as a source material.
        length: The length of the sequence to be generated.
        order: The selected Markov chain order.
    """
    def __init__(self, start: int, notes: list, length: int, order: int):
        self.start = start
        self.notes = notes
        self.length = length
        self.order = order

    def get_chains(self):
        """
        Forms a list of melody chains from notes based on the selected Markov chain order.

        Returns:
            The list of melody chains.
        """
        arrays = []
        for n in range(self.order + 1):
            arrays.append(self.notes[n:])

        chains = []
        for x in zip(*arrays):
            chains.append(x)

        return chains

    def get_prediction(self, note: int):
        """
        Predicts the next note.

        Args:
            note: The current midi note.

        Returns:
            The prediction for the next note.
        """
        chains = self.get_chains()
        chains = [chain for chain in chains if chain[0] == note]
        counts = Counter(chains)
        keys = counts.keys()

        for key in keys:
            counts[key] = counts[key] / len(chains)

        options = [key[-1] for key in keys]
        probabilities = list(counts.values())
        prediction = random.choices(options, probabilities)[0]

        return prediction

    def generate_sequence(self):
        """
        Generates a sequence of notes.

        Returns:
            The generated sequence.
        """
        sequence = []

        for _ in range(self.length):
            sequence.append(self.get_prediction(self.start))
            self.start = sequence[-1]

        return sequence
