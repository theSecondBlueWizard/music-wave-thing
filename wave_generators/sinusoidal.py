from wave_generators.base import BaseWaveGenerator
import numpy as np

class Sinusoidal(BaseWaveGenerator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def generate_samples(self, pitch, duration):
        def wave_function(t):
            return np.sin(pitch * 2 * np.pi * t)
        t_arr = np.arange(0, duration, 1/self.sample_frequency)
        samples = list(map(wave_function, t_arr))
        return list(samples)