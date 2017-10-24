from machine import Pin


import time

for bank in 'ABCDEFGHI':
    print(bank, (ord(bank) - 65)*32 )



pins =  [  Pin('PA10','w') , Pin('PA20','w')  ]

print(pins)

pins[0].value(0)
pins[1].value(1)

for x in range(0,5):

    for pin in pins:
        pin.write( not pin.value() )
    time.sleep(.5)
else:
    for pin in pins:
        pin.write(False)








