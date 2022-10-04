import serial

arduino_data = serial.Serial('com3', 115200)


def set_screen(cmd):
    cmd = cmd + '\r'
    arduino_data.write(cmd.encode())


def set(cmd, l):
    for i in range(0, l):
        set_screen(cmd)

