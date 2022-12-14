from datetime import datetime
import pytz

from bot.database.methods.select import is_user_notfication_enabled, get_user_group


def decode_callback_data(callback):
    return int(callback.data.split('_')[1])


def get_poweroff_schedule_text(user_id, selected_weekday):
    poweroff_schedule = [[[0, 1, 2, 0, 1, 2], [1, 2, 0, 1, 2, 0], [2, 0, 1, 2, 0, 1], [0, 1, 2, 0, 1, 2], [1, 2, 0, 1, 2, 0], [2, 0, 1, 2, 0, 1], [0, 1, 2, 0, 1, 2]],
                        [[1, 2, 0, 1, 2, 0], [2, 0, 1, 2, 0, 1], [0, 1, 2, 0, 1, 2], [1, 2, 0, 1, 2, 0], [2, 0, 1, 2, 0, 1], [0, 1, 2, 0, 1, 2], [1, 2, 0, 1, 2, 0]],
                        [[2, 0, 1, 2, 0, 1], [0, 1, 2, 0, 1, 2], [1, 2, 0, 1, 2, 0], [2, 0, 1, 2, 0, 1], [0, 1, 2, 0, 1, 2], [1, 2, 0, 1, 2, 0], [2, 0, 1, 2, 0, 1]]]
    poweroff_schedule_time = ['1:00-5:00', '5:00-9:00', '9:00-13:00', '13:00-17:00', '17:00-21:00', '21:00-1:00']
    name_of_weekday = ['Понеділок', 'Вівторок', 'Середа', 'Четвер', "П'ятниця", 'Субота', 'Неділя']

    weekday_name = name_of_weekday[selected_weekday]
    user_group = get_user_group(user_id) - 1
    poweroff_schedule_text = ''
    for i in range(6):
        poweroff_schedule_text += '\n'
        poweroff_schedule_text += f'*{poweroff_schedule_time[i]}*'
        if poweroff_schedule[user_group][selected_weekday][i] == 0:
            poweroff_schedule_text += ' - Електроенергія ❌'
        elif poweroff_schedule[user_group][selected_weekday][i] == 1:
            poweroff_schedule_text += ' - Електроенергія ✅'
        else:
            poweroff_schedule_text += ' - Електроенергія ⚠️'
    poweroff_schedule_text = f'Ваша група - {user_group + 1}\nВибрано: {weekday_name}\n' + poweroff_schedule_text
    if not is_user_notfication_enabled(user_id):
        return poweroff_schedule_text
    return f'Сьогодні: {name_of_weekday[get_weekday()]}, {poweroff_schedule_text}'


def get_weekday():
    dt = datetime.now(pytz.timezone('Europe/Kiev'))
    return dt.weekday()

def get_state_in_emoji(state):
    state_in_emoji = ["☑️", "✅"]
    return state_in_emoji[state]