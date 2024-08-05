from st7735.ST7735 import TFT

CUBE_SIZE = 8
FIELD_SIZE = (10, 20)


class Graphics:
    def __init__(self, tft: TFT):
        self.__tft__ = tft

    def draw_background(self):
        self.__tft__.fillrect((0, 0), (128, 160), TFT.RED)
        self.clear_field()

    def clear_field(self):
        field_width = CUBE_SIZE * FIELD_SIZE[0] + FIELD_SIZE[0]
        self.__tft__.fillrect((4, 4), (field_width, 152), TFT.BLACK)

    # DEV TEMP
    def test_vertical(self):
        start_x = 4
        lines = 9

        for _ in range(1, lines + 1):
            self.__tft__.vline((_ * CUBE_SIZE + start_x + 1 + _ - 1, start_x), 152, TFT.GREEN)

    def test_horizontal(self):
        start_y = 4
        lines = 16

        for _ in range(1, lines + 1):
            self.__tft__.hline((start_y, _ * CUBE_SIZE + start_y + 1 + _ -1), 100, TFT.BLUE)