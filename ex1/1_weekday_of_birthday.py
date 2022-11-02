
# exercice 1 
# please see the README.md file

from datetime import datetime 
from datetime import date

def get_weekday_of_birthday(number_years, birthday):
    WEEKDAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    try:
        number_years = int(number_years)
    except TypeError as error_msg:
        print(error_msg)
        return
    else:
        new_year = date.today().year + number_years 
        sb = birthday.split('-')
        new_birthday = datetime(new_year, int(sb[1]), int(sb[2]))
        idx_wd = new_birthday.weekday()
        weekday = WEEKDAYS[idx_wd]
    return weekday
    
if __name__ == "__main__":
    number_years = input('Number of years: ')
    birthday = input('Your birthday (YYYY-MM-DD): ')
    weekday = get_weekday_of_birthday(number_years, birthday)
    print('After', number_years, 'years, your birthday will be on', weekday)