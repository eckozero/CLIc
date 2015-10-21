from Mechanics import Gameplay

# Yeah that's supposed to be a King in the ascii. Shut up.
clic-splash = [
["                                                                          "]
["                                                      |__|                "],
["                                                   |  _||_  |             "],
["       _______    ____        ____                 |_/    \_|             "],
["      /   ____|   |  |        |  |                 \__    __/             "],
["     /   /        |  |        |  |    _____           |  |                "],
["    |   |         |  |        |  |   /  ___|         /    \               "],
["    |   |         |  |        |  |  /  /             |    |               "],
["     \   \____    |  |____    |  |  \  \___      ____|    |____           "],
["      \_______|   |_______|   |__|   \_____|    /______________\          "],
["                                                                          "],
["                      Command     Line    Chess                           "],
["                                                                          "],
["                                                                          "],
["What would you like to do?                                                "],
["                                                                          "],
["1. Start new game (vs human)                                              "],
["2. Start new game (vs CPU)                                                "],
["3. Load existing game                                                     "],
["4. Quit                                                                   "],
]

# Clearly this isn't going to work, and I'm going to disable it because it will
# frustrate the hell out of me but whatever

# No selection made so current selection false
selection_valid = False

while selection_valid != True:
  game_selection = raw_input("Please make a selection (1, 2, 3, or 4): ")

  if game_selection not in (1,2,3,4):
    print "Not a valid selection.\n"
    print "What would you like to do?\n"
    print "1. Start new game (vs human)"
    print "2. Start new game (vs CPU)"
    print "3. Load existing game"
    print "4. Quit"
  else:
    selection_valid = True

if game_selection == 4:
  Gameplay().end_game()
