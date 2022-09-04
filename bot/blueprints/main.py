from vkbottle.bot import Blueprint, Message, rules

from texts import MESSAGES
from states import Registration, Main

from db import DBApi


class UserInfoRule(rules.ABCRule[Message]):
    async def check(self, message: Message) -> dict:
        user = (await bp.api.users.get(message.from_id))[0]
        return {"user": user}


bp = Blueprint("for menu")
bp.labeler.vbml_ignore_case = True

