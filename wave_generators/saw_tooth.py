from .base import BaseWaveGenerator
import numpy as np

class SawTooth(BaseWaveGenerator):
    def __init__(self, fade_in=200, fade_out=200, **kwargs):
        """
        Generates SawTooth wave.
        
        Linear fade in/out meant to avoid clicking.

        Parameters
        ----------
        fade_in : int
            Number of samples 
        fade_out : int
            Number of samples 

        Returns
        -------
        SawToothWaveGenerator : WaveGenerator
        """
        self.fade_in = fade_in
        self.fade_out = fade_out
        super().__init__(**kwargs)

    def generate_samples(self, pitch, duration):
        def wave_function(t):
            return 2 * pitch * t % 1
        t_arr = np.arange(0, duration, 1/self.sample_frequency)
        samples = list(map(wave_function, t_arr))

        for i in range(self.fade_in):
            samples[i] *= i / self.fade_in
        for i in range(self.fade_out):
            samples[-i] *= i / self.fade_out
            
        return list(samples)