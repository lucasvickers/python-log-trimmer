#!/usr/bin/env python

import yaml
import os
import sys
import re


def trim_log_files(test=False):

    config = yaml.load(open('config.yaml', 'r'))

    os.chdir(config['path'])
    files = []
    for path in os.listdir('./'):
        if os.path.isfile(path):
            if re.match(config['log_regex'], path):
                files.append(path)

    if config['sort'] == 'alphanumeric':
        files.sort()
    elif config['sort'] == 'alphanumeric-reverse':
        files.sort(reverse=True)
    elif config['sort'] == 'timestamp':
        mtime = lambda f: os.stat(f).st_mtime
        files = sorted(files, key=mtime)
    else:
        print "Undefined logging type: ", config['sort']
        sys.exit(1)

    if test:
        print "Log files found are: "
        print files

    while len(files) > config['history']:
        target = files.pop(0)
        if test:
            print "Would remove file: ", target
        else:
            os.remove(target)


if __name__ == "__main__":

    print sys.argv

    if len(sys.argv) > 1:
        if sys.argv[1].lower() == 'test':
            print "Running in test mode"
            trim_log_files(test=True)
            sys.exit(0)

    trim_log_files()
    sys.exit(0)