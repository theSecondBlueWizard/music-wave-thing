from dataclasses import dataclass

@dataclass
class NoteString:
    name: str
    duration: float

def read_file_to_list(filepath):
    notes: list[NoteString] = []
    with open(filepath, 'r') as file:
        for line_number, line in enumerate(file):
            datum = line.split()
            if not datum:
                continue

            if len(datum) != 2:
                raise ValueError(f"Line {line_number!r} is malformed: {line!r}") 
            
            note_str, duration = datum[0], datum[1]

            duration = float(duration)
            notes.append(NoteString(note_str, duration))
    return notes


