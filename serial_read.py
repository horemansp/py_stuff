
import time
import serial

ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate = 115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
    )



def telegram():
    for teller in range(23):
        telegram_line=str(ser.readline())
        stop_str = telegram_line.rfind("(")
        telegram_code = telegram_line[6:stop_str]
        #print(telegram_code)
        print(telegram_line)
        if (telegram_code == "1.7.0"):
            #vind de startpositie van de ( in de text
            #print(telegram_line, end=' ')
            start_str = telegram_line.rfind("(")+1
            stop_str = telegram_line.rfind("*")
            telegram_value = telegram_line[start_str:stop_str]
            print("value="+ telegram_value, end=' ')
            start_str = telegram_line.rfind("*")+1
            stop_str = telegram_line.rfind(")")
            telegram_metric = telegram_line[start_str:stop_str]
            print(" Metric=" + telegram_metric)
        
while 1:
    telegram()