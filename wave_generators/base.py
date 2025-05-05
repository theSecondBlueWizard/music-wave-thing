class BaseWaveGenerator():
    def __init__(self, *, sample_frequency=44_100):
        self.sample_frequency =  sample_frequency

    def generate_samples(self, pitch, duration):
        ...