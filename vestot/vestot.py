from zmanim.hebrew_calendar.jewish_date import JewishDate

class HebFormeter:
    def __init__(self):
        self.DAYS = ['א', 'ב', 'ג', 'ד', 'ה', 'ו', 'ז', 'ח', 'ט', 'י', 'יא', 'יב', 'יג', 'יד', 'טו', 'טז', 'יז', 'יח',
                     'יט',
                     'כ', 'כא', 'כב', 'כג', 'כד', 'כה', 'כו', 'כז', 'כח', 'כט', 'ל']
        self.MONTH = ['ניסן', 'אייר', 'סיון', 'תמוז', 'אב', 'אלול', 'תשרי', 'חשוון', 'כסלו', 'טבת', 'שבט', 'אדר',
                      'אדר ב']
        self.ONA = ['יום', 'לילה']

    def con_year_to_str(self, year):
        letters = {400: 'ת', 300: 'ש', 200: 'ר', 100: 'ק', 90: 'צ', 80: 'פ',
                   70: 'ע', 60: 'ס', 50: 'נ', 40: 'מ', 30: 'ל', 20: 'כ',
                   10: 'י', 9: 'ט', 8: 'ח', 7: 'ז', 6: 'ו', 5: 'ה', 4: 'ד',
                   3: 'ג', 2: 'ב', 1: 'א'}

        i_year = year - 5000
        s_year = 'ה'
        while i_year > 0:
            for key in letters.keys():
                if key <= i_year:
                    s_year = s_year + letters[key]
                    i_year = i_year - key
                    break
        s_year = s_year[:len(s_year) - 1] + '\"' + s_year[len(s_year) - 1]
        return s_year

hebFormeter = HebFormeter()

class Veset:
    def __init__(self, year, month, day, ona):
        self.date = JewishDate(year, month, day)
        self.ona = ona
        
    def get_str(self):
        day = hebFormeter.DAYS[self.date.jewish_day-1]
        month = hebFormeter.MONTH[self.date.jewish_month-1]
        year = hebFormeter.con_year_to_str(self.date.jewish_year)
        ona = hebFormeter.ONA[self.ona]

        return f"{day}' {month} <br> {year} {ona}"

    def __str__(self):
        return f'{self.__class__.__name__}: date:{self.date.jewish_date} ona:{self.ona}'


class VesetMonth:

    def __init__(self, veset):
        self.based_veset = veset
        # need to take care if veset in ל and  next month only 29 days
        self.date = self.based_veset.date + self.based_veset.date.days_in_jewish_month()
        self.ona = self.based_veset.ona
        self.orz = ([self.date.jewish_day, 1] if self.ona == 0 else [(self.date - 1).jewish_day, 0])

    def get_str(self):
        day = hebFormeter.DAYS[self.date.jewish_day-1]
        month = hebFormeter.MONTH[self.date.jewish_month-1]
        ona = hebFormeter.ONA[self.ona]
        orz = f"{hebFormeter.DAYS[self.orz[0]-1]}' {hebFormeter.ONA[self.orz[1]]}"

        return f"{day}' {month} {ona} <br> או\"ז: {orz}"

    def __str__(self):
        return f'{self.__class__.__name__}: date:{self.date.jewish_date} ona:{self.ona} orz:{self.orz}'


class VesetMedium:
    def __init__(self, veset):
        self.based_veset = veset
        self.date = self.based_veset.date + 29
        self.ona = self.based_veset.ona
        self.orz = ([self.date.jewish_day, 1] if self.ona == 0 else [(self.date - 1).jewish_day, 0])
        self.kret = ([self.date.jewish_day, 1] if self.ona == 0 else [self.date.jewish_day, 0])

    def get_str(self):
        day = hebFormeter.DAYS[self.date.jewish_day-1]
        month = hebFormeter.MONTH[self.date.jewish_month-1]
        ona = hebFormeter.ONA[self.ona]
        orz = f"{hebFormeter.DAYS[self.orz[0]-1]}' {hebFormeter.ONA[self.orz[1]]}"
        kret = f"{hebFormeter.DAYS[self.kret[0]-1]}' {hebFormeter.ONA[self.kret[1]]}"

        return f"{day}' {month} {ona} <br> או\"ז: {orz} <br> כו\"פ: {kret}"

    def __str__(self):
        return f'{self.__class__.__name__}: date:{self.date.jewish_date} ona:{self.ona} orz:{self.orz} kret{self.kret}'


class VesetMediumR:
    def __init__(self, veset):
        self.based_veset = veset
        self.date = self.based_veset.date + 29
        self.ona = self.based_veset.ona

    def get_str(self):
        day = hebFormeter.DAYS[self.date.jewish_day-1]
        month = hebFormeter.MONTH[self.date.jewish_month-1]
        year = hebFormeter.con_year_to_str(self.date.jewish_year)
        ona = hebFormeter.ONA[self.ona]

        return f"{day}' {month} {ona}"

    def __str__(self):
        return f'{self.__class__.__name__}: date:{self.date.jewish_date} ona:{self.ona}'


class VesetAfl:
    def __init__(self, old_veset, veset):
        if old_veset:
            self.old_veset = old_veset
            self.based_veset = veset
            self.afl_days = (self.based_veset.date - self.old_veset.date).days + 1
            self.date = self.based_veset.date + self.afl_days - 1
            self.ona = self.based_veset.ona
            self.orz = ([self.date.jewish_day, 1] if self.ona == 0 else [(self.date - 1).jewish_day, 0])

    def get_str(self):
        day = hebFormeter.DAYS[self.date.jewish_day-1]
        month = hebFormeter.MONTH[self.date.jewish_month-1]
        ona = hebFormeter.ONA[self.ona]
        orz = f"{hebFormeter.DAYS[self.orz[0]-1]}' {hebFormeter.ONA[self.orz[1]]}"

        return f"{day}' {month} {ona}<br> או\"ז: {orz} <br> הפלגה: {self.afl_days}"
   
    def __str__(self):
        return f'{self.__class__.__name__}: date:{self.date.jewish_date} ona:{self.ona} orz:{self.orz} aflga days:{self.afl_days}'

