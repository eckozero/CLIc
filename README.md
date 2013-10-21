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

I have fixed the redraw issue for non-pawn moves by rewriting the __redraw_valid__ function.

Knight code is now not only working (no longer accepts row&column +/-1) it's slightly
more elegant. Not great, not by a long shot, but I've cut a lot of code to be left with
a fairly small function.

Now fixed the hideous a7-a(x) bug with a really ugly hack.
_Update: code is now slightly less hideous_

21/10/13: 
 Updated exception handler so the program doesn't crash for invalid input
 Added Queen moves.
 Added King moves

Known bugs/issues as at 21/10/13:

>~~If you try and move black pawn a7 to anywhere legal, the program crashes~~

>~~Valid redraw only occurs for certain moves~~

>~~Knights can move incorrectly _(specifically (row+/-1 & column+/-1)_~~

>~~No legal move rules for queens~~

>~~No legal move rules for kings~~

>No collision detection _(e.g. not running through your own pieces)_

>No capture rules _(e.g. continuing past an opposing piece)_

>No check rules

>No castling

>No pawn captures

>No __en passant__ _(and there likely never fucking will be - seriously, that rule is 
>completely ridiculous)_

Such is life, eh?
