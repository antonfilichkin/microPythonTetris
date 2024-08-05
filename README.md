# microPythonTetris
#### Practicing mPython with esp32 and ST7735S


### Install ESP Tool and Setup MicroPython
https://docs.micropython.org/en/latest/esp32/tutorial/intro.html]


### Create virtual env: 
> python -m venv venv

> .\venv\Scripts\activate


### Check HW SPI
Connect to REPL and run
> import machine

> print(machine.SPI(1))
 
### ST7735 lib
https://github.com/boochow/MicroPython-ST7735

### ST7735 fonts
https://github.com/GuyCarver/MicroPython
