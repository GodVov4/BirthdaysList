from collections import defaultdict
from datetime import date, datetime, timedelta


def get_birthdays_per_week(users: list) -> dict:
    print(users)
    # Реалізуйте тут домашнє завдання
    if not users:
        return {}
    today = date.today()
    next_week = today + timedelta(7)
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    users_dict = defaultdict(list)
    for user in users:
        if user['birthday'] < today:
            user['birthday'] = user['birthday'].replace(year=date.today().year+1)
        if today <= user['birthday'] <= next_week:
            if user['birthday'].strftime('%A') in weekdays:
                users_dict[user['birthday'].strftime('%A')].append(user['name'])
            else:
                users_dict[weekdays[0]].append(user['name'])
    return users_dict


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
        {"name": "Jan Kou", "birthday": datetime(1976, 1, 2).date()},
        {"name": "Jan Ko", "birthday": datetime(1976, 1, 3).date()},
        {"name": "Jan K", "birthday": datetime(1976, 1, 4).date()},
        {"name": "Jan", "birthday": datetime(1976, 1, 5).date()},
        {"name": "Ja", "birthday": datetime(1976, 1, 6).date()},
        {"name": "J", "birthday": datetime(1976, 1, 7).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
