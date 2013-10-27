CLIc
====

A command line chess game, written in Python

CLIc is still under development and has not yet been tested fully.
As each new function is built (or existing functions amended) a
brief test has been carried out to ensure that the function works;
it has not been sanity tested so the game in its current form is buggy

As this receives alpha version updates, more extensive testing will be
carried out prior to a release candidate push/commit to GitHub


Version Update
--------------

I have finally fixed some bugs. The biggest bug was that pawn movement didn't _actually_ 
work before. I have now fixed the redraw issue where any +1 movement for pawns was 
redrawing an incorrect pawn.

I have fixed the redraw issue for non-pawn moves by rewriting the __redraw_valid__ function.

Knight code is now not only working (no longer accepts row&column +/-1) it's slightly
more elegant. Not great, not by a long shot, but I've cut a lot of code to be left with
a fairly small function.

Now fixed the hideous a7-a(x) bug with a really ugly hack. 
_Update: code is now slightly less hideous_

__21/10/13:__ 

 Updated exception handler so the program doesn't crash for invalid input

 Added Queen moves.

 Added King moves

__23/10/13:__

Well that was fun. I made some changes, tidied up code and the like, and then pawn movement 
totally crapped out on me. Luckily, GitHub stores raw files of every commit, so it was a 
simple case of rolling back until I found a version that worked, then making sure to not 
try and get clever with the pawn movement code. It's ugly as hell but by god it works.

Anyway, I've now added the stuff back in and debugged queen and king moves. Seems like 
I should call it on this for now...

__24/10/13:__

I have added in some form of pawn captures today. The code came to me at work 
and I made a mental note of it. The code that's in the program is pretty 
much only syntatically different from my mind code. There's probably bugs 
in there though, so I wont celebrate too much.

__25/10/13:__

There are definitely bugs in the pawn capture. Namely pawn captures only work 
on one side (column +1, not -1).

Castling is being introduced. At the moment there is _white castling_ only. 
It also causes the program to crash but that's because I was more excited 
about committing the change than I was about the necessary amendments to the 
main loop to make sure it doesn't crash. In time though...


__26/10/13:__

King and queenside castling now completed. Code wise that is. It's still 
a bit free-and-easy with the rules. Remember kids, you can't castle into, 
through, or out of check. Not that CLIc cares about this at the moment...

The good thing is that I have now fixed the code that was causing the crash 
when the move was executed.

Removed bug that was causing pawn capture to go wrong.


__27/10/13:__

Added in some form of collision detection. You can't run through your own 
pieces anymore, but you can't capture opposing pieces either.


This section is (predictably enough) pretty difficult, code-wise. I have 
told it to search every square that the piece you control will go through, 
and then run it through varying degrees of evlauations (is the space empty, 
if not is it one of your own or an opposing piece etc) and then returning a
numerical value so the program knows whether to continue or not.

The latter part of the evaluations, are causing some problems but I have at 
least two types of pawn capture included in them; both types of white pawn 
capture as it happens. (My code is biased towards fixing white moves first 
as they are the first ones I encounter.)

There's also a bug where certain length moves to the left of the board as 
you look at it are causing a list to explode.


Known bugs/issues as at 24/10/13:

>~~If you try and move black pawn a7 to anywhere legal, the program crashes~~

>~~Valid redraw only occurs for certain moves~~

>~~Knights can move incorrectly _(specifically (row+/-1 & column+/-1)_~~

>~~No legal move rules for queens~~

>~~No legal move rules for kings~~

>~~No collision detection _(e.g. not running through your own pieces)_~~ 
Collision detection ~~but no~~ with _some_ capture rules

>~~No capture rules _(e.g. continuing past an opposing piece)_~~ Partially 
fixed, see updates 27/10/13 for details

>No check rules

>~~No castling~~ ~~_White castling_~~

>~~No pawn captures~~

>No __en passant__ _(and there likely never fucking will be - seriously, that rule is 
>completely ridiculous)_

>~~Issues with redraw, particularly around pawn n2-n4 movements~~

> ~~Pawn capture only works for column +1, not column -1~~

> Pawn function will redraw the board even if you didn't move your own pawn

All in, things are shaping up nicely.
