#!/bin/bash

# Sets up CLIc for use on the command line with the command "CLIc"

if [ -d '/home/`whoami`/.CLIc' ]; then
    mkdir /home/`whoami`/.CLIc
fi
cp CLIc.py /home/`whoami`/.CLIc/CLIc.py && cp README.md /home/`whoami`/.CLIc/README.md
cp LICENSE /home/`whoami`/.CLIc/LICENSE
cp CLIc2.gif /home/`whoami`/.CLIc/CLIc2.gif
touch /home/`whoami`/.bash_aliases
if [ 'grep -Fq "alias CLIc" /home/`whoami`/.bash_aliases' ]; then
    true
else
    echo "alias CLIc='cd /home/`whoami`/.CLIc && python CLIc.py'" >> /home/`whoami`/.bash_aliases

fi
