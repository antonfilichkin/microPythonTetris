from st7735.ST7735 import TFT
from st7735.sysfont import sysfont

NEW_GAME = "NEW GAME"
OPTIONS = "OPTIONS"
ABOUT = "ABOUT"

MENU_ITEMS = (NEW_GAME, OPTIONS, ABOUT)
MENU_ITEM_START_X = 10
MENU_ITEM_START_Y = 30
MENU_ITEM_DISTANCE = 2
MENU_ITEM_WIDTH = 100
MENU_ITEM_HEIGHT = 25

LETTER_WIDTH = 11
FONT_SIZE = 2


class Menu:
    def __init__(self, tft: TFT):
        self.__tft__ = tft
        self.__selected__ = 0

    def draw_menu(self):
        self.__selected__ = 0
        self.__draw_menu_item__(0, True)

        for _ in range(1, len(MENU_ITEMS)):
            self.__draw_menu_item__(_, False)

    def __draw_menu_item__(self, pos: int, selected: bool):
        menu_item_y = MENU_ITEM_START_Y + MENU_ITEM_HEIGHT * pos + MENU_ITEM_DISTANCE * pos
        color = TFT.GREEN if selected else TFT.BLUE
        self.__tft__.fillrect((MENU_ITEM_START_X, menu_item_y), (MENU_ITEM_WIDTH, MENU_ITEM_HEIGHT), color)

        text = MENU_ITEMS[pos]
        menu_item_text_y = (MENU_ITEM_WIDTH - len(text) * LETTER_WIDTH) / 2
        self.__tft__.text((MENU_ITEM_START_X + menu_item_text_y, menu_item_y + 4), text, TFT.WHITE, sysfont, FONT_SIZE)

    def next(self):
        self.__draw_menu_item__(self.__selected__, False)
        self.__selected__ = 0 if self.__selected__ + 1 == len(MENU_ITEMS) else self.__selected__ + 1
        self.__draw_menu_item__(self.__selected__, True)

    def prev(self):
        self.__draw_menu_item__(self.__selected__, False)
        self.__selected__ = len(MENU_ITEMS) - 1 if self.__selected__ - 1 == 0 else self.__selected__ - 1
        self.__draw_menu_item__(self.__selected__, True)

    def selected(self):
        return MENU_ITEMS[self.__selected__]
