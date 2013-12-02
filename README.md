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

_Update_

Well that was a little embarassing. I'd been deliberately avoiding the bug 
for pawn redraw where choosing the other persons piece still redrew the board 
because I was worried I'd get caught up in it. Turns out it was a simple 
two-lines-of-code job to fix. Whoops.

Still, one less (known) bug.

__28/10/13:__

Fixed some crap in the collision detection function (which is just hideous by 
the way). Lists no longer explode as you move around the board although I 
haven't had chance to check bishop and queen diagonal moves. I have piece 
capture built into the collision detection though, and now Knights can't 
capture Kings (although they're the only piece that can't...)

Pawn capture is not as stable as I thought. I can't get it to play nicely with 
collision detection.


__29/10/13:__

The collision detection module is now 152 lines of ugly, ugly code. But it 
does work, so assuming the old adage 'Functional > Elegant' I think it's a 
win.

The __redraw_valid()__ problem has been solved by shuffling some code around 
and adding one more line in.


__30/10/13:__

The __redraw_valid()__ problem is still a problem. I had to remove the fix 
because it broke pawn moves. I can fix it though, just not tonight.

In **much** better news, I started making a check function. I'm still not 
100% sure on how it's going to work at the end... but that's because I code 
like I write.

Currently, all it does is find the co-ordinates of the King on the board with 
a couple of pre-validation checks. Now it does that, it's a _simple_ 
(naturally) matter of separately counting back to row 0, up to row 8, down to 
column 0, up to column 0, and going up +/- _n_ for diagonals and checking 
that nothing of the opposing piece is in any of those spaces, unless something 
is in the way. Easy, right?


__31/10/13:__

Check works surprisingly exactly like it does in my update above. I have check 
for rooks and queens on non-diagonals picked up by the function now. I will 
have to do some kind of acrobatics to make it actually spit out a usable 
result, but that's not what I'm building right now.


__11/11/13:__

There has been an 11 day hiatus because I was participating in [NaNoWriMo]
(http://nanowrimo.org) so now that I've finished my novel, I'm back to chess.

Annoyingly enough this update is to say that I fixed some code that I mangled 
on 31/10/13 regarding collision detection.

Check is giving me a headache, and I can't write code tonight.


__13/11/13:__

Added a Class for check, rather than trying to squeeze everything into one 
ridiculously oversized function. It's going well, and the Check class can now 
find the King *(always a good start)* **and** check horizontal spaces. It 
also now stops running if one of your pieces is blocking the King, because
obviously it's not in check in that case.

__14/11/13:__

Added vertical check validation. The code is virtually identical to the code for above.

Started added diagonal check validation. Ran into the snag that where I thought I was 
running all four directions I was just running two directions, twice.

This is a very trivial update, because it's copy, paste, slightly amend.


__15/11/13:__

The big brain am winning again.

Managed to fix the **check_d()** function. I still need to sort out the issues with check 
validation happening at the wrong time, and add in something to make it so you can't move 
into check, and you can't make a move that would then put you in check but little steps... 
If you're wondering, I'm quoting Futurama for no raisin.


__18/11/13:__

Implemented **check_k()** function which decides whether a king is in check by 
a ka-nig-et or not (Ni!). Not fully tested but definitely works from King 
starting position. Same detail with the chess function as above - it can tell 
whether a position is check, but can't stop play until the issue is resolved 
and will let you move into check. Still, knight check is mighty fine step in 
the right direction.

__23/11/13:__

Check now (sort of) works. It determines whether or not the kings are in check 
and then doesn't let you make a move unless it's to get out of check. Also now 
you can't move *into* check, which is good.

Castling will need some work to make sure you don't castle out of, through or
into check but it's coming along nicely.


__02/12/13:__

Well, there's a minor bug fix gone in. It's unimportant but it was a bug.

If you typed in, for example, a23-a4 it would evaluate as a2-a4. As the length 
of the string wasn't spitting up an error in the try/except clause it never 
failed. I have added in a second evaluation for the moves that specifically 
checks the length and fails the evalutation if the length is not 2.

Like I said, not important but a bug, either way.

Additional: I did a little fix for castling. Now you can't castle if there 
are pieces in the way. The code is still ugly as sin, and you can castle into 
through or out of check, but this can all be fixed.


Known bugs/issues as at 16/11/13:

>~~If you try and move black pawn a7 to anywhere legal, the program crashes~~

>~~Valid redraw only occurs for certain moves~~

>~~Knights can move incorrectly _(specifically (row+/-1 & column+/-1)_~~

>~~No legal move rules for queens~~

>~~No legal move rules for kings~~

>~~No collision detection _(e.g. not running through your own pieces)_~~ 
~~Collision detection ~~but no~~ with _some_ capture rules

>~~No capture rules _(e.g. continuing past an opposing piece)_~~ Partially 
fixed, see updates 27/10/13 for details

>No check rules - see updates for latest

>~~No castling~~ ~~_White castling_~~

>~~No pawn captures~~

>No __en passant__ _(and there likely never fucking will be - seriously, that rule is 
>completely ridiculous)_

>~~Issues with redraw, particularly around pawn n2-n4 movements~~

> ~~Pawn capture only works for column +1, not column -1~~

> ~~Pawn function will redraw the board even if you didn't move your own pawn~~

> Unfortunately, the __redraw_valid()__ function doesn't quite do what I want 
it to and if you move other people's pieces, it redraws. _Reinstated bug_

> ~~Pawn capture OR collision detection, not both~~

> ~~Evalutates moves that have character 0 as a letter and character 1 as a 
number incorrectly~~


All in, things are shaping up nicely. I mean, seriously. I can almost _taste_ 
completion. ~~Check is going to be a bugger though.~~ Check is coming along 
nicely now, including its own class, which is nice because I thought I'd
forgotten how to use them.

The Check class is almost done, it has a function for horizontal, vertical and diagonal 
check validation. As per the update on 14/11/13 I have yet to make this work according to 
the rules of the game.


In other news, I found a simpler wording for the __en passant__ rule so I 
*may* look to add this in at some (much) later point.
