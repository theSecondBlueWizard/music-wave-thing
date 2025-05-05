from scipy.io import wavfile
from wave_generators import *
from file_reader import read_file_to_list
from music_reader import read_notes
import numpy as np

A4_FREQUENCY = 440.0
BPM = 180.0
# AMPLITUDE=1



if __name__ == "__main__":

    musical_notes = read_file_to_list("examples/sunday-clothes.txt")
    physical_notes = read_notes(musical_notes, A4_FREQUENCY, BPM)
    
    wave_generator = Square()
    wave_generator2 = Sinusoidal()

    samples = []
    for note in physical_notes:
        new_note = wave_generator.generate_samples(note.frequency, note.duration)
        samples.extend(new_note)
    sample_arr = np.array(samples)
    
    samples2 = []
    for note in physical_notes:
        new_note = wave_generator2.generate_samples(note.frequency, note.duration)
        samples2.extend(new_note)
    sample_arr += np.array(samples2)

    wavfile.write("sunday-clothes.wav", wave_generator.sample_frequency, sample_arr)