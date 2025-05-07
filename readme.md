# music-wave-thing
I've wanted to have a buzzy version of [the wall-e intro song](https://www.youtube.com/watch?v=DHP9BVo7X1w) (technically from a 60s broadway musical called [Hello, Dolly!](https://en.wikipedia.org/wiki/Hello,_Dolly!_(musical)), which sort of makes sense in context) as my ringtone for a while. The smart move would probably be to transcribe it in musescore and export to MIDI or just directy to a mp3, or directly in garage band [seeing as that's the only official way of setting a custom rindtone on an iOS device](https://support.apple.com/en-us/120692), hovever...
what's the fun in that?

Music is just sounds, which is just waves at different frequencies, so here's a quick tool to convert a textual representation of sheet music into a very rudamentary synth-soudning `.wav` file.

I doubt this will be useful to anyone, it's mostly a learning opportunity for me in organising a project, some rudamentary things somewhere between wave physics and music theory, and just doing stugg. Maybe someone gets some use out of this thing, who knows?

## Installation
Project uses `pipenv` for venv/library management, for those not into python (though if you're here I'm surprised you'd be here honestly), you install it by 
```shell
python3 -m pip install pipenv
```
Of course this requires you to have [python 3.13](https://www.python.org/downloads/) on your system, which I won't go into. From former experience and confusion I didn't feel like including a `Pipfile.lock` in the repo, so feel free to install the required packages with pipenv if its on your path, or alternatively
```shell
python3 -m pipenv install
```
Honestly I'd like to see if I can't reimplement the things I'm using `scipy` for, namely generating spectrograms and writing the final `.wav` file, however I'm afraid that's a project for a later date

## Usage
You can run the main file in this repo's root directory by
```shell
python3 -m pipenv run python the-thing.py
```
Please don't judge choice of naming, I'm smack in the middle of exam season and should probably focus on [algebra](https://www.ntnu.edu/studies/courses/TMA4150#tab=omEmnet).

## Project setup
The main file is `the-thing.py`. It first calls out to the `parsers` module to read the file using `file_reader.py` from the textual representation into a format that's surprisingly and coincidentally close in ideology to [the MIDI format](https://en.wikipedia.org/wiki/MIDI), except whereas they do something smart I don't quite get, I simply affix `A0` to integer 0, and increase by semitones, making our favourite `A4`, which we by default set to $440$ Hz, number 48. This is then read by `music_reader.py` to return the same format, except with the frequency of the notes instead. See `parsers/readme.md`, or the code itself for more.

We then move on to the wave generators in `wave_generators`. These were implemented to be as interchangable as possible - though upon reflection I think most interest will be in `square.py`, as it carries the most frequencies of the generators I could come up with. Nonetheless - all of these are of period and amplitude `1` for simplicity's sake. They also have a linear fade-in and fade-out to avoid the clicking between notes, a necessary sacrifice as far as I know. New `wave_generators` are implemented as children of `BaseWaveGenerator()` in `wave_generators/base.py`, and added to `wave_generators/__init__.py` for namespacing. The OOP is not strictly necessary and may be more hurt than benefit, but hindsight is 20/20!

Finally, filters are applied. While I at first wanted to just pass a spectrogram into them, this would limit what filters could do by themselves. Therefore every filter recieves just the raw samples we're working with.

## TODO's
I'd really like to make a nice CLI interface for writing multiple files on top of one another, perhaps even with different wave generators and filters applied. I'm picturing this as something like
```shell
music_wave_thing -i 'file_1.txt' -w square -f HighPass 500 -f LowPass 1500 -i 'file_2.txt' -w sinusoidal -o 'out.wav'
```
, but that may be optimistic of me.

It'd also be nice to have more robust wave generators (instruments I suppose you'd call them) with a dynamic intensity, a curve growing rapidly at first, then with an exponential decay. Could give the results a bit more character

Finally, the filters could use some love. Some cooler phase-based things would be neat, apparently this is as simple as taking the imaginary part of the FFT, which sort of makes intuitive sense, though I'm afraid I'll have to wait until [signal processing](https://www.ntnu.edu/studies/courses/TFY4280/#tab=omEmnet) for a proper grasp of how that is. I also think this would benefit from allowing for per-note filters. Honestly that might not be a bad idea in general, would make enveloping a curve onto the notes a bit easier

Much less importantly, automatic wave generator and filter discovery would be nice in their respective `__init__.py` files, though it seems that's not particularly pythonic of me...

https://www.youtube.com/watch?v=nLx_7wEmwms
