#!/usr/bin/python3

for cpt in range(0, 10):
    for cpt2 in range(cpt + 1, 10):
        if cpt == 8:
            print("{}{}".format(cpt, cpt2))
        else:
            print("{}{}".format(cpt, cpt2), end=", ")
