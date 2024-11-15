import datetime

DAYS = ["Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"]
MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]
MONTH_DAYS = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
CAL_WIDTH = 20


class Calendar:
    def __init__(self, year: int) -> None:
        self.year = year
        self.is_leap_year = self.__is_leap_year()
    
    def __is_leap_year(self):
        y = self.year
        if y % 4 == 0 and y % 100 != 0:
            return True
        if y % 400 == 0:
            return True
        return False

    def print(self):
        pass


class Month:
    def __init__(self, month_num: int, year: int):
        self.number = month_num
        self.month_index = month_num - 1
        self.year = year
        self.days = MONTH_DAYS[self.month_index]
        start_date = f"{month_num}-01-{year}"
        self._starting_day_index = (
            datetime.datetime.strptime(start_date, "%m-%d-%Y").weekday() + 1
        ) % 7

    def get_weeks(self):
        weeks = []
        day_index = self._starting_day_index
        week = [" "] * day_index
        for day in range(1, self.days + 1):
            if day < 10:
                week.append(f" {day}")
            else:
                week.append(f"{day} ")

            day_index += 1
            if day_index % 7 == 0:
                weeks.append(week)
                week = []
        return weeks
