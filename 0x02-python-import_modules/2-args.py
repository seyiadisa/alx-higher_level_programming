#!/usr/bin/python3
import sys

plural = "argument" if len(sys.argv) == 2 else "arguments"
colon_or_period = ":" if len(sys.argv) > 1 else "."

if __name__ == "__main__":
    print("{0} {1}{2}"
          .format(len(sys.argv) - 1, plural, colon_or_period))

    for i in range(1, len(sys.argv)):
        print("{0}: {1}".format(i, sys.argv[i]))
