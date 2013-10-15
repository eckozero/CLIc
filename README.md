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

Today is 15/10/13 and I have finally fixed some bugs. The biggest bug was that
pawn movement didn't __actually__ work before. It does now, with a caveat:

>If you try and move black pawn a7 to a6, the program crashes

Such is life, eh?
