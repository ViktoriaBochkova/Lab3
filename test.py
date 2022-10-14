from datetime import datetime

import CAlcul
import pytest

test_list = [{'amount': 1000, 'comment': 'что-то', 'date': '29.09.2021'},
             {'amount': 2000, 'comment': 'что-то'},
             {'amount': 100, 'comment': 'что-то', 'date': '14.10.2022'}]


@pytest.mark.parametrize("list_", test_list)
def test__init__(list_):
    result = CAlcul.Record(**list_)
    if 'date' in list_:
        assert result.date == datetime.strptime(list_['date'], '%d.%m.%Y').date()
    else:
        assert result.date == datetime.now().date()


list2 = [{'amount': 2000, 'comment': 'что-то', 'date': '2001.02.03'}]


@pytest.mark.parametrize("error", list2)
def test_errors(error):
    with pytest.raises(ValueError):
        result = CAlcul.Record(**error)
        assert result.date == datetime.strptime(error['date'], '%d.%m.%Y').date()


def test_get_today_stats():
    new_records = CAlcul.Record(amount=1000, comment='кофе')
    a = CAlcul.CashCalculator(1000)
    a.add_record(new_records)
    assert a.get_today_stats() == 1000


def test__today_cash_remained():
    new_records = CAlcul.Record(amount=1000, comment='кофе')
    a = CAlcul.CashCalculator(1000)
    a.add_record(new_records)
    a.get_today_stats()
    assert a.get_today_cash_remained("rub") == 'Денег нет, держись'
