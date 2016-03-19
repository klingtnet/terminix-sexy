#!/usr/bin/env python3

import os
import sys
import json


BASEPATH = 'terminal.sexy/dist/schemes'
OUTPATH = 'out'


def main():
    index_fp = os.path.join(BASEPATH, 'index.json')
    if not os.path.isfile(index_fp):
        print("""could not find color scheme index under: {}
Did you clone the repo with the `--recursive` flag?""".format(index_fp))
        sys.exit(1)
    if not os.path.isdir(OUTPATH):
        try:
            os.mkdir(OUTPATH, mode=0o755)
        except OSError as err:
            print("""could not create output path: {}
error: {}""".format(OUTPATH, err))
            sys.exit(1)
    with open(index_fp) as idx_f:
        rel_paths = json.load(idx_f)
        for path in [os.path.join(BASEPATH, p + '.json') for p in rel_paths]:
            convert(path)


def convert(path):
    try:
        with open(path) as src_f:
            source = json.load(src_f)
            dest = {'name': source['name'],
                    'comment': "Author: {}".format(source['author']),
                    'use-theme-colors': False,
                    'foreground-color': source['foreground'],
                    'background-color': source['background'],
                    'palette': source['color']
                    }
            write(dest)
    except IOError as err:
        print("""could not open source scheme: {}
error: {}""".format(path, err))


def write(scheme):
    try:
        dst_fp = os.path.join(OUTPATH, scheme['name'] + '.json')
        with open(dst_fp, 'w') as dst_f:
            json.dump(scheme, dst_f, indent=4, sort_keys=True)
    except IOError as err:
        print("""could not write output color scheme: {}
error: {}""".format(dst_fp, err))


if __name__ == '__main__':
    main()
