from st7735.ST7735 import TFT
from st7735.sysfont import sysfont

MENU_ITEM_START_X = 14
MENU_ITEM_START_Y = 30
MENU_ITEM_DISTANCE = 2
MENU_ITEM_WIDTH = 100
MENU_ITEM_HEIGHT = 25

LETTER_WIDTH = 11
FONT_SIZE = 2


class Menu:
    def __init__(self, tft: TFT, menu_items: tuple):
        self.__tft__ = tft
        self.__menu_items__ = menu_items
        self.__selected__ = 0
        self.is_shown = False

    def draw_menu(self):
        self.is_shown = True
        self.__selected__ = 0
        self.__tft__.fillrect((0, 0), (128, 160), TFT.BLACK)
        self.__draw_menu_item__(0, True)

        for _ in range(1, len(self.__menu_items__)):
            self.__draw_menu_item__(_, False)

    def __draw_menu_item__(self, pos: int, selected: bool):
        menu_item_y = MENU_ITEM_START_Y + MENU_ITEM_HEIGHT * pos + MENU_ITEM_DISTANCE * pos
        color = TFT.GREEN if selected else TFT.BLUE
        self.__tft__.fillrect((MENU_ITEM_START_X, menu_item_y), (MENU_ITEM_WIDTH, MENU_ITEM_HEIGHT), color)

        text = self.__menu_items__[pos]
        menu_item_text_y = (MENU_ITEM_WIDTH - len(text) * LETTER_WIDTH) / 2
        self.__tft__.text((MENU_ITEM_START_X + menu_item_text_y, menu_item_y + 4), text, TFT.WHITE, sysfont, FONT_SIZE)

    def next(self):
        self.__draw_menu_item__(self.__selected__, False)
        self.__selected__ = 0 if self.__selected__ + 1 == len(self.__menu_items__) else self.__selected__ + 1
        self.__draw_menu_item__(self.__selected__, True)

    def prev(self):
        self.__draw_menu_item__(self.__selected__, False)
        self.__selected__ = len(self.__menu_items__) - 1 if self.__selected__ - 1 < 0 else self.__selected__ - 1
        self.__draw_menu_item__(self.__selected__, True)

    def selected(self):
        return self.__menu_items__[self.__selected__]

    def close(self):
        self.is_shown = False
        self.__selected__ = 0
        self.__tft__.fillrect((0, 0), (128, 160), TFT.BLACK)
