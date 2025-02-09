from datetime import datetime, timedelta
from typing import *

import polars as pl
day_of_week = {
    0: "Mon",
    1: "Tue",
    2: "Wed",
    3: "Thu",
    4: "Fri",
    5: "Sat",
    6: "Sun"
}

def getdays_for_week(ultimo: datetime)->list:
    first_day = ultimo - timedelta(weeks=5)
    first_day_week = first_day - timedelta(days=first_day.weekday())
    first_year = first_day.year
    first_week = first_day.isocalendar()[1]
    second_day = ultimo - timedelta(weeks=4)
    second_day_week = second_day - timedelta(days=second_day.weekday())
    second_year = second_day.year
    second_week = second_day.isocalendar()[1]
    third_day = ultimo - timedelta(weeks=3)
    third_day_week = third_day - timedelta(days=third_day.weekday())
    third_year = third_day.year
    third_week = third_day.isocalendar()[1]
    fourth_day = ultimo - timedelta(weeks=2)
    fourth_day_week = fourth_day - timedelta(days=fourth_day.weekday())
    fourth_year = fourth_day.year
    fourth_week = fourth_day.isocalendar()[1]
    ultimo_day_week = ultimo - timedelta(days=ultimo.weekday())
    fifth_year = ultimo.year
    if ultimo.month==12 and ultimo.isocalendar().week==1:
        fifth_week = 52
    else:
        fifth_week = fourth_week+1
    return [[first_day_week, first_year, first_week], 
            [second_day_week, second_year, second_week], 
            [third_day_week, third_year, third_week], 
            [fourth_day_week, fourth_year, fourth_week], 
            [ultimo_day_week, fifth_year, fifth_week]]

def edate(data: datetime)->datetime:
    temp = data.replace(day=1)
    tem2 = temp - timedelta(days=1)
    if tem2.day < data.day:
        return tem2
    return tem2.replace(day=data.day)

def last_day_of_last_month(data: datetime) -> datetime:
    return data.replace(day=1) - timedelta(days=1)

def first_day_a_year_ago(data: datetime) -> datetime:
    day_month_last_year = last_day_of_last_month(data)-timedelta(days=370)
    day_posterior_month = day_month_last_year+timedelta(days=5)
    return day_posterior_month - timedelta(days=(day_posterior_month.day-1))

def range_needed_of_date(data:datetime)->pl.Series:
    first_day = first_day_a_year_ago(data)
    last_day = last_day_of_last_month(data)
    return pl.date_range(first_day, last_day, "1d", eager=True)

def get_day(tabela: str, key: str,dados: dict, day: datetime.date)->int:
    return list(dados[tabela].filter(dados[tabela][key] == day.date())[tabela])[0]
            
def get_data_year_week(dados: dict, key: str, year: int, week: int, col: str)->int:
    return list(
        dados[key].filter(
            (
                dados[key]["Year"] == year
            ) & (
                dados[key]["Week"] == week
            )
        )[col]
    )[0]
    
def get_data_year_month(dados: dict, key: str, year: int, week: int, col: str)->int:
    return list(
        dados[key].filter(
            (
                dados[key]["Year"] == year
            ) & (
                dados[key]["Month"] == week
            )
        )[col]
    )[0]


def calc_date_values()->list:
    ultimo: datetime=last_day_of_last_month(datetime.today())
    primeiro: datetime=first_day_a_year_ago(datetime.today())
    primeiro_ultimo_mes: datetime=ultimo.replace(day=1)
    last_last_month: datetime = primeiro_ultimo_mes - timedelta(days=1)
    first_last_month: datetime = last_last_month.replace(day=1)
    return [ultimo, primeiro, primeiro_ultimo_mes, first_last_month, last_last_month]