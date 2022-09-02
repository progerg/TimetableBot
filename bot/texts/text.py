import json

# Текста, которые отправляются пользователю
MESSAGES: dict[str, dict[str, str]] = json.load(open("texts/message.json"))

# Текст кнопок
BUTTONS: dict[str, dict[str, str]] = json.load(open("texts/button.json"))
