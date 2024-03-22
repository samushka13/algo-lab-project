from collections import Counter
import random

class Generator:
    def get_chains(self, arr: list, order: int):
        arrays = []
        for n in range(order + 1):
            arrays.append(arr[n:])

        chains = []
        for x in zip(*arrays):
            chains.append(x)

        return chains

    def get_prediction(self, pitch: int, data: list, order: int):
        chains = self.get_chains(data, order)
        chains = [chain for chain in chains if chain[0] == pitch]
        counts = Counter(chains)
        keys = counts.keys()

        for key in keys:
            counts[key] = counts[key] / len(chains)

        options = [key[-1] for key in keys]
        probabilities = list(counts.values())
        prediction = random.choices(options, probabilities)[0]

        return prediction

    def generate_sequence(self, pitch: int, data: list, length: int, order: int):
        pitches = []

        for _ in range(length):
            pitches.append(self.get_prediction(pitch, data, order))
            pitch = pitches[-1]

        return pitches
