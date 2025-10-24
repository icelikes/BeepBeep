import gc9a01
from machine import Pin, SPI
import config
import NotoSansMono_32 as noto_mono

class RoundLcdScreen:
    lcd = None

    spi = SPI(1, baudrate=60000000, sck=Pin(10), mosi=Pin(11))
    rotation = config.ROUND_LCD_ROTATION
    options = 0
    buffer_size = 0

    def __init__(self):

        self.lcd = gc9a01.GC9A01(
            self.spi,
            240,
            240,
            reset=Pin(12, Pin.OUT),
            cs=Pin(9, Pin.OUT),
            dc=Pin(8, Pin.OUT),
            backlight=Pin(40, Pin.OUT),
            rotation=self.rotation,
            options=self.options,
            buffer_size= self.buffer_size)
        self.lcd.init()
        self.lcd.fill(0)
        self.lcd.circle(119, 119, 119, gc9a01.color565(255, 255, 255))



    def two_line_message(self, line1, line2):
        self.lcd.write(noto_mono, line1, 119-self.lcd.write_len(noto_mono, line1)//2, 90)
        self.lcd.write(noto_mono, line2, 119-self.lcd.write_len(noto_mono, line2)//2, 130)

    def connecting_wifi(self):
        self.two_line_message("Connecting", "Wifi")

    def connecting_websocket(self):
        self.two_line_message("Connecting to", "server")

    def ready(self):
        self.two_line_message("Scan to", "activate")

    def interlock_active(self):
        self.two_line_message("Interlock", "active")

    def interlock_timeout(self):
        self.two_line_message("Use or", "lock in:")
        

    def access_success(self):
        self.lcd.fill(gc9a01.color565(50, 168, 56))
        self.lcd.circle(119, 119, 119, gc9a01.color565(50, 168, 56))
        self.two_line_message("Access", "Granted")

    def access_fail(self):
        self.two_line_message("Access", "Denied")

    def interlock_success(self):
        self.two_line_message("Interlock", "active")

    def vend_success(self):
        self.two_line_message("Vending", "Success")
    
    def vend_fail(self):
        self.two_line_message("Vending", "Failed")

    def clear(self):
        self.lcd.fill(0)
        self.lcd.circle(119, 119, 119, gc9a01.color565(255, 255, 255))