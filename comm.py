import serial

puerto = serial.Serial("/dev/tty.usbmodem14131")
while(True):
    datos = str(serial.Serial.readline(puerto))
    print(datos)

