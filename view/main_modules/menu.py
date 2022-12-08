import telebot


def get_default_menu():
    """Выдает меню для пользователя."""
    menu = telebot.types.ReplyKeyboardMarkup()

    params = ["Как дела, Мэри?", 'Какая завтра погода?', 'Добавить раздел вопросов']

    for item in params:
        if isinstance(item, list):
            menu.add(*item)
        else:
            menu.add(item)
    return menu


def button_menu(params):
    """Шаблон всех меню"""
    menu = telebot.types.ReplyKeyboardMarkup()
    if len(params) > 3:
        for i in range(1, len(params), 2):
            menu.add(params[i - 1], params[i])
        if len(params) % 2:
            menu.add(params[-1])
    else:
        for item in params:
            if isinstance(item, list):
                menu.add(*item)
            else:
                menu.add(item)
    return menu