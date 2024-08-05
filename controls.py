from machine import Pin
import asyncio

import config

DEBOUNCE_MS = 20

BUTTONS = {
    "up": Pin(config.BUTTON_UP, Pin.IN, Pin.PULL_UP),
    "down": Pin(config.BUTTON_DOWN, Pin.IN, Pin.PULL_UP),
    "left": Pin(config.BUTTON_LEFT, Pin.IN, Pin.PULL_UP),
    "right": Pin(config.BUTTON_RIGHT, Pin.IN, Pin.PULL_UP)
}


class Buttons:
    def __init__(self):
        loop = asyncio.get_event_loop()
        for name, button in BUTTONS.items():
            setattr(self, name, 0)
            loop.create_task(self.__read_button__(name, button))

    async def __read_button__(self, name: str, button: Pin):
        while True:
            # print(f'Button: {name} - {button.value()}')
            current = button.value()
            active = 0
            while active < DEBOUNCE_MS:
                if current == button.value():
                    active += 1
                else:
                    active = 0
                    asyncio.sleep_ms(1)
            if active == DEBOUNCE_MS:
                setattr(self, name, not button.value())
                # self.name = button.value()
            await asyncio.sleep_ms(50)
