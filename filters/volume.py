from filters.base import BaseFilter

class VolumeFilter(BaseFilter):
    def __init__(self, volume):
        self.volume=volume
    
    def excecute(self, samples):
        return samples * self.volume