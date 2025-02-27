from datetime import datetime, timedelta
from typing import *
from sqlalchemy import create_engine, engine
import codecs
import os
from yaml import load, FullLoader
import polars as pl

#with codecs.open(str(os.getenv("CONFS"))+"conf_dba\\configuracao.yaml", "r", "utf-8") as fich:
#    config = load(fich, Loader=FullLoader)
#    string_conf = config['con_str_0']

#bd: str ='BD_GESTAOSQL'
#engine: engine = create_engine(f'mssql+pyodbc:///?odbc_connect={ string_conf };DATABASE='+bd)


day_of_week = {
    0: "Mon",
    1: "Tue",
    2: "Wed",
    3: "Thu",
    4: "Fri",
    5: "Sat",
    6: "Sun"
}

def get_first_day_of_week(year, week):
    first_day_of_year = datetime(year, 1, 1)
    first_week_start = first_day_of_year - timedelta(days=first_day_of_year.weekday())
    return first_week_start + timedelta(weeks=week-1)

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
    """
    Function to get the value of a given column in a given week of a given year in a given table
    :param dados: dictionary with the dataframes of the tables
    :param key: key of the table in the dictionary
    :param year: year to get the data
    :param week: week to get the data
    :param col: name of thecolumn to get the data
    :return: the value of the column in the given week of the given year in the given table
    """   
    sdt = dados[key].with_columns(pl.struct(["Year", "Week"]).map_elements(lambda x: get_first_day_of_week(x["Year"], x["Week"]), return_dtype=pl.Datetime).alias("Data")).sort(by=["Data"]) 
    ddt = sdt.filter(pl.col("Data")==sdt.filter((pl.col("Year")==year)&(pl.col("Week")==week))["Data"][0])
    dfd = ddt.group_by("Data").agg(pl.exclude(["Year", "Week"]).sum())
    return dfd[col][0]

def get_data_year_month(dados: dict, key: str, year: int, month: int, col: str)->int:
    return list(dados[key].filter((dados[key]["Year"] == year) & (dados[key]["Month"] == month))[col])[0]


def calc_date_values()->list:
    ultimo: datetime=last_day_of_last_month(datetime.today())
    primeiro: datetime=first_day_a_year_ago(datetime.today())
    primeiro_ultimo_mes: datetime=ultimo.replace(day=1)
    last_last_month: datetime = primeiro_ultimo_mes - timedelta(days=1)
    first_last_month: datetime = last_last_month.replace(day=1)
    return [ultimo, primeiro, primeiro_ultimo_mes, first_last_month, last_last_month]
