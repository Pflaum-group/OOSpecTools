from typing import Tuple
from os import path
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
        self._AQTIME_INCREMENT = 10000
        self._wavelength = wavelength
        self._savepath = savepath
        self._savecounter = 0
        self._dcflag = False
        
        ### Build UI
        self.window = pg.GraphicsLayoutWidget(show=True)
        self.window.resize(1000,600)
        self.window.setWindowTitle('OOSpecTools liveview')

        # Define plot Layout
        self.p1 = self.window.addPlot()
        self.p1.setLabel('left', 'intensity [a.u.]')
        self.p1.setLabel('bottom', 'wavelength [nm]')
        self.p1.setXRange(self.wavelength[0],self.wavelength[1])
        self.p1.enableAutoRange('x', False)
        self.curve = self.p1.plot(pen="r")

        self.setCentralWidget(self.window)
        self.show()
        
        # add shortcut rules
        self.shortcut_add_save_spectrum = QtWidgets.QShortcut(QKeySequence("s"), self)
        self.shortcut_add_save_spectrum.activated.connect(self.save_spectrum)

        self.shortcut_add_dark_correction = QtWidgets.QShortcut(QKeySequence("d"), self)
        self.shortcut_add_dark_correction.activated.connect(self.darkcorrection)
        
        self.shortcut_add_increase_aqtime = QtWidgets.QShortcut(QKeySequence("+"), self)
        self.shortcut_add_increase_aqtime.activated.connect(self.increase_aqtime)

        self.shortcut_add_decrease_aqtime = QtWidgets.QShortcut(QKeySequence("-"), self)
        self.shortcut_add_decrease_aqtime.activated.connect(self.decrease_aqtime)

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
        self.p1.setYRange(0.95*_int[:2068].min(),1.05*_int[:2068].max())

    @pyqtSlot()
    def save_spectrum(self):
        np.save(path.join(self.savepath,f"spectrum_{self._savecounter:03d}.npy"), 
                np.vstack((self.spectrometer.wavelength, self.spectrometer.aquire_spectrum())))
        self._savecounter += 1
    
    def increase_aqtime(self):
        self.aqtime = self.aqtime + self._AQTIME_INCREMENT
        self.updateTimer.stop()
        self.spectrometer.set_aqtime(self.aqtime)
        self.updateTimer.start(int(self.aqtime/1000))
    
    def decrease_aqtime(self):
        newaqtime = self.aqtime - self._AQTIME_INCREMENT
        if newaqtime >= 10000:
            self.aqtime = newaqtime
            self.updateTimer.stop()
            self.spectrometer.set_aqtime(self.aqtime)
            self.updateTimer.start(int(self.aqtime/1000))
    
    def darkcorrection(self):
        if not self._dcflag:
            self._dcflag = True
            self.spectrometer.dcflag = self._dcflag
        else:
            self._dcflag = False
            self.spectrometer.dcflag = self._dcflag
        


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

