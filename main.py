# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os

import getapidata as apidata

import sys


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    path = "/home/andressilva/PycharmProjects/JsonCovidColombia/foldercases"
    apidata.getJsoncasesactive( sys.argv[1], sys.argv[2])

    apidata.mergefiles(path)
    apidata.cleanfiles(path)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
