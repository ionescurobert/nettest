# ----------------------------------------------#
# NetTest tool information
# Author: Robert Ionescu
# Date: 15.02.2018
# Tool version:
__version__ = "0.1"
# ----------------------------------------------#
# -----------Pingtest todos--------------------#
# Todo implement jitter calculator for pingtest
# Todo Get a plausible pingtest
# Todo Get a data evaluation and output
# -----------Speedtest todos--------------------#
# -----------Netstat todos----------------------#


import logging
import msvcrt
import sys
import os

from components.msgs import msgs
from components.pingtest import pingtest

# Logging configuration
logfile = "nettest.log"

try:
    if os.path.isfile(logfile):
        os.remove(logfile)
    else:
        print("Creating log file...")
except OSError:
    print("ERROR")

logging.basicConfig(filename='nettest.log', level=logging.DEBUG, format='%(asctime)s                  %(message)s',
                    datefmt='[%d.%m.%Y]-[%H:%M:%S]')


def initialize():
    os.system('cls')
    msgs.intro()
    print("   ---------------------------------")
    print("   NetTest version               " + __version__)
    print("   ---------------------------------")
    print("      Console Symbol Information")
    print("   ---------------------------------")
    print("   [+]    Default log symbol")
    print("   [#]    WARN. Tool will continue")
    print("   [!]    ERROR. Execution will stop")
    print("   [-]    Other messages")
    print("   ---------------------------------")
    print("   ---------------------------------")
    print("\n            Possible Keys")
    print("   ---------------------------------")
    print("   KEY    |        DESCRIPTION")
    print("   ---------------------------------")
    print("   [S]    |        Speedtest")
    print("   [P]    |        Pingtest")
    print("   [ESC]  |        EXIT")
    print("   ---------------------------------")
    print("   Press a key to continue...\n\n")

    while 1:
        k = msvcrt.getch()
        if k.decode('ASCII') == chr(27):
            print("[+] User canceled!")
            logging.info("User canceled!")
            sys.exit(1)
        if k.decode('ASCII') == chr(112):
            print("[+] Ping test started")
            logging.info("Ping test started")
            return pingtest.pingtest()
        if k.decode('ASCII') == chr(115):
            logging.info("Speedtest started")
            print("[+] Speedtest started")


def main():
    initialize()
    print("Tool has finished work!")


if __name__ == '__main__':
    main()
