from vkbottle.bot import Blueprint, Message, rules

from texts import MESSAGES
from states import Registration, Main

from db import DBApi


# class UserInfoRule(rules.ABCRule[Message]):
#     async def check(self, message: Message) -> dict:
#         user = (await bp.api.users.get(message.from_id))[0]
#         return {"user": user}


bp = Blueprint("for registration")
bp.labeler.vbml_ignore_case = True


@bp.on.message(text="ФКН топ")
async def registration(message: Message):
    vk_user = (await bp.api.users.get(message.from_id))[0]
    await message.answer(MESSAGES['start']['1'].format(vk_user.first_name))
    async with DBApi() as db:
        user = await db.get_user_by_vk_id(message.from_id)
        if not user:
            await message.answer(MESSAGES['start']['3'])
            await db.reg_user(message.from_id, vk_user.first_name, vk_user.last_name)
            await bp.state_dispenser.set(message.peer_id, state=Registration.COURSE_STATE)
        elif not user.course or not user.group or not user.subgroup:
            await message.answer(MESSAGES['start']['3'])
            await bp.state_dispenser.set(message.peer_id, state=Registration.COURSE_STATE)
        else:
            pass


@bp.on.message(state=Registration.COURSE_STATE)
async def registration_course(message: Message):
    if message.text.isdecimal() and 1 <= int(message.text) <= 4:
        await message.answer(MESSAGES['start']['4'])
        await bp.state_dispenser.set(message.peer_id, Registration.GROUP_STATE, course=int(message.text))
    else:
        await message.answer(MESSAGES['start']['6'])


@bp.on.message(state=Registration.GROUP_STATE)
async def registration_group(message: Message):
    if message.text.isdecimal() and 1 <= int(message.text) <= 16:
        await message.answer(MESSAGES['start']['5'])
        await bp.state_dispenser.set(message.peer_id, Registration.SUBGROUP_STATE, group=int(message.text))
    else:
        await message.answer(MESSAGES['start']['7'])


@bp.on.message(state=Registration.SUBGROUP_STATE)
async def registration_subgroup(message: Message):
    if message.text.isdecimal() and 1 <= int(message.text) <= 2:
        state = (await bp.state_dispenser.get(message.peer_id)).payload
        await DBApi().add_course_group_subgroup(message.from_id, state.get("course"), state.get("group"),
                                                int(message.text))
        await message.answer(MESSAGES['start']['9'])
        await bp.state_dispenser.delete(message.peer_id)
        await bp.state_dispenser.set(message.peer_id, state=Main.MENU_STATE)
    else:
        await message.answer(MESSAGES['start']['8'])
