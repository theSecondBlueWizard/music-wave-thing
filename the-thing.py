from scipy.io import wavfile
import parsers
import wave_generators
import filters
import numpy as np

A4_FREQUENCY = 440.0
BPM = 180.0
AMPLITUDE=0.03

SQUARE_FRACTION = 0.6


if __name__ == "__main__":
    musical_notes = parsers.file_readerread_file_to_list("examples/sunday-clothes.txt")
    physical_notes = parsers.read_notes_to_frequencies(musical_notes, A4_FREQUENCY, BPM)
    
    wave_generator = wave_generators.Square()

    samples = []
    for note in physical_notes:
        new_note = wave_generator.generate_samples(note.frequency, note.duration)
        samples.extend(new_note)
    sample_arr = np.array(samples)

    wavfile.write("sunday-clothes.wav", wave_generator.sample_frequency, AMPLITUDE * sample_arr)

    # Filtering
    # CLI
    # Multiple files?

    # Discover wave_generators and filters