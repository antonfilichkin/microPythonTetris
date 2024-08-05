from machine import SPI, Pin
import asyncio
import time

from st7735.ST7735 import TFT
from st7735.sysfont import sysfont

import config
from game_menu import Menu

# Init TFT
spi = SPI(1, baudrate=20000000, polarity=0, phase=0, sck=Pin(config.SPI_SCK), mosi=Pin(config.SPI_SDA))
tft = TFT(spi, config.TFT_A0, config.TFT_RESET, config.TFT_CS)
tft.initr()
tft.rgb(True)
tft.rotation(2)
tft.fill(TFT.BLACK)

# Constants
CUBE_SIZE = 8
FIELD_SIZE = (10, 20)

menu = Menu(tft)
button_up = Pin(config.BUTTON_UP, Pin.IN, Pin.PULL_UP)
button_down = Pin(config.BUTTON_DOWN, Pin.IN, Pin.PULL_UP)
button_left = Pin(config.BUTTON_LEFT, Pin.IN, Pin.PULL_UP)
button_right = Pin(config.BUTTON_RIGHT, Pin.IN, Pin.PULL_UP)


# INTERFACE
def draw_interface():
    tft.fillrect((0, 0), (128, 160), TFT.RED)
    clear_field()


def clear_field():
    field_width = CUBE_SIZE * FIELD_SIZE[0] + FIELD_SIZE[0]
    tft.fillrect((4, 4), (field_width, 152), TFT.BLACK)


def test_vertical():
    start_x = 4
    lines = 9

    for _ in range(1, lines + 1):
        tft.vline((_ * CUBE_SIZE + start_x + 1 + _ - 1, start_x), 152, TFT.GREEN)


def test_horizontal():
    start_y = 4
    lines = 16

    for _ in range(1, lines + 1):
        tft.hline((start_y, _ * CUBE_SIZE + start_y + 1 + _ -1), 100, TFT.BLUE)

# async def main_handler():
#     draw_field()
#     await asyncio.sleep_ms(200000)
#     # await tft.fill(TFT.BLACK)
#
# loop = asyncio.get_event_loop()
# loop.set_exception_handler(common.exception_handler)
# loop.create_task(main_handler())
# loop.run_forever()

draw_interface()
clear_field()

test_vertical()
test_horizontal()


menu.draw_menu()
while True:
    time.sleep(0.5)
    print(f'Buttons: U-{button_up.value()}, D-{button_down.value()}, L-{button_left.value()}, R-{button_right.value()}')
    # menu.next()

