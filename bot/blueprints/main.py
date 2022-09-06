from vkbottle.bot import Blueprint, Message, rules

from texts import MESSAGES, BUTTONS
from states import Registration, Main

from db import DBApi


class UserInfoRule(rules.ABCRule[Message]):
    async def check(self, message: Message) -> dict:
        user = (await bp.api.users.get(message.from_id))[0]
        return {"user": user}


bp = Blueprint("for menu")
bp.labeler.vbml_ignore_case = True


@bp.on.message(text=BUTTONS['main']['1'])
async def get_today_timetable(message: Message):
    async with DBApi() as db:
        timetables = await db.get_user_today_timetable(message.from_id)
        msg = MESSAGES['main']['2']
        for n, timetable in enumerate(timetables, start=1):
            msg = MESSAGES['main']['3'].format(n, timetable.subject, timetable.start, timetable.end,
                                               timetable.subject.lecturer)
            if timetable.cabinet != "-":
                msg += MESSAGES['main']['4'].format(timetable.cabinet)
            else:
                msg += MESSAGES['main']['5']
            msg += "\n\n"

        await message.answer(msg)

