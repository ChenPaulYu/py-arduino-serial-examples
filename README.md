# Python-Arduino Communication via PySerial
This repository demonstrates how to set up and perform unidirectional and bidirectional communication between Python and Arduino using the PySerial library.

### Python Setup

1. Create a new Conda environment
```
conda create -n [env name] python=3.11.4
```

2. Install the required package:

```
pip install pyserial
```



### Important Notice
Do not open the Serial Monitor in the Arduino IDE if you want to receive data from Arduino to Python. Opening the Serial Monitor will occupy the serial port, blocking Python from accessing the data. Ensure that the port is free for communication with Python.