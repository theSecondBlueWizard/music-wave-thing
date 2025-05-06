from filters.base import BaseFilter

class DistortionFilter(BaseFilter):
    def __init__(self, cutoff):
        self.cutoff = cutoff
    
    def excecute(self, samples):
        max_amplitude = samples.max() * self.cutoff
        samples[samples>max_amplitude] = max_amplitude
        samples[samples<-max_amplitude] = -max_amplitude
        return samples