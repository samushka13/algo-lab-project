import unittest
from mido import MidiFile
from midi import MidiHandler
from generator import Generator

mock_midi = MidiFile('song.mid')
mock_handler = MidiHandler(mock_midi)
mock_notes = mock_handler.get_notes()

class TestGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = Generator()

    def test_notes_are_equal_or_over_min_midi_pitch(self):
        notes = self.generator.generate_sequence(50, mock_notes, 100, 1)
        notes.sort()
        self.assertGreaterEqual(notes[0], 0, "All notes higher than minimum midi pitch")

    def test_notes_are_equal_or_under_max_midi_pitch(self):
        notes = self.generator.generate_sequence(50, mock_notes, 100, 1)
        notes.sort(reverse=True)
        self.assertLessEqual(notes[0], 127, "All notes less than maximum midi pitch")

    def test_correct_number_of_chains(self):
        order = 1
        chains = self.generator.get_chains(mock_notes, order)
        self.assertEqual(len(chains), len(mock_notes) - order, "Number of chains is correct")
