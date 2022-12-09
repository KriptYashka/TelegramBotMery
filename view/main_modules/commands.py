import re
from brench_communicate import hello, weather, sub_mem, question

mery_cmd = {
    r"\bпривет|здра?ств|\bку\b": hello.send_hello,
    r"\bкак дела|что делаешь|\bчем занимаешься|как ты": hello.send_how_are_you,
    r"завтра погода|завтра температур|сколько завтра градус": weather.send_weather_yesterday,
    r"хочу подписаться": sub_mem.subscribe_user,
    r"добавить раздел вопрос": question.branch_add_section,
    r"показать раздел": question.branch_show_section,
    r"добавить вопрос": question.branch_add_question,
    # r"расскажи анекдот|шутку|прикол": hello.send_joke,
}