import datetime
from datetime import timedelta
# import create_users
# users = create_users

#             ^^^^^^^^^^^
# You can use this import for create users (need install requirements)

# or use this users
users = [
    {'Василь': datetime.date(2023, 7, 16)}, {'Данило': datetime.date(2023, 7, 22)},
    {'Варвара': datetime.date(2023, 7, 21)}, {'Златослава': datetime.date(2023, 8, 5)},
    {'Ліза': datetime.date(2023, 7, 26)}, {'Любов': datetime.date(2023, 8, 8)},
    {'Едита': datetime.date(2023, 7, 13)}, {'Віктор': datetime.date(2023, 8, 11)},
    {'Данна': datetime.date(2023, 8, 2)}, {'Олександр': datetime.date(2023, 7, 16)}
]


def get_birthdays_per_week(users):
    current_date = datetime.date.today()
    next_week = current_date + timedelta(7)
    weekend = ['Saturday', 'Sunday']
    while current_date < next_week:
        names = []
        for user in users:
            for name, birthday in user.items():
                if current_date == birthday:
                    names.append(name)
        if names:
            print(f"{'Monday' if current_date.strftime('%A') in weekend else current_date.strftime('%A')}: "
                  f"{', '.join(names)}")
        current_date += timedelta(1)


get_birthdays_per_week(users)
