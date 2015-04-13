#!/usr/bin/env python

import yaml
import os
import sys
import re


def trim_log_files():

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

    while len(files) > config['history']:
        target = files.pop(0)
        os.remove(target)


if __name__ == "__main__":

    trim_log_files()