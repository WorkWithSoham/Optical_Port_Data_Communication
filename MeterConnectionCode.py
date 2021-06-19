import serial 
import time

def knocking(rounds=5):
    '''
        Best results were obtained with 5 ":" knocks before the handshake request
    '''
    for _ in range(rounds):
        time.sleep(0.5) # Time delay in seconds before the next bit is written on the port
        ser.write(':'.encode('raw_unicode_escape'))

def string_write_read_on_port(list_of_strings: list) -> str:
    '''
        Send request string to the Port and return the response from the meter
    '''
    print(ser)
    string = ''.join(list_of_strings)
    ser.write(string.encode('raw_unicode_escape'))
    output = ser.readline()
    return output

def char_write_read_on_port(list_of_strings: list) -> str:
    '''
        Send request chars to the Port and return the response from the meter
    '''
    print(ser)
    for char in list_of_strings:
        print(char, '--->', char.encode('raw_unicode_escape'))
        ser.write(char.encode('raw_unicode_escape'))
    output = ser.readline()
    return output

if __name__ == '__main__':
    # Create Serial Object with the attributes of the COM3 port
    ser = serial.Serial(
        port='COM3',
        baudrate=9600,
        bytesize=8,
        timeout=1,
        stopbits=serial.STOPBITS_ONE,
        parity=serial.PARITY_NONE,
    )

    request = ['/', '?', '!', '\r', '\n'] # string = '/?!\r\n'
    acknowledgement = ['\x06', '0', '5', '0', '\r', '\n'] # string = '\x06050\r\n'

    knocking()
    output1 = char_write_read_on_port(request)
    print('Request Res: ', output1)

    print()

    # knocking()
    output2 = char_write_read_on_port(acknowledgement)
    print('Acknowledgement Res: ', output2)

    print()

    ser.close()
