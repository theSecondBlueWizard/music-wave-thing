# Filters
These are the filters that can be used on the calculated waves for hopefully a slightly less boring sound.

## Implementing your own
These are classes much like the ones in `wave_generators`, easily extended by adding a file, inherit from `BaseFilter()` in `filters/base.py`, and added to `filters/__init__.py`. Their function is `excecute(self, samples)`, where samples is a list of floats representing the wave intensities at any point, with the physical time being found from the `sample_frequency` sometimes passed into the filter.

## TODOs
Would be nice to think of how these should be applied on both a per-note level, per-track level, and per-output level. There must be some pretty solution here. Also separate consearns between the base class and the rest.
