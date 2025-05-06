# Sheet music file structure:
This was written to be as quick and dirty as possible. Every note is on a single line. This must include the note and octave, as well as the number of beats for which the note is plaid(as a float). For example:
>```
>c4 0.25
>e4 0.25
>f4 0.25
>d4 0.25
>a4 0.75
>a4 0.75
>g4 1.5
>```

The BMP would be nice to set in the file itself, but oh well, that's a task for later. Would also be cool to have a tempo flag...

## Writing your own
I hope this should be pretty self-explanatory...
Tracks are separete files. Metadata isn't imlpemented, but something human-readable would be nice.

## TODO
Silence or breaks haven't been implemented. This is pretty cursed, and is very much a nice to have. A dash could be nice maybe?