from dataclasses import dataclass

SEMITONE_RATIO = 2 ** (1/12) # Comes from music theory: https://en.wikipedia.org/wiki/Twelfth_root_of_two

@dataclass
class NoteFrequency:
    frequency: float
    duration: float

def note_string_to_int(note_string, semitone_char, octave):
    match note_string:
        case 'a': note_int = 1
        case 'b': note_int = 3
        case 'h': note_int = 3
        case 'c': note_int = 4
        case 'd': note_int = 6
        case 'e': note_int = 8
        case 'f': note_int = 9
        case 'g': note_int = 11
        case default:
            raise ValueError(f"Parsing unexpecting note string {note_string!r}") 


    match semitone_char:
        case 'b': note_int -= 1
        case '#': note_int += 1
        case '': note_int += 0
    
    return note_int + 12 * octave

def note_int_to_frequency(note_int, a4_frequency):
    a4_int = note_string_to_int('a', '', 4)
    a4_interval = note_int - a4_int
    frequency = a4_frequency * (SEMITONE_RATIO ** a4_interval)
    return frequency

def read_notes(notes, a4_frequency, bpm):
    read_notes = []
    for note_number, note in enumerate(notes):
        note_string = note.name
        if not (2 <= len(note_string) <= 3):
            raise ValueError(f"Unexpected length of note string {note_string!r}, note number {note_number!r}") 
        
        note_char = note_string[0]
        if not note_char.isalpha():
            raise ValueError(f"Unexpected note string {note_string!r}, note number {note_number!r}") 
        
        if not ('a' <= note_char <= 'h') and not ('A' <= note <= 'H'):
            raise ValueError(f"Unexpected note character {note_string!r}, note number: {note_number!r}") 
        note_char = note_char.lower()

        semitone_char = '' if len(note_string) == 2 else note_string[1]
        
        if semitone_char not in ['', 'b', '#']:
            raise ValueError(f"Unexpected semitone character {note_string!r}, note number: {note_number!r}") 
        
        octave = note_string[-1]

        if not octave.isdigit():
            raise ValueError(f"Unexpected octave {note_string!r}, note number: {note_number!r}") 
        octave = int(octave)

        note_int = note_string_to_int(note_char, semitone_char, octave)
        note_frequency = note_int_to_frequency(note_int, a4_frequency)

        note_duration = note.duration / bpm * 60.0

        read_notes.append(NoteFrequency(note_frequency, note_duration))
    return read_notes


