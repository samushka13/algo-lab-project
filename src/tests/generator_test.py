import unittest
from mido import MidiFile
from midi import MidiHandler
from generator import Generator

mock_midi = MidiFile('song.mid')
mock_handler = MidiHandler(mock_midi)
mock_notes = mock_handler.get_notes()

class TestGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = Generator(50, mock_notes, 100, 1)

    def test_notes_are_equal_or_over_min_midi_pitch(self):
        notes = self.generator.generate_sequence()
        notes.sort()
        self.assertGreaterEqual(notes[0], 0, "All notes higher than minimum midi pitch")

    def test_notes_are_equal_or_under_max_midi_pitch(self):
        notes = self.generator.generate_sequence()
        notes.sort(reverse=True)
        self.assertLessEqual(notes[0], 127, "All notes less than maximum midi pitch")

    def test_correct_number_of_chains(self):
        chains = self.generator.get_chains()
        self.assertEqual(len(chains), len(mock_notes) - 1, "Number of chains is correct")
