import re

date_regex = re.compile(r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(1000|1[0-9]{3}|200[0-9]|201[0-9]|202[0-9]|203[0-9]|204[0-9]|205[0-9]|206[0-9]|207[0-9]|208[0-9]|209[0-9]|2[12][0-9]{2})$')

def validate_date(date_str):
    match = date_regex.match(date_str)
    if match:
        day, month, year = map(int, match.groups())
        if month in [4, 6, 9, 11] and day > 30:
            return False
        elif month == 2:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                return day <= 29
            else:
                return day <= 28
        elif day > 31:
            return False
        else:
            return True
    else:
        return False

# Example usage:
date_str = "31/02/2020"
if validate_date(date_str):
    print(f"{date_str} is a valid date.")
else:
    print(f"{date_str} is not a valid date.")
