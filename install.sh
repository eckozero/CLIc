#!/bin/bash

# Sets up CLIc for use on the command line with the command "CLIc"

if [ -d '/home/`whoami`/.CLIc' ]; then
    mkdir /home/`whoami`/.CLIc
fi
cp CLIc.py /home/`whoami`/.CLIc/CLIc.py && cp README.md /home/`whoami`/.CLIc/README.md
cp LICENSE /home/`whoami`/.CLIc/LICENSE
touch /home/`whoami`/.bash_aliases

echo "alias CLIc='cd /home/`whoami`/.CLIc && python CLIc.py'" >> /home/`whoami`/.bash_aliases

