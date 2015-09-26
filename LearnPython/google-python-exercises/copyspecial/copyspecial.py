#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
# import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them


def main():
    import pdb
    pdb.set_trace()
    # This basic command line argument parsing code is provided.
    # Add code to call your functions below.

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if not args:
        print "usage: [--todir dir][--tozip zipfile] dir [dir ...]"
        sys.exit(1)

    # todir and tozip are either set from command line
    # or left as the empty string.
    # The args array is left just containing the dirs.
    result = []
    if not os.path.exists(args[1]):
            os.mkdir(args[1])
    paths = os.listdir(args[1])
    if args[0] == '--todir':
        for fname in paths:
            match = re.search(r'__(\w+)__', fname)
            if match:
                result.append(os.path.abspath(os.path.join(args[1], fname)))
        print result

    # tozip = ''
    if args[0] == '--tozip':
        zipfile = ''
        cmd = 'zip -j ' + zipfile + ' ' + ' '.join(paths)
        (status, output) = commands.getstatusoutput(cmd)
        print output

    if len(args) == 0:
        print "error: must specify one or more dirs"
        sys.exit(1)

    # +++your code here+++
    # Call your functions
if __name__ == "__main__":
    main()
