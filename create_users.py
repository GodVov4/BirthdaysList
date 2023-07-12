from faker import Faker


f = Faker(['uk_UA'])
users = []


def create_users():
    while len(users) < 10:
        d = {f.first_name(): f.future_date(14)}
        users.append(d)


create_users()
