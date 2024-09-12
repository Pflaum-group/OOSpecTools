from typing import Tuple
from argparse import ArgumentParser
import numpy as np
import pyqtgraph as pg
from pyqtgraph import QtWidgets, QtCore
from tools.spectools import TempSpec

def parse_args():
    parser = ArgumentParser()
    parser.add_argument(
        "--aq", type=int, default=10000, help="integration time in microseconds"
    )
    parser.add_argument(
        "--wavelength", type=str, default="200:1100", help="wavelength range as tring 'start:stop, eg. '200:1100' for 200 nm to 1100 nm"
    )

    args = parser.parse_args()
    return args

def parse_wavelength_range(wavelength_str):
    wl_str = wavelength_str.split(":")
    return [int(wl) for wl in wl_str]

def run():
    args = parse_args()

    ### make pyqtWidget
    win = pg.GraphicsLayoutWidget(show=True, title="Basic plotting examples")
    win.resize(1000,600)
    win.setWindowTitle('pyqtgraph example: Plotting')
    
    ### Define plot Layout
    p1 = win.addPlot()
    p1.setLabel('left', 'intensity', units='cts')
    p1.setLabel('bottom', 'wavelength', units='nm')
    p1.setXRange(parse_wavelength_range(args.wavelength)[0],parse_wavelength_range(args.wavelength)[1])
    p1.enableAutoRange('x', False)
    curve = p1.plot(pen="r")
    
    ### Connect to Spectrometer
    spec = TempSpec(args.aq)


    def update():
        _int = spec.aquire_spectrum()
        curve.setData(y=_int, x=spec.wavelength)
    
    t = QtCore.QTimer()
    t.timeout.connect(
        update
        )
    t.start(int(args.aq/1000)) #100 ms longer than AQ time to avoid timing issues
    pg.exec()





if __name__ == "__main__":
    run()
