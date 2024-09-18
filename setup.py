from setuptools import setup, find_packages

setup(name='OOSpecTools',
      version='0.0.2',
      description='Tools for OceanOptics spectrometers',
      long_description=open('README.md').read(),
      long_description_content_type ='text/markdown',
      license= 'MIT',
      author='Sebastian Hammer',
      author_email='sebastian.hammer@mail.mcgill.ca',
      url='https://github.com/Pflaum-group/OOSpecTools',
      packages= find_packages(),
      install_requires=['numpy', 'pyqtgraph'],
      python_requires='>=3.10',
     )