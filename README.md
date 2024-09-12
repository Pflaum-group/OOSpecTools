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
Start liveview via
```bash
$ python3 -m OOSpecTools.liveview
```
