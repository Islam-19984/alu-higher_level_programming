#!/usr/bin/python3
"""List inheritance"""


class MyList(list):
    """Class MyList inherits list."""

    def print_sorted(self):
        """Prints sorted list."""
        temp_list = self[:]
        temp_list.sort()
        print("{}".format(temp_list))

