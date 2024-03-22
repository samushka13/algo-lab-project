import unittest
from mido import MidiFile
from midi import MidiHandler

mockfile = MidiFile('song.mid')

class TestMidiHandler(unittest.TestCase):
    def setUp(self):
        self.handler = MidiHandler(mockfile)

    def test_get_all_valid_notes(self):
        count = 0
        for msg in mockfile:
            if msg.type == "note_on":
                count += 1
        notes = self.handler.get_notes()
        self.assertEqual(count, len(notes), "All valid notes extracted")

    def test_notes_are_equal_or_over_min_midi_pitch(self):
        notes = self.handler.get_notes()
        notes.sort()
        self.assertGreaterEqual(notes[0], 0, "All notes higher than minimum midi pitch")

    def test_notes_are_equal_or_under_max_midi_pitch(self):
        notes = self.handler.get_notes()
        notes.sort(reverse=True)
        self.assertLessEqual(notes[0], 127, "All notes less than maximum midi pitch")

    def test_notes_are_integers(self):
        notes = self.handler.get_notes()
        decimals_found = False
        for note in notes:
            if "." in str(note):
                decimals_found = True
                break
        self.assertFalse(decimals_found, "All notes are integers")
