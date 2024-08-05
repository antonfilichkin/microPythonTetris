from machine import SPI, Pin
import asyncio
import time

from st7735.ST7735 import TFT
from st7735.sysfont import sysfont

import config
from game_menu import Menu
from controls import Buttons
from graphics import Graphics

# Init TFT
spi = SPI(1, baudrate=20000000, polarity=0, phase=0, sck=Pin(config.SPI_SCK), mosi=Pin(config.SPI_SDA))
tft = TFT(spi, config.TFT_A0, config.TFT_RESET, config.TFT_CS)
tft.initr()
tft.rgb(True)
tft.rotation(2)
tft.fill(TFT.BLACK)


buttons = Buttons()
menu = Menu(tft)
graphics = Graphics(tft)

graphics.draw_background()
graphics.clear_field()

graphics.test_vertical()
graphics.test_horizontal()


async def main_task():
    menu.draw_menu()
    while menu.is_shown:
        print(f'{buttons.up}, {buttons.down}')
        # menu.next()
        if buttons.down:
            menu.next()
        if buttons.up:
            menu.prev()
        await asyncio.sleep_ms(100)
        # if buttons.get()["up"]:
        #     menu.prev()
        # if buttons.get()["down"]:
        #     menu.next()
        # await asyncio.sleep(1)

loop = asyncio.get_event_loop()
loop.create_task(main_task())
loop.run_forever()

# loop = asyncio.get_event_loop()
# loop.run_until_complete(main_task())
# loop.close()
