__version__ = "1.1.0"
"Module version string."

version = (1,1,0)
"Module version tuple."
import sys

import mpycompat

if 0:
    try:
        import time
    except ImportError:
        import utime as time
        builtins.time =time

#        import uos as os
#        sys.modules['os']=os

        #builtins.IOError = OSError



def sleep(seconds):
    """Sleep for the specified number of seconds.

    Args:
        seconds (int, long, float): duration in seconds.

    """
    time.sleep(seconds)

def sleep_ms(milliseconds):
    """Sleep for the specified number of milliseconds.

    Args:
        milliseconds (int, long, float): duration in milliseconds.

    """
    time.sleep(milliseconds / 1000.0)

def sleep_us(microseconds):
    """Sleep for the specified number of microseconds.

    Args:
        microseconds (int, long, float): duration in microseconds.

    """
    time.sleep(microseconds / 1000000.0)

from machine.gpio import GPIO, GPIOError
try:
    from machine.led import LED, LEDError
except ImportError as e:
    print("machine.led could not import :", e, file=sys.stderr)
try:
    from machine.pwm import PWM, PWMError
except ImportError as e:
    print("machine.pwm could not import :", e, file=sys.stderr)

try:
    from machine.spi import SPI
except ImportError as e:
    print("machine.spi could not import :", e, file=sys.stderr)

if UPY:
    print("machine.i2c could not import :", file=sys.stderr)
    I2C = None
else:
    from machine.i2c import I2C, I2CError


try:
    from machine.mmio import MMIO, MMIOError
except ImportError as e:
    print("machine.mmio could not import :", e, file=sys.stderr)

from machine.serial import Serial, SerialError


def SUNXI_GPIO(pbanknum):
    pbanknum = pbanknum.upper()
    bank = ( ord(pbanknum[1]) -65 ) * 32
    pin = int(pbanknum[2:])
    print(pbanknum,bank,pin)
    return bank + pin



class Pin(GPIO):
    IN = 'r'
    OUT = 'w'
    PULL_UP = 'h'
    PULL_DOWN = None

    def __init__(self,pbanknum, mode=None, pull=None):
        self.name = pbanknum
        self.gpio = SUNXI_GPIO(self.name)
        pull = pull or ''
        mode = mode or ''

        self.pull = pull.lower()
        self.mode = mode.lower()
        if self.pull or self.mode:
            self.init(self.mode, self.pull)


    def init(self,mode='',pull='l',**kw):
        if 'w' in mode:
            direction = 'out'
        elif 'r' in mode:
            direction = 'in'
            if pull:
                if 'h' in pull:
                    direction = 'high'
                elif 'l' in pull:
                    direction = 'low'
        else:
            direction = 'preserve'
        GPIO.__init__(self, self.gpio, direction)

        self.value( kw.pop('value',False) )


    def value(self,v=None):
        if v is None:
            return self.read()
        self.write( (v and True) or False)

    def off(self):
        self.write(False)

    def on(self):
        self.write(True)

    def __repr__(self):
        return "(%s)%s"%(self.gpio, self.name)


