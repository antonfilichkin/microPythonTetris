from st7735.ST7735 import TFT, TFTColor

BOX_SIZE = 8


class Figures:
    def __init__(self, tft: TFT):
        self.__tft__ = tft
        self.I_PIECE = Figure(self.__tft__, TFT.GREEN, (
            ((0, 0), (0, 1), (0, 2), (0, 3)),
            ((0, 0), (1, 0), (2, 0), (3, 0)))
        )
        self.O_PIECE = Figure(self.__tft__, TFT.YELLOW, (
            ((0, 0), (0, 1), (1, 0), (1, 1)), )
        )


class Figure:
    def __init__(self, tft: TFT, color: TFTColor, blocks: tuple):
        self.__tft__ = tft
        self.__color__ = color
        self.__current_state__ = 0
        self.__blocks__ = blocks

    def show(self, at_point):
        self.__draw__(at_point, self.__color__)

    def hide(self, at_point):
        self.__draw__(at_point, TFT.BLACK)

    def rotate(self, at_point):
        pass

    def drop(self, at_point):
        pass

    def __draw__(self, at_point, color: TFTColor):
        for block in self.__blocks__[self.__current_state__]:
            offset_x = block[0] * BOX_SIZE + block[0]
            offset_y = block[1] * BOX_SIZE + block[1]

            box = (offset_x + at_point[0], offset_y + at_point[1])
            self.__tft__.fillrect(box, (BOX_SIZE, BOX_SIZE), color)
