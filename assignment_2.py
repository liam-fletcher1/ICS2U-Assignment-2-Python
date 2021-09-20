#!/usr/bin/env python3

# Created by: Liam Fletcher
# Created on: Sep 2021
# This program calculates the area of a triangle

import math


def main():
    # this function calculates the area of a triangle

    # input
    Base = int(input("Enter the base of the triangle (cm): "))
    Height = int(input("Enter the height of the triangle (cm): "))

    # process
    area = 0.5 * Base * Height

    # output
    print("")
    print("Area is {0} cm².".format(area))
    print("")
    print("Done.")
    

if __name__ == "__main__":
    main()
