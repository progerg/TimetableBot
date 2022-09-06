import datetime

from sqlalchemy import select, update

from db.base_db import BaseDBApi
from models import User, Timetable


day_to_name = {
    1: "Понедельник",
    2: "Вторник",
    3: "Среда",
    4: "Четверг",
    5: "Пятница",
    6: "Суббота",
    7: "Воскресенье"
}


class DBApi(BaseDBApi):
    """
    Основной класс для взаимодействия с базой. Наследует BaseDBApi
    """

    async def get_user_by_vk_id(self, vk_id: int) -> User | None:
        """
        Получение пользователя по vk_id

        :param vk_id: id человека в vk
        :return: User или None (если нет пользователя)
        """

        _ = await self._sess.execute(select(User).where(User.vk_id == vk_id))
        return _.scalars().first()

    async def reg_user(self, vk_id: int, first_name: str, last_name: str):
        """
        Регистрация пользователя сразу при входе

        :param vk_id: id человека в vk
        :param first_name: имя
        :param last_name: фамилия
        :return: None
        """

        self._sess.add(User(vk_id=vk_id, first_name=first_name, last_name=last_name))
        await self._sess.commit()

    async def add_course_group_subgroup(self, vk_id: int, course: int, group: int, subgroup: int):
        """
        Добавление курса, группы, подгруппы

        :param vk_id: vk_id: id человека в vk
        :param course: курс
        :param group: группа
        :param subgroup: подгруппа
        :return: None
        """

        await self._sess.execute(update(User).where(User.vk_id == vk_id).values(course=course,
                                                                                group=group, subgroup=subgroup))
        await self._sess.commit()

    async def get_user_today_timetable(self, vk_id: int) -> list[Timetable]:
        """
        Получение расписания на сегодня по vk_id

        :param vk_id:
        :return:
        """
        year, week_number, weekday = datetime.datetime.now().isocalendar()

        if week_number % 2 == 0:
            numerator = False
        else:
            numerator = True

        user = await self.get_user_by_vk_id(vk_id)
        timetable = (await self._sess.execute(select(Timetable).where(Timetable.group == user.group,
                                                                      Timetable.subgroup == user.subgroup,
                                                                      Timetable.course == user.course,
                                                                      Timetable.day == day_to_name[weekday],
                                                                      Timetable.numerator.in_([numerator, None])))).scalars().all()
        return timetable
