import serial
import time


PORT1 = '/dev/cu.usbmodem111301'  
PORT2 = '/dev/cu.usbserial-11140'
BAUDRATE = 115200

ser1 = serial.Serial(PORT1, BAUDRATE)
ser2 = serial.Serial(PORT2, BAUDRATE)
time.sleep(2)

try:
    while True:
        user_input = input("Enter '1' or '2' to trigger the Arduino 1 or 2, or 'exit' to quit: ")

        if user_input == '1':  # Check if the user entered '1'
            ser1.write(b'1')  # Send trigger to Arduino
            print("Sent to Arduino 1.")

            time.sleep(1)  # Add delay to allow Arduino to process

            while ser1.in_waiting > 0:  # Check if there is data waiting
                line = ser1.readline().decode('utf-8').rstrip()  # Read a line and decode
                print("Received from Arduino:", line)
                
        elif user_input == '2':
            ser2.write(b'1')  # Send trigger to Arduino
            print("Sent to Arduino 2.")

            time.sleep(1)  # Add delay to allow Arduino to process

            while ser2.in_waiting > 0:  # Check if there is data waiting
                line = ser2.readline().decode('utf-8').rstrip()  # Read a line and decode
                print("Received from Arduino:", line)           

        elif user_input.lower() == 'exit':
            print("Exiting...")
            break

except KeyboardInterrupt:
    print("Program stopped.")
finally:
    ser1.close()
    ser2.close()



