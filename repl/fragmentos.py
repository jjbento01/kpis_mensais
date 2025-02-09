from main import primeiro_ultimo_mes
dados['logins_day'].sort(by="Date").filter(
	(
		dados['logins_day']["Date"] >= primeiro_ultimo_mes
	) & (
		dados['logins_day']["Date"] <= ultimo
	)
)['Date', 'Qtd_Logins_MyMeo']

dados['logins_day'].filter(dados['logins_day']["Date"].month == 10)
list(
    dados['logins_week'].filter(
		(
			dados['logins_week']["Year"] == ultimo.year
		) & (
			dados['logins_week']["Week"] == (ultimo.isocalendar().week-3)
		)
	)['Qtd_Logins_MyMeo']
)[0]

dados['logins_day'].filter(dados['logins_day']["Date"].month == 10)
list(
    dados['logins_week'].filter(
		(
			dados['logins_week']["Year"] == ultimo.year
		) & (
			dados['logins_week']["Week"] == ultimo.isocalendar().week
		)
	)['Qtd_Logins_MyMeo']
)[0]

lista_ytd = [
	sum(
		list(
			dados['logins_week'].filter(
				(
					dados['logins_week']['Year']==2024
				)&(
					dados['logins_week']['Week']<44
				)
			)[item]
		)
	) for item in lista
]
