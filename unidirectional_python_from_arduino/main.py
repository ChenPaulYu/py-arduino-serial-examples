import serial
import time


PORT     = '/dev/cu.usbmodem111301'  
BAUDRATE = 115200

ser = serial.Serial(PORT, BAUDRATE)
ser.setDTR(False)
ser.setRTS(False)
time.sleep(2)  # Wait for the connection to be established

try:
    while True:
        if ser.in_waiting > 0:  # Check if there is data waiting
            line = ser.readline().decode('utf-8').rstrip()  # Read a line and decode
            print("Received from Arduino:", line)

except KeyboardInterrupt:
    print("Program stopped.")
finally:
    ser.close()  # Close the serial connection when done







