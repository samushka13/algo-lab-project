import mido

if __name__ == "__main__":
    mid = mido.MidiFile('song.mid')
    notes = []
    for msg in mid:
        if msg.type == "note_on":
            note = msg.note
            velo = round(msg.velocity, -1)
            time = round(msg.time, 2)
            notes.append({"note": note, "velo": velo, "time": time})

    for note in notes:
        print(note)
