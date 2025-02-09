from datetime import datetime
import pandas as pd
def lista_de_dias(ano_inicial: int) -> None:
    lista1: list[int] = []
    lista2: list[str] = []
    lista3: list[str] = []
    inic: int = ano_inicial
    for i in [
        datetime(inic,12,25,0,0,0),
        datetime(inic,12,26,0,0,0),
        datetime(inic,12,27,0,0,0),
        datetime(inic,12,28,0,0,0),
        datetime(inic,12,29,0,0,0),
        datetime(inic,12,30,0,0,0),
        datetime(inic,12,31,0,0,0),
        datetime(inic+1,1,1,0,0,0),
        datetime(inic+1,1,2,0,0,0),
        datetime(inic+1,1,3,0,0,0),
        datetime(inic+1,1,4,0,0,0),
        datetime(inic+1,1,5,0,0,0)]:
        lista1.append(i.isocalendar().weekday)
        lista2.append(i.strftime("%A"))
        lista3.append(i.strftime("%d/%m/%Y"))

    df: pd.DataFrame = pd.DataFrame({'Dia': lista3, 'Dia da semana': lista1, 'Dia da semana (nome)': lista2})
    print(df)

if __name__ == '__main__':
    lista_de_dias(2022)
    lista_de_dias(2023)
    lista_de_dias(2024)
    lista_de_dias(2025)
    lista_de_dias(2026)