from dataclasses import dataclass

@dataclass
class NoteString:
    name: str
    duration: float

def read_file_to_list(filepath):
    """
    Parses text file of expected format to a list of note strings.

    Text file should be formatted as follows:
    > ab4 1.0

    > b3 0.25
    
    > a4 0.75
    
    Parameters
    ----------
    filepath : string
        File to be read

    Returns
    -------
    notes : list[NoteString(name: str, duration: float)]
        List of notes in format {note}{accent?}{octave} and their duration
    """
    notes: list[NoteString] = []
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
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
    except FileNotFoundError:
        raise FileNotFoundError(f"No file found at {filepath!r}") 
    except IOError:
        raise IOError(f"Error occured while reading file at {filepath!r}") 
    except OSError:
        raise OSError(f"Somwthing weird happened when trying to read file at {filepath!r}") 


