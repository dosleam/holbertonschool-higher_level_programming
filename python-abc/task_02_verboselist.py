#!/usr/bin/python3

"""
Contain the class
"""


class VerboseList(list):

    """
    Contain the inherit class
    """

    def append(self, item):
        """
        append method
        """

        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """
        extend method
        """

        super().extend(iterable)
        print("Extended the list with [{}] items.".format(len(iterable)))

    def remove(self, item):
        """
        remove item
        """

        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """
        pop method
        """

        item = super().pop(index)
        print("Popped [{}] from the list.".format(item))
        return item
