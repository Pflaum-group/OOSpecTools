from typing import Tuple

import numpy as np
import pyqtgraph as pg
from PyQt5.QtCore import pyqtSlot, QTimer
from PyQt5.QtGui import QKeySequence
from PyQt5 import QtWidgets
from pyqtgraph import QtWidgets, QtCore
from tools.spectools import TempSpec

class LiveView(QtWidgets.QMainWindow):
    def __init__(self, aqtime: int, wavelength: Tuple, savepath: str, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._aqtime = aqtime
        self._wavelength = wavelength
        self._savepath = savepath
        
        ### Build UI
        self.window = pg.GraphicsLayoutWidget(show=True)
        self.window.resize(1000,600)
        self.window.setWindowTitle('OOSpecTools liveview')

        # Define plot Layout
        self.p1 = self.window.addPlot()
        self.p1.setLabel('left', 'intensity', units='cts')
        self.p1.setLabel('bottom', 'wavelength', units='nm')
        self.p1.setXRange(self.wavelength[0],self.wavelength[1])
        self.p1.enableAutoRange('x', False)
        self.curve = self.p1.plot(pen="r")

        self.setCentralWidget(self.window)
        self.show()
        # add shortcut rules

        
        ### Connect and start spectrometer
        self.spectrometer = TempSpec(self.aqtime)

        self.updateTimer = QTimer()
        self.updateTimer.timeout.connect(self.update)
        self.updateTimer.start(int(self.aqtime/1000))


    ### Class slots
    @pyqtSlot()
    def update(self):
        _int = self.spectrometer.aquire_spectrum()
        self.curve.setData(y=_int, x=self.spectrometer.wavelength)


    ### Attributes
    @property
    def aqtime(self) -> int:
        return self._aqtime
    
    @aqtime.setter
    def aqtime(self, aqtime: int) -> None:
        self._aqtime = aqtime

    @property
    def wavelength(self) -> Tuple:
        return self._wavelength

    @wavelength.setter
    def wavelength(self, wavelength: Tuple) -> None:
        self._wavelength = wavelength
    
    @property
    def savepath(self) -> str:
        return self._savepath

    @savepath.setter
    def savepath(self, savepath: str) -> None:
        self._savepath = savepath

