import board
import displayio
import adafruit_ssd1327
import busio
import time

displayio.release_displays()

# This pinout works on a Metro and may need to be altered for other boards.
spi = busio.SPI(board.SCL, board.SDA)
tft_cs = board.D6
tft_dc = board.D9
tft_reset = board.D5

display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=tft_reset, baudrate=1000000)
time.sleep(1)
display = adafruit_ssd1327.SSD1327(display_bus, width=128, height=128)
