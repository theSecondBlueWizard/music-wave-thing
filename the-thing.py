from scipy.io import wavfile
from scipy import signal
from matplotlib import pyplot as plt
import filters
import parsers
import wave_generators
import filters
import numpy as np

A4_FREQUENCY = 440.0
BPM = 180.0
AMPLITUDE = 0.03
SAMPLE_FREQUENCY = 44_100

visualise_filter = False
visialise_spectrogram = False




if __name__ == "__main__":
    musical_notes = parsers.read_file_to_list("examples/sunday-clothes.txt")
    physical_notes = parsers.read_notes_to_frequencies(musical_notes, A4_FREQUENCY, BPM)
    
    wave_generator = wave_generators.Square(sample_frequency=SAMPLE_FREQUENCY)

    samples = []
    for note in physical_notes:
        new_note = wave_generator.generate_samples(note.frequency, note.duration)
        samples.extend(new_note)
    sample_arr = np.array(samples)

    musical_notes = parsers.read_file_to_list("examples/sunday-clothes-bass.txt")
    physical_notes = parsers.read_notes_to_frequencies(musical_notes, A4_FREQUENCY, BPM)
    
    wave_generator = wave_generators.Square(sample_frequency=SAMPLE_FREQUENCY)

    samples = []
    for note in physical_notes:
        new_note = wave_generator.generate_samples(note.frequency, note.duration)
        samples.extend(new_note)
    
    if len(sample_arr) > np.array(samples).size:
        sample_arr = sample_arr[:np.array(samples).size] + np.array(samples)
    else:
        sample_arr += np.array(samples[sample_arr.size:])
        
    for filter in [
                filters.HighPassFilter(min_frequency=100, sample_frequency=SAMPLE_FREQUENCY),
                filters.LowPassFilter(max_frequency=15_000, sample_frequency=SAMPLE_FREQUENCY),
                # filters.DistortionFilter(cutoff=0.9),
            ]:
        sample_arr = filter.excecute(sample_arr)

    if visualise_filter:
        plt.plot(filter)
        plt.show()

    if visialise_spectrogram:
        # Thought a pixel per quarter beat would be smart-ish
        fs = SAMPLE_FREQUENCY         # e.g. 44100
        f, t, Sxx = signal.spectrogram(
            sample_arr,
            fs=fs,
            window='hann',
            nperseg=int(fs * 60 / BPM),  # quarter-beat window
            noverlap=0,
            scaling='density',
            mode='magnitude'
        )

        plt.pcolormesh(t, f, 20*np.log10(Sxx + 1e-10), shading='gouraud')
        plt.ylabel('Frequency [Hz]')
        plt.xlabel('Time [sec]')
        plt.title('Spectrogram')
        plt.colorbar(label='Magnitude [dB]')
        plt.show()

    wavfile.write("sunday-clothes.wav", SAMPLE_FREQUENCY, AMPLITUDE * sample_arr)

    # CLI
    # Multiple files?
    # silence

    # Discover wave_generators and filters automatically