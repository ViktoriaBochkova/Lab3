import datetime as dt


class Calculator:
    def __init__(self, limit):
        self.limit = float(limit)
        self.records = []

    def add_record(self, new_records):
        self.records.append(new_records)

    def get_today_stats(self):
        day_today = dt.date.today()
        summ = 0
        for RECORD in self.records:
            if RECORD.date == day_today:
                summ += RECORD.amount
            return summ

    def get_week_stats(self):
        week_sum = 0
        week = dt.date.today()
        delta7 = week - dt.timedelta(days=7)
        for record in self.records:
            if delta7 < record.date <= week:
                week_sum += record.amount
        return week_sum


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        caloric = self.limit - self.get_today_stats()
        if caloric == self.limit or caloric > self.limit:
            return f'Хватит есть!'
        else:
            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {caloric} кКал»'


class CashCalculator(Calculator):

    def get_today_cash_remained(self, currency):
        USD_RATE = 63.49
        EURO_RATE = 62.59
        RUB_RATE = 1.0
        cash = self.limit - self.get_today_stats()
        if currency == "eur":
            cash = cash / EURO_RATE
        elif currency == "usd":
            cash = cash / USD_RATE
        elif currency == "rub":
            cash = cash / RUB_RATE
        if cash == 0:
            return f'Денег нет, держись'
        elif cash > 0:
            return f'На cегодня осталось  {cash} {currency}'
        else:
            return f'Денег нет, держись: твой долг - {cash} {currency}'


class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = float(amount)
        self.comment = str(comment)
        if date is not None:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()
        else:
            self.date = dt.date.today()


'''
# создадим калькулятор денег с дневным лимитом 1000
cash_calculator = CashCalculator(1000)

# дата в параметрах не указана,
# так что по умолчанию к записи
# должна автоматически добавиться сегодняшняя дата
cash_calculator.add_record(Record(amount=145, comment='кофе'))
# и к этой записи тоже дата должна добавиться автоматически
cash_calculator.add_record(Record(amount=300, comment='Серёге за обед'))
# а тут пользователь указал дату, сохраняем её
cash_calculator.add_record(Record(amount=3000,
                                  comment='бар в Танин др',
                                 date='08.11.2019'))
print(cash_calculator.get_today_cash_remained(rub))
# должно напечататься
# На сегодня осталось 555 руб
 '''
