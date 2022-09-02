from vkbottle import BaseStateGroup


class Registration(BaseStateGroup):
    """
    State-ы для ветки регистрации
    """

    COURSE_STATE = "course"
    GROUP_STATE = "group"
    SUBGROUP_STATE = "subgroup"


class Main(BaseStateGroup):
    """
    State-ы для основного меню
    """

    MENU_STATE = "main_menu_state"
