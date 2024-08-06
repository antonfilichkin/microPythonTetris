from st7735.ST7735 import TFT, TFTColor

BOX_SIZE = 8


class Figures:
    def __init__(self, tft: TFT):
        self.__tft__ = tft
        self.I_PIECE = Figure(
            self.__tft__,
            TFT.GREEN,
            (((0, 0), (0, 1), (0, 2), (0, 3)), ((0, 0), (1, 0), (2, 0), (3, 0))),
            x=20, y=20
        )
        self.O_PIECE = Figure(
            self.__tft__,
            TFT.YELLOW,
            (((0, 0), (0, 1), (1, 0), (1, 1)), ),
            x=20, y=20
        )


class Figure:
    def __init__(self, tft: TFT, color: TFTColor, blocks, rotation=0, x=20, y=20):
        self.__tft__ = tft
        self.__blocks__ = blocks
        self.color = color
        self.rotation = rotation
        self.x = x
        self.y = y

    def show(self):
        self.__draw__(self.x, self.y, self.color)

    def hide(self):
        self.__draw__(self.x, self.y, TFT.BLACK)

    def fall(self):
        self.hide()
        self.y += 1
        self.show()

    def right(self):
        self.hide()
        self.x += BOX_SIZE + 1
        self.show()

    def left(self):
        self.hide()
        self.x -= BOX_SIZE - 1
        self.show()

    def rotate(self):
        self.hide()
        self.rotation = 0 if self.rotation + 1 > len(self.__blocks__) - 1 else self.rotation + 1
        self.show()

    def drop(self):
        pass

    def __draw__(self, x, y, color: TFTColor):
        for block in self.__blocks__[self.rotation]:
            offset_x = block[0] * BOX_SIZE + block[0]
            offset_y = block[1] * BOX_SIZE + block[1]

            box = (x + offset_x, y + offset_y)
            self.__tft__.fillrect(box, (BOX_SIZE, BOX_SIZE), color)
