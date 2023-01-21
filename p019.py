month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month_names = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December',
]
weekday_names = [
    'Sunday',
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
]

def is_leap_year(year: int) -> bool:
    """Returns True if the specified year is a leap year, False otherwise"""
    return ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)

if __name__ == '__main__':
    weekday = 1  # January 1st 1900 was a Monday

    count = 0
    for year in range(1900, 2000 + 1):
        for month in range(12):
            # print('{} 1st {} was a {}'.format(month_names[month], year, weekday_names[weekday]))
            weekday = (weekday + month_days[month] + (month == 1 and is_leap_year(year))) % 7
            if weekday == 0 and year > 1900:
                count += 1
                # print("First Sunday on {} 1st {}".format(month_names[(month + 1) % 12], year))

    print("There were {} 'first Sundays' between Jan 1st 1901 and Dec 31st 2000".format(count))
