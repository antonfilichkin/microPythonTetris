from machine import SPI, PWM, Pin
import asyncio
import time

from st7735.ST7735 import TFT
from st7735.sysfont import sysfont

import config
from menu import Menu
from controls import Buttons
from graphics import Graphics

from tetris import Figures

# Menus
MAIN_MENU = ("NEW GAME", "OPTIONS", "ABOUT")
OPTIONS_MENU = ("Bcklght+", "Bcklght-")


# Init TFT
spi = SPI(1, baudrate=20000000, polarity=0, phase=0, sck=Pin(config.SPI_SCK), mosi=Pin(config.SPI_SDA))
tft = TFT(spi, config.TFT_A0, config.TFT_RESET, config.TFT_CS)
tft.initr()
tft.rgb(True)
tft.rotation(2)
tft.fill(TFT.BLACK)

brightness = PWM(Pin(config.TFT_PWM))
brightness.freq(500)
brightness.duty(511)

buttons = Buttons()
graphics = Graphics(tft)

# Menus
main_menu = Menu(tft, MAIN_MENU)
options_menu = Menu(tft, OPTIONS_MENU)


async def with_main_menu():
    await asyncio.sleep(0.5)
    print('Main menu')
    main_menu.draw_menu()
    while main_menu.is_shown:
        if buttons.down:
            main_menu.next()
        if buttons.up:
            main_menu.prev()
        if buttons.right:
            selected = main_menu.selected()
            main_menu.close()
            if selected == 'NEW GAME':
                await run_game()
            elif selected == 'OPTIONS':
                await with_options_menu()
            else:
                await with_main_menu()
        await asyncio.sleep(0.05)


async def with_options_menu():
    await asyncio.sleep(0.5)
    print('Options menu')
    options_menu.draw_menu()
    while options_menu.is_shown:
        if buttons.down:
            options_menu.next()
        if buttons.up:
            options_menu.prev()
        if buttons.right:
            selected = options_menu.selected()
            if selected == 'Bcklght+':
                brightness.duty(min(1023, brightness.duty() + 5))
            elif selected == 'Bcklght-':
                brightness.duty(max(0, brightness.duty() - 5))
            print(f'Brightness: {brightness.duty()}')
        if buttons.left:
            options_menu.close()
            await with_main_menu()
        await asyncio.sleep(0.05)


async def run_game():
    figures = Figures(tft)
    graphics.draw_background()
    graphics.clear_field()

    figures.O_PIECE.show((40, 40))
    await drop_figure()

    # graphics.test_vertical()
    # graphics.test_horizontal()


async def drop_figure():
    figures = Figures(tft)
    start_y_old = 20
    start_y_new = 20
    while True:
        figures.I_PIECE.hide((20, start_y_old))
        figures.I_PIECE.show((20, start_y_new))
        await asyncio.sleep(0.5)
        start_y_old = start_y_new
        start_y_new += 5


async def main_task():
    await with_main_menu()

loop = asyncio.get_event_loop()
loop.create_task(main_task())
loop.run_forever()

# loop = asyncio.get_event_loop()
# loop.run_until_complete(main_task())
# loop.close()
