from filters.base import BaseFilter
import numpy as np

class LowPassFilter(BaseFilter):
    def __init__(self, max_frequency, sample_frequency=44_100):
        self.max_frequency = max_frequency
        self.sample_frequemcy = sample_frequency
    
    def excecute(self, samples):
        frequency_spectrum = np.fft.rfft(samples)
        frequencies = np.fft.rfftfreq(len(samples), d=1/self.sample_frequemcy)
        mask = (frequencies <= self.max_frequency)
        filtered_spectrum = mask * frequency_spectrum
        return np.fft.irfft(filtered_spectrum, n=len(samples))