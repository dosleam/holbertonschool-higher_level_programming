#!/usr/bin/python3

def uppercase(str):
    for c in str:
        if 97 <= ord(c) <= 122:
            # Convert lowercase to uppercase by subtracting 32
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print()  # Print newline at the end
