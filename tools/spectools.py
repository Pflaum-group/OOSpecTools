from typing import Tuple

import seabreeze
seabreeze.use('pyseabreeze')
from seabreeze.spectrometers import Spectrometer


class TempSpec():
    def __init__(self, aq_time) -> None:
        self.spec = Spectrometer.from_first_available()
        self.spec.integration_time_micros(aq_time)
        self.wavelength = self.spec.wavelengths()

    def aquire_spectrum(self):
        return self.spec.intensities()
