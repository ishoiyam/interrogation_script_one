#!/usr/bin/env python3

from greeting import greetings
from getInfo import get_information
from printCard import print_card
from saveData import Save_Data


def main():
    greetings()
    fname, lname, email, address, origin = get_information()
    print_card(fname, lname, email, address, origin)    
    Save_Data(fname, lname, email, address, origin)

if __name__ == "__main__":
    main()