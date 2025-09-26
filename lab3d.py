#!/usr/bin/env python3
'''Lab 3 Inv 2 function free_space '''
# Author ID: 133383224

import subprocess

def free_space():
    # Run the shell command
    result = subprocess.run(
        "df -h | grep '/$' | awk '{print $4}'",
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    # Decode to string, strip newline
    return result.stdout.decode('utf-8').strip()

if __name__ == '__main__':
    print(free_space())
