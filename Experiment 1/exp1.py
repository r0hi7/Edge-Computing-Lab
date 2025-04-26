import RPi.GPIO as GPIO
import time

# Use BCM pin numbering
GPIO.setmode(GPIO.BCM)

# Set up the GPIO pin (for example, GPIO 18) as an output
LED_PIN = 18
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        # Turn the LED on
        GPIO.output(LED_PIN, GPIO.HIGH)
        print("LED is ON")
        time.sleep(1)  # Wait for 1 second

        # Turn the LED off
        GPIO.output(LED_PIN, GPIO.LOW)
        print("LED is OFF")
        time.sleep(1)  # Wait for 1 second

except KeyboardInterrupt:
    # Clean up GPIO settings before exiting
    GPIO.cleanup()
    print("\nProgram stopped and GPIO cleaned up.")
