import time

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008


def brightness(num):
    if values[i] < 256:
        print("Bright")
    elif values[i] < 512:
        print("Normal")
    elif values[i] < 768:
        print("Dim")
    elif values[i] < 1024:
        print("Dark")


def convert_int2f(num):
    c = (input * 3.3 * 1000.0 / 1023 - 500) / 10
    f = 9.0 / 5.0 * c + 32
    return f


print('Reading MCP3008 values, press Ctrl-C to quit...')
# Print nice channel column headers.
print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*range(8)))
print('-' * 57)
# Main program loop.
while True:
    # Read all the ADC channel values in a list.
    values = [0]*8
    for i in range(8):
        # The read_adc function will get the value of the specified channel (0-7).
        values[i] = mcp.read_adc(i)
    # Print the ADC values.
    print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} | brightness(i) | convert_int2f(i) |'
          .format(*values))
    # Pause for half a second.
    time.sleep(0.5)






