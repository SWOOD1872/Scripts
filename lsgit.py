#!/usr/bin/env python3

import os
import sys

# Sets the cwd based on user input or the cwd where the script was executed
try:
    curdir = os.chdir(sys.argv[1])
except IndexError as e:
	curdir = os.chdir(os.getcwd())

# Empty list where directories which have git repos will get appended
gitrepos = list()

# Loop through system directories and append the full path of those which contain a git repo
for paths, dirs, files in os.walk(os.getcwd()):
    if '.git' in dirs:
        gitrepos.append(paths)

# Prints all directories which contain a git repo
if gitrepos:
    for gr in gitrepos:
        print(gr)
else:
    print('No git repos found')
