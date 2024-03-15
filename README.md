# Read input from the camera

The camera model we use is FLIR Grasshopper 2. We will use [rotpy](https://github.com/matham/rotpy) library to read the raw image from the camera then passing it to opencv for further processing.


## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install rotpy for reading the input.
```bash
pip install rotpy
```
**OR**
```bash
python -m pip install rotpy
```
Others common library:
```bash
pip install numpy opencv-python
```