#!/usr/bin/python3
for i in range(0, 100):
    if i == 99:
        print("{0}".format(i))
    print(f"{i:02}", end=", ")