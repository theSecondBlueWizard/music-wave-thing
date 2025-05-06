# Parsers
This is really more of the "others" directory where I just didn't want all the logic to be in the main file for ease of readability. Implementation details shouldn't matter to that file, all that's important is that the code reacts predictably.

## `file_reader.py`
Responsible for reading the `.txt` files into a format easier modified in code. At the moment this is a `dataclass` containing note name (a string of the english name of the note, accentuations if any, and octave) and duration in number of beats

Upon reflection this being a separate class is actively damaging to the project, should've just stuck to returning a list of note durations and note strings. You live and you learn ;))

## `music_reader.py`
Converts the list returned from the file above to a list of frequencies. Technically it returns `NoteFrequency` objects, the regrets to which have already been outlined. Can be massively more performant if this is ripped out and vectorised, but that's by the by.