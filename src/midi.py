class MidiHandler:
    def __init__(self, midifile):
        self.mid = midifile

    def get_notes(self):
        notes = []
        for msg in self.mid:
            if msg.type == "note_on":
                note = msg.note
                # velo = round(msg.velocity, -1)
                # time = round(msg.time, 2)
                # notes.append({"note": note, "velo": velo, "time": time})
                if note > 127:
                    notes.append(round(127))
                elif note < 0:
                    notes.append(round(0))
                else:
                    notes.append(round(note))

        return notes
