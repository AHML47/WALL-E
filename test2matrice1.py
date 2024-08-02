from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from time import sleep

# Define the SPI interface and the number of cascaded MAX7219 devices
serial = spi(port=0, device=0, gpio=noop())
device1 = max7219(serial, cascaded=1, block_orientation=-90)
device2 = max7219(serial, cascaded=1, block_orientation=-90)

def initialize(devices):
    for device in devices:
        with canvas(device) as draw:
            for i in range(8):
                for j in range(8):
                    draw.point((i, j), fill="black")

def blink_pattern(devices, time):
    for _ in range(5):
        with canvas(devices) as draw:
            for device in devices:
                for i in range(8):
                    for j in range(8):
                        draw.point((i, j), fill="white")
        sleep(time)
        initialize(devices)
        sleep(time)

if __name__ == "__main__":
    initialize([device1, device2])
    try:
        while True:
            blink_pattern([device1, device2], 0.5)
    except KeyboardInterrupt:
        pass
