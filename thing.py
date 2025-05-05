from scipy.io import wavfile
from wave_generators import *
from file_reader import read_file_to_list
from music_reader import read_notes
import numpy as np

A4_FREQUENCY = 440.0
BPM = 120.0



if __name__ == "__main__":
    wave_generator = Sinusoidal()

    musical_notes = read_file_to_list("examples/c-scale.txt")
    physical_notes = read_notes(musical_notes, A4_FREQUENCY, BPM)
    

    samples = []
    for note in physical_notes:
        new_note = wave_generator.generate_samples(note.frequency, note.duration)
        samples.extend(new_note)
    sample_arr = np.array(samples)
    wavfile.write("C-scale.wav", wave_generator.sample_frequency, sample_arr)