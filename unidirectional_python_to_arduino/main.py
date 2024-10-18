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
        user_input = input("Enter '1' to trigger the Arduino or 'exit' to quit: ")

        if user_input == '1':  # Check if the user entered '1'
            ser.write(b'1')  # Send trigger to Arduino

        elif user_input.lower() == 'exit':
            print("Exiting...")
            break

except KeyboardInterrupt:
    print("Program stopped.")
finally:
    ser.close()  # Close the serial connection when done



