from dataclasses import dataclass
from .file_reader import NoteString

SEMITONE_RATIO = 2 ** (1/12) # Comes from music theory: https://en.wikipedia.org/wiki/Twelfth_root_of_two

@dataclass
class NoteFrequency:
    frequency: float
    duration: float

def note_string_to_int(note_string: str, semitone_char: str, octave: int):
    match note_string:
        case 'c': note_int = 4 - 12
        case 'd': note_int = 6 - 12
        case 'e': note_int = 8 - 12
        case 'f': note_int = 9 - 12
        case 'g': note_int = 11 - 12
        case 'a': note_int = 1
        case 'b': note_int = 3
        case 'h': note_int = 3
        case _:
            raise ValueError(f"Parsing unexpecting note string {note_string!r}") 


    match semitone_char:
        case 'b': note_int -= 1
        case '#': note_int += 1
        case '': note_int += 0
        case _:
            raise ValueError(f"Parsing unexpecting accent {semitone_char!r}") 
    
    return note_int + (12 * octave)

def note_int_to_frequency(note_int: int, a4_frequency: float):
    """
    Parses note from number of relative halftones to a0 to frequency.
    
    Assumes chromatic 12-semitone scale.
    
    Parameters
    ----------
    note_int : int
        Position of note in terms of half-tones relative to a0
    a4_frequency : float
        Frequency of the a4 note in hertz. Typically 440, sometimes 442

    Returns
    -------
    frequency : float
        Frequency of requested note
    """
    a4_int = note_string_to_int('a', '', 4)
    a4_interval = note_int - a4_int
    frequency = a4_frequency * (SEMITONE_RATIO ** a4_interval)
    return frequency

def read_notes_to_frequencies(notes: NoteString, a4_frequency: float=440, bpm: float=80) -> list[NoteFrequency]:
    """
    Parses list of notes as strings to a list of fequencies
    
    Parameters
    ----------
    notes : list[NoteString(name: str, duration: float)]
        List of notes {note}{accent?}{octave}, and their duration
    a4_frequency : float
        Frequency of the a4 note in hertz. Typically 440, sometimes 442
    bpm : float
        Number of beats per minute.

    Returns
    -------
    notes : list[NoteFrequencies(frequency: float, duration: float)]
        List of frequencies and durations
    """
    read_notes = []
    for note_number, note in enumerate(notes):
        note_string = note.name
        if not (2 <= len(note_string) <= 3):
            raise ValueError(f"Unexpected length of note string {note_string!r}, note number {note_number!r}") 
        
        note_char = note_string[0]
        if not note_char.isalpha():
            raise ValueError(f"Unexpected note string {note_string!r}, note number {note_number!r}") 
        
        if not ('a' <= note_char <= 'h') and not ('A' <= note_char <= 'H'):
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


