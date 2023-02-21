#!/usr/bin/python3
import sys

argv = sys.argv
argc = len(argv)

if argc == 1:
    print("{:d} argument{}.".format(argc-1, '' if argc-1 == 1 else 's'))
else:
    print("{:d} argument{}:".format(argc-1, '' if argc-1 == 1 else 's'))
    for i in range(1, argc):
        print("{:d}: {}".format(i, argv[i]))

