class MidiHandler:
    """
    Handles various midi file operations.

    Attributes:
        midifile: A midi file used as the source.
    """

    def __init__(self, midifile):
        self.mid = midifile

    def get_valid_note(self, note: int):
        """
        Ensures the midi note is valid, i.e. in range [0, 127].

        Args:
            note: The midi note to be validated.

        Returns:
            The note as a valid midi note.
        """

        return max(min(note, 127), 0)

    def get_notes(self):
        """
        Forms a list of valid midi notes by looping through the midi file's messages.

        Returns:
            The list of midi notes.
        """

        notes = []
        for msg in self.mid:
            if msg.type == "note_on":
                # velo = round(msg.velocity, -1)
                # time = round(msg.time, 2)
                # notes.append({"note": note, "velo": velo, "time": time})
                note = self.get_valid_note(int(msg.note))
                notes.append(note)

        return notes
