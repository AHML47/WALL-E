import RPi.GPIO as GPIO
import time

# Set GPIO mode
GPIO.setmode(GPIO.BOARD)

# Define GPIO pins
TRIG = 11
ECHO = 13
LED = 7

# Setup GPIO pins
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

# Function to measure distance
def measure_distance():
    # Set trigger to HIGH
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    # Wait for the echo to go HIGH
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    # Wait for the echo to go LOW
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    # Calculate pulse duration
    pulse_duration = pulse_end - pulse_start

    # Calculate distance (speed of sound: 343m/s)
    distance = pulse_duration * 17150

    # Round distance to 2 decimal places
    distance = round(distance, 2)

    return distance

try:
    while True:
        distance = measure_distance()
        print("Distance:", distance, "cm")

        # If distance is less than or equal to 3cm, turn on LED
        if distance <= 3:
            GPIO.output(LED, GPIO.HIGH)
        else:
            GPIO.output(LED, GPIO.LOW)

        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
