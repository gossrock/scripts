#! /usr/bin/python3.6

import glob
import shlex
from utils.command_execution import run

files = glob.glob("*.mkv") # may want to work this into command_execution
for old_file in files:
    new_file = old_file[:-4]+".mp4"
    old_file = shlex.quote(old_file)
    new_file = shlex.quote(new_file)
    print(f'converting {old_file} to {new_file}')
    command = f"ffmpeg -y -i {old_file} -codec copy {new_file}"
    run(command)
