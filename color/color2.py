#!/usr/bin/env python3
"""Alta3 Research || Author RZFeeser@alta3.com
Learning how to use functions"""

## Installs the crayons package.
## python3 -m pip install crayons
## import statements ALWAYS go up top
import crayons

MYCOLORS = ['red', 'green', 'yellow', 'blue', 'black', 'magenta', 'cyan', 'white']


def main():
    """Runtime code. Always indent a function"""

    for x in MYCOLORS:
        newcolor = crayons.{x}
        print(newcolor(x + ' string'))

# we must call our main function or our code will not run!
main()

