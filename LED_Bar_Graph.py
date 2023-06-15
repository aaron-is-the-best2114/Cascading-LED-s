import RPi.GPIO as GPIO
import time

SER_PIN = 17
SRCLK_PIN = 27
RCLK_PIN = 22
OE_PIN = 23

levels = [0b0000000000,
          0b0000000001,
          0b0000000011,
          0b0000000111,
          0b0000001111,
          0b0000011111,
          0b0000111111,
          0b0001111111,
          0b0011111111,
          0b0111111111,
          0b1111111111]

GPIO.setmode(GPIO.BCM)
GPIO.setup(SER_PIN, GPIO.OUT)
GPIO.setup(SRCLK_PIN, GPIO.OUT)
GPIO.setup(RCLK_PIN, GPIO.OUT)
GPIO.setup(OE_PIN, GPIO.OUT)

def shift_out(byte):
    for _ in range(8):
        print("Shift_out")
        GPIO.output(SER_PIN, byte & 0x80)
        byte <<=1
        GPIO.output(SRCLK_PIN, GPIO.HIGH)
        GPIO.output(SRCLK_PIN, GPIO.LOW)
        
def latch_data():
    print("latch_data")
    GPIO.output(RCLK_PIN, GPIO.HIGH)
    GPIO.output(RCLK_PIN, GPIO.LOW)
    
def enable_output(enable):
    print("enable_output")
    GPIO.output(OE_PIN, not enable)
    
try:
    while True:
        for level in levels:
            shift_out(level)
            latch_data()
            enable_output(True)
            time.sleep(0.5)
            enable_output(False)
            
except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()