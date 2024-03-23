from mido import MidiFile
from midi import MidiHandler
from generator import Generator

if __name__ == "__main__":
    mid = MidiFile('song.mid')
    handler = MidiHandler(mid)
    notes = handler.get_notes()
    generator = Generator(50, notes, 100, 1)
    print(generator.generate_sequence())
