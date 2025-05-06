# Wave generators
This directory contains all the implemented wave generators. Honestly this might be what is usually called "instruments", though I'm not entirely sure.

## Implementing your own
This was written to be as easily extensible as possible. Should be as easy as writing a child class of `BaseWaveGenerator` in `base.py`, and `generate_samples(self, pitch, duration)`. Further options should be possible to pass down, once the CLI is implemented.

All that's required of the wave is that they implement `generate_samples(self, pitch, duration)`. It should be $1$-periodic (note not $2 \pi$-periodic), and have a range of $\langle -1, 1\rangle$. I don't actuallty know if scipy reacts poorly to numbers outside this range, but I don't think I want to find out the bad way.

Further settings for your wave generator can be passed into your `WaveGenerator()` object, as long as they also pass the `sample_frequency` at a default of $44 \ 100$ kHz too. Honestly the sample-durations `fade_in` and `fade_out` should probably be part of the base class too, I'll see when I can fix that up.