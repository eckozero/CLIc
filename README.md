CLIc
====

A command line chess game, written in Python

CLIc is still under development and has not yet been tested fully.
As each new function is built (or existing functions amended) a
brief test has been carried out to ensure that the function works;
it has not been sanity tested so the game in its current form is buggy

As this receives alpha version updates, more extensive testing will be
carried out prior to a release candidate push/commit to GitHub


**Version Update**

I have finally fixed some bugs. The biggest bug was that pawn movement didn't _actually_ 
work before. I have now fixed the redraw issue where any +1 movement for pawns was 
redrawing an incorrect pawn.

Known bugs/issues as at 16/10/13:

>If you try and move black pawn a7 to anywhere legal, the program crashes
>No legal move rules for queens
>No legal move rules for kings

>No collision detection (e.g. not running through your own pieces)

>No capture rules (e.g. continuing past an opposing piece)

>No check rules

>No castling

>No pawn captures

>No _en passant_ (and there likely never fucking will be)

Such is life, eh?
