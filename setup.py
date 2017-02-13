try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='micropython-machine-linux',
    version='1.1.0',
    description='A pure Python recreation of the MicroPython machine module based on python-periphery.',
    author='Sebastian Plamauer',
    author_email='oeplse@gmail.com',
    url='https://github.com/turbinenreiter/micropython-machine-linux',
    packages=['machine'],
    long_description="""micropython-machine-linux is a pure Python recreation of the MicroPython machine module based on python-periphery. It provides modules for GPIO, LED, PWM, SPI, I2C and Serial peripheral I/O interface access in userspace Linux. It is useful in embedded Linux environments (including Raspberry Pi, BeagleBone, etc. platforms) for interfacing with external peripherals.""",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: MicroPython',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Embedded Systems',
        'Topic :: System :: Hardware',
        'Topic :: System :: Hardware :: Hardware Drivers',
    ],
    license='MIT',
    keywords='gpio spi led pwm i2c serial uart embedded linux beaglebone raspberrypi rpi odroid',
)
