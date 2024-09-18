# OOSpecTools
Tools for OceanOptics spectrometers. It has been tested with the OceanOptics Maya2000Pro, but should in theory work with any other OceanOptics spectrometer supported by ```python-seabreeze```. 

## Dependencies
This package uses [```python-seabreeze```](https://github.com/ap--/python-seabreeze) to communicate with the devices. Before using this package make sure you have downloaded and installed seabreeze properly following there installation guide. 

Installing the package does **NOT** install this dependency to not mess with the OS specific setup of seabreeze. 

## Usage

### Installation
Install with pip as 
```bash
$ pip install git+https://github.com/Pflaum-group/OOSpecTools
```
or download from here and install locally with
```bash
$ pip install -e path/to/parent_folder/OOSpecTools
```

### LiveView
This module opens a simple live view showing the current spectrum recorded by the spectrometer. There are several [arguments](#specifying-arguments) and [hotkeys](#hotkeys) that can be used. 

#### General Remarks
Start liveview via withing the package folder
```bash
$ python3 -m liveview
```
If you want to run it from everywhere you need to add the package folder to your python path
```bash
$ export PYTHONPATH="path/to/some/parent/directory/of/package"
```
Then you can start the liveview with
```bash
$ python3 -m OOSpecTools.liveview
```
from anywhere in you system.

#### Specifying Arguments
When starting the live view some parameters can be specified, the integration time of the spectrometer, the shown wavelength range and the save path for recorded spectra. The possible arguments are: 


| command | description | default |
|:-------:|-------------|-------- |
| --help    |  show this table| |
| --aq | integration time in microseconds | 10000 µs |
|--wavelength | wavelength range as string 'start:stop', eg.      '200:1100' for 200 nm to 1100 nm | 200:1100 |
|--savepath | save path for spectra | cwd | 

For example, using a 100 ms integration time and showing a wavelength range of 950 nm to 1050 nm would beed the following addition to the regular starting command
```bash
$ python3 -m OOSpecTools.liveview --aq 100000 --wavelength '950:1050'
```
#### Hotkeys
The following hotkeys can be used:

|Key|description|
|:-:|-----------|
|S|saves current spectrum as numpy.ndarray to directory specified in save path. The full spectrum is saved, not only the range specified by --wavelength|
|d|use internal dark count correction of the spectrometer
|+|increase aquisition time by 10 ms
|-|decrease aquisition time by 10 ms (minimum is 10 ms)


