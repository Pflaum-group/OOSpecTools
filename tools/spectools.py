from typing import Tuple
import numpy as np
import seabreeze
seabreeze.use('pyseabreeze')
from seabreeze.spectrometers import Spectrometer


class TempSpec():
    def __init__(self, aq_time: int) -> None:
        self.spec = Spectrometer.from_first_available()
        self.spec.integration_time_micros(aq_time)
        self._wavelength = self.spec.wavelengths()
        self._dcflag = False

    def aquire_spectrum(self) -> np.ndarray:
        return self.spec.intensities(correct_dark_counts = self.dcflag)
    
    def set_aqtime(self, aqtime: int):
        self.spec.integration_time_micros(aqtime)
        print(f"aq_time set to {aqtime}")

    def close(self):
        self.spec.close()

    ### Properties
    
    @property
    def wavelength(self) -> np.ndarray:
        return self._wavelength
    
    @property
    def dcflag(self) -> bool:
        return self._dcflag
    
    @dcflag.setter
    def dcflag(self, flag: bool) -> None:
        self._dcflag = flag