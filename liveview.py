import sys
from os import getcwd
from typing import Tuple
from argparse import ArgumentParser
import numpy as np
import pyqtgraph as pg
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QKeySequence
from PyQt5 import QtWidgets
from pyqtgraph import QtWidgets, QtCore
from tools.spectools import TempSpec
from tools.liveview_ui import LiveView

def parse_args():
    parser = ArgumentParser()
    parser.add_argument(
        "--aq", type=int, default=10000, help="integration time in microseconds"
    )
    parser.add_argument(
        "--wavelength", type=str, default="200:1100", help="wavelength range as tring 'start:stop, eg. '200:1100' for 200 nm to 1100 nm"
    )
    parser.add_argument(
        "--savepath", type=str, default=getcwd(), help="savepath for spectra"
    )

    args = parser.parse_args()
    return args

def parse_wavelength_range(wavelength_str):
    wl_str = wavelength_str.split(":")
    return [int(wl) for wl in wl_str]

if __name__ == "__main__":
    args = parse_args()
    app = QtWidgets.QApplication(sys.argv)
    win = LiveView(args.aq, parse_wavelength_range(args.wavelength), args.savepath)
    sys.exit(app.exec_())
