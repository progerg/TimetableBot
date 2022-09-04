from vkbottle import Keyboard, Text, KeyboardButtonColor
from texts import BUTTONS


def main_menu_buttons():
    keyboard = Keyboard(inline=False)
    keyboard.add(Text(BUTTONS['main']['1']))
    keyboard.add(Text(BUTTONS['main']['2']))
    return keyboard
