from datetime import datetime
import pytz

from bot.database.methods.select import is_user_notfication_enabled, get_user_group


def decode_callback_data(callback):
    return callback.data.split('_')[1]


def get_poweroff_schedule_text(user_id):
    poweroff_schedule = [[[0, 1, 2, 0, 1, 2], [1, 2, 0, 1, 2, 0], [2, 0, 1, 2, 0, 1], [0, 1, 2, 0, 1, 2], [1, 2, 0, 1, 2, 0], [2, 0, 1, 2, 0, 1], [0, 1, 2, 0, 1, 2]],
                        [[1, 2, 0, 1, 2, 0], [2, 0, 1, 2, 0, 1], [0, 1, 2, 0, 1, 2], [1, 2, 0, 1, 2, 0], [2, 0, 1, 2, 0, 1], [0, 1, 2, 0, 1, 2], [1, 2, 0, 1, 2, 0]],
                        [[2, 0, 1, 2, 0, 1], [0, 1, 2, 0, 1, 2], [1, 2, 0, 1, 2, 0], [2, 0, 1, 2, 0, 1], [0, 1, 2, 0, 1, 2], [1, 2, 0, 1, 2, 0], [2, 0, 1, 2, 0, 1]]]
    poweroff_schedule_time = ['1:00-5:00', '5:00-9:00', '9:00-13:00', '13:00-17:00', '17:00-21:00', '21:00-1:00']
    name_of_week_day = ['Понеділок', 'Вівторок', 'Середа', 'Четвер', "П'ятниця", 'Субота', 'Неділя']

    day_of_week = get_day_of_week()
    day_name = name_of_week_day[day_of_week]
    user_group = get_user_group(user_id) - 1
    poweroff_schedule_text = ''
    for i in range(6):
        poweroff_schedule_text += '\n'
        poweroff_schedule_text += f'*{poweroff_schedule_time[i]}*'
        if poweroff_schedule[user_group][day_of_week][i] == 0:
            poweroff_schedule_text += ' - Відключення електроенергії ❌'
        elif poweroff_schedule[user_group][day_of_week][i] == 1:
            poweroff_schedule_text += ' - Електроенергія подається ✅'
        else:
            poweroff_schedule_text += ' - Можливе відключення ⚠️'
    poweroff_schedule_text = f'Ваша група - {user_group + 1}\nВибрано: {day_name}\n' + poweroff_schedule_text
    if not is_user_notfication_enabled(user_id):
        return poweroff_schedule_text
    return f'Сьогодні: {day_name}, {poweroff_schedule_text}'


def get_day_of_week():
    dt = datetime.now(pytz.timezone('Europe/Kiev'))
    return dt.weekday();