from machine import SPI, Pin
import config

# Print SPI config
print(f'Onboard SPI: {SPI(1)}')

# Switch OFF Onboard LED
__led__ = Pin(config.LED_PIN, Pin.OUT)
__led__.value(0)
