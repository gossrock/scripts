#! /usr/bin/python3.6
import sys
current_dir = sys.path[0]
sys.path += [current_dir+'/utils']  # add utils repository to PYTHONPATH

import glob
import shlex
from utils.command_execution import Command, CommandManager

files = glob.glob("*.mkv") # may want to work this into command_execution

cm = CommandManager()

for old_file in files:
    new_file = old_file[:-4]+".mp4"
    print(f'converting {old_file} to {new_file}')
    old_file = shlex.quote(old_file)
    new_file = shlex.quote(new_file)
    cm.add(Command(f"ffmpeg -y -i {old_file} -codec copy {new_file}"))

cm.run_all()
