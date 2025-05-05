from scipy.io import wavfile
from wave_generators import *
from file_reader import read_file_to_list
from music_reader import read_notes
import numpy as np

A4_FREQUENCY = 440.0
BPM = 180.0
AMPLITUDE=0.03

SQUARE_FRACTION = 0.6


if __name__ == "__main__":

    musical_notes = read_file_to_list("examples/sunday-clothes.txt")
    physical_notes = read_notes(musical_notes, A4_FREQUENCY, BPM)
    
    wave_generator = Sinusoidal()
    wave_generator2 = Square()

    samples = []
    for note in physical_notes:
        new_note = wave_generator.generate_samples(note.frequency, note.duration)
        samples.extend(new_note)
    sinusoudal_arr = np.array(samples)
    
    samples2 = []
    for note in physical_notes:
        new_note = wave_generator2.generate_samples(note.frequency, note.duration)
        samples2.extend(new_note)
    square_arr = np.array(samples2)

    sample_arr = (1 - SQUARE_FRACTION) * sinusoudal_arr + SQUARE_FRACTION * square_arr

    wavfile.write("sunday-clothes.wav", wave_generator.sample_frequency, AMPLITUDE * sample_arr)