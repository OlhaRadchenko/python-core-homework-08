from datetime import date, timedelta

def get_birthdays_per_week(users):
    birthdays_per_week = {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': []}

    today = date.today()

    start_of_week = today - timedelta(days=today.weekday())

    for user in users:
        name = user['name']
        birthday = user['birthday']

        if birthday.replace(year=today.year) < today:
            birthday = birthday.replace(year=today.year + 1)

        day_of_week = birthday.strftime('%A')

        birthdays_per_week[day_of_week].append(name)

    for i in range(today.weekday()):
        day = (start_of_week + timedelta(days=i)).strftime('%A')
        birthdays_per_week[day] += birthdays_per_week[day_of_week]
        birthdays_per_week[day_of_week] = []

    return birthdays_per_week

if __name__ == "__main__":
    users = [{'name': 'Bill', 'birthday': date(1990, 11, 5)},
             {'name': 'Jan', 'birthday': date(1992, 11, 7)},
             {'name': 'Kim', 'birthday': date(1995, 11, 9)}]

    result = get_birthdays_per_week(users)

    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
