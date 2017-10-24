# micropython-machine-linux

*NB: requires mpycompat dist-packages and its modifications to os module*

**just started nothing much done yet**

GPIO : can blink on orange pi, will probably add lpt-gpio for pc later.

LED: untested

PWM: untested

SPI: untested

I2C: untested

MMIO: untested

Serial: untested


.



## Linux Peripheral I/O (GPIO, LED, PWM, SPI, I2C, MMIO, Serial) with Python 2 & 3

micropython-machine-linux is a pure Python recreation of the MicroPython machine module based on python-periphery. It provides modules for GPIO, LED, PWM, SPI, I2C and Serial peripheral I/O interface access in userspace Linux. It is useful in embedded Linux environments (including Raspberry Pi, BeagleBone, etc. platforms) for interfacing with external peripherals.

## Installation

With setup.py:
``` text
git clone https://github.com/turbinenreiter/micropython-machine-linux
cd micropython-machine-linux
python setup.py install
```

## Examples

### GPIO

``` python
from periphery import GPIO

# Open GPIO 10 with input direction
gpio_in = GPIO(10, "in")
# Open GPIO 12 with output direction
gpio_out = GPIO(12, "out")

value = gpio_in.read()
gpio_out.write(value)

gpio_in.close()
gpio_out.close()
```

### LED

``` python
from periphery import LED

# Open LED "led0" with initial state off
led0 = LED("led0", False)
# Open LED "led1" with initial state on
led1 = LED("led1", True)

value = led0.read()
led1.write(value)

# Set custom brightness level
led1.write(led1.max_brightness / 2)

led0.close()
led1.close()
```

### PWM

``` python
from periphery import PWM

# Open PWM channel 0, pin 10
pwm = PWM(0, 10)

# Set frequency to 1 kHz
pwm.frequency = 1e3
# Set duty cycle to 75%
pwm.duty_cycle = 0.75

pwm.enable()

# Change duty cycle to 50%
pwm.duty_cycle = 0.50

pwm.close()
```

### SPI

``` python
from periphery import SPI

# Open spidev1.0 with mode 0 and max speed 1MHz
spi = SPI("/dev/spidev1.0", 0, 1000000)

data_out = [0xaa, 0xbb, 0xcc, 0xdd]
data_in = spi.transfer(data_out)

print("shifted out [0x%02x, 0x%02x, 0x%02x, 0x%02x]" % tuple(data_out))
print("shifted in  [0x%02x, 0x%02x, 0x%02x, 0x%02x]" % tuple(data_in))

spi.close()
```

### I2C

``` python
from periphery import I2C

# Open i2c-0 controller
i2c = I2C("/dev/i2c-0")

# Read byte at address 0x100 of EEPROM at 0x50
msgs = [I2C.Message([0x01, 0x00]), I2C.Message([0x00], read=True)]
i2c.transfer(0x50, msgs)
print("0x100: 0x%02x" % msgs[1].data[0])

i2c.close()
```

### Serial

``` python
from periphery import Serial

# Open /dev/ttyUSB0 with baudrate 115200, and defaults of 8N1, no flow control
serial = Serial("/dev/ttyUSB0", 115200)

serial.write(b"Hello World!")

# Read up to 128 bytes with 500ms timeout
buf = serial.read(128, 0.5)
print("read %d bytes: _%s_" % (len(buf), buf))

serial.close()
```

## Documentation

To build documentation locally with Sphinx, run:

```
cd docs
make html
```

Sphinx will produce the HTML documentation in `docs/_build/html/`.

Run `make help` to see other output targets (LaTeX, man, text, etc.).

## Testing

The tests located in the [tests](tests/) folder may be run under Python to test the correctness and functionality of micropython-machine-linux. Some tests require interactive probing (e.g. with an oscilloscope), the installation of a physical loopback, or the existence of a particular device on a bus. See the usage of each test for more details on the required setup.

## License

micropython-machine-linux is MIT licensed. See the included [LICENSE](LICENSE) file.

