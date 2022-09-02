from vkbottle.bot import Blueprint, Message, rules
from vkbottle_types.codegen.objects import UsersUserFull
from vkbottle_types.objects import MessagesConversation


class ChatInfoRule(rules.ABCRule[Message]):
    async def check(self, message: Message) -> dict:
        chats_info = await bp.api.messages.get_conversations_by_id(message.peer_id)
        user = (await bp.api.users.get(message.from_id))[0]
        return {"chat": chats_info.items[0],
                "user": user}


bp = Blueprint("for chat commands")
bp.labeler.vbml_ignore_case = True
bp.labeler.auto_rules = [rules.PeerRule(from_chat=True), ChatInfoRule()]


@bp.on.message(command="самобан")
async def kick(message: Message, chat: MessagesConversation):
    await bp.api.messages.remove_chat_user(message.chat_id, message.from_id)
    await message.answer(f"Участник самоустранился из {chat.chat_settings.title} по собственному желанию")


@bp.on.message(text="где я")
async def where_am_i(message: Message, chat: MessagesConversation):
    await message.answer(f"Вы в <<{chat.chat_settings.title}>>")