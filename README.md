CLIc
====

A command line chess game, written in Python.

![alt text](http://img.photobucket.com/albums/v235/glamtwatwhore/clic-1.png "CLIc splash")

CLIc is still under development and has not yet been fully tested. As each new 
function is built (or existing functions are amended) a brief test has been 
carried out to ensure that the function works. It has not, however, been 
sanity tested so the game in its current form is buggy at best.

As this receives alpha version updated, more extensive testing will be
carried out prior to a release candidate push/commit to GitHub.


Setting Up
----------

Download the git repo to your computer. Navigate to the src directory that 
contains the "install.sh" file and run

```bash
chmod +x install.sh
./install.sh
```

Exit the shell and reopen. You can now play CLIc by running the command 

```bash
CLIc
```

in the terminal.



How To Play
-----------

These rules explain how to play CLIc, not how to play chess. If you don't 
know how to play chess, why did you download this?

> Moves are controlled using non-algebraic notation, with one move per prompt

> Enter which piece you would like to move at the first prompt

> Enter which space you would like to move to at the second prompt

> Keep an eye out at the top of the screen for error messages - some inputs 
do not allow your move to be completed

> To castle Kingside, at the move prompt (either the first or second) type in 
"o-o" (the letter "o" not the number zero) without the quotes. Leave the other
 prompt empty

> To castle Queenside, at the move prompt (either the first or second) type in 
"o-o-o" (the letter "o" not the number zero) without the quotes. Leave the 
other prompt empty

> Do not try to do an *en-passant* move because it wont work


Notes
-----

There is a reimplementation in progress, looking to release version 2.0 at 
some point. Whilst there has never been a proper release of version 1.x, it
has been at alpha stage for some time.

I'm now a bit better of a programmer than when I started this, so v2 will be
tidier code-wise and much easier to maintain. In the meantime, ignore the 
folder called "NewCLIc"
