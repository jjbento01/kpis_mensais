--WARNING! ERRORS ENCOUNTERED DURING SQL PARSING!
SELECT CAST(calendar_date AS DATE) AS [Date],
	year_week AS [year_week],
	calendar_year AS [Year]
FROM BD_GESTAOSQL.dbo.date_calendar_new
WHERE CAST(calendar_date AS DATE) >= CAST(DATEADD(dd, 1, EOMONTH(GETDATE(), - 13)) AS DATE) ),
	auds AS (
		SELECT d.year_week,
			a.[Operação de Audit],
			c.Canal,
			count(*) [# Audits],
			sum(a.Amount) [€ Amount]
		FROM [BD_ACC].[dbo].FACT_Audits_CarregPag a
		LEFT JOIN BD_ECARE.[dbo].[REF_ChannelID] c ON c.ID = a.ChannelID
		INNER JOIN datecalendar d ON d.[Date] = CONVERT(DATE, [Data de Criação])
		GROUP BY d.year_week,
			[Operação de Audit],
			c.Canal
		) /*select * from auds*/,
	pivNum AS (
		SELECT year_week,
			Canal,
			isnull([Carregamento online – Confirm], 0) AS [# Carreg],
			isnull([Pagamento Online - Resultado], 0) AS [# Pag]
		FROM auds d
		PIVOT(sum([# Audits]) FOR [Operação de Audit] IN ([Carregamento online – Confirm], [Pagamento Online - Resultado])) x
		),
	pivEur AS (
		SELECT year_week,
			Canal,
			isnull([Carregamento online – Confirm], 0) AS [€ Carreg],
			isnull([Pagamento Online - Resultado], 0) AS [€ Pag]
		FROM auds d
		PIVOT(sum([€ Amount]) FOR [Operação de Audit] IN ([Carregamento online – Confirm], [Pagamento Online - Resultado])) x
		),
	finalNum AS (
		SELECT *
		FROM (
			SELECT year_week,
				dados,
				NEW_COL + ' ' + Canal AS PIV_COL
			FROM pivNum
			CROSS APPLY (
				VALUES (
					'# Car',
					[# Carreg]
					),
					(
					'# Pag',
					[# Pag]
					)
				) CS(NEW_COL, dados)
			) a
		PIVOT(sum(dados) FOR [PIV_COL] IN ([# Car MyAlticeEmpresas], [# Pag MyAlticeEmpresas], [# Car MyMeo], [# Pag MyMeo], [# Car MyMoche], [# Pag MyMoche], [# Car MyUzo], [# Pag MyUzo])) pv
		),
	finalEur AS (
		SELECT *
		FROM (
			SELECT year_week,
				dados,
				NEW_COL + ' ' + Canal AS PIV_COL
			FROM pivEur
			CROSS APPLY (
				VALUES (
					'€ Car',
					[€ Carreg]
					),
					(
					'€ Pag',
					[€ Pag]
					)
				) CS(NEW_COL, dados)
			) a
		PIVOT(sum(dados) FOR [PIV_COL] IN ([€ Car MyAlticeEmpresas], [€ Pag MyAlticeEmpresas], [€ Car MyMeo], [€ Pag MyMeo], [€ Car MyMoche], [€ Pag MyMoche], [€ Car MyUzo], [€ Pag MyUzo])) pv
		)

SELECT a.year_week / 100 AS [Year],
	a.year_week % 100 AS [Week],
	isnull([# Car MyAlticeEmpresas], 0) AS [Car_MyAlticeEmpresas],
	isnull([# Pag MyAlticeEmpresas], 0) AS [Pag_MyAlticeEmpresas],
	isnull([# Car MyMeo], 0) AS [Car_MyMeo],
	isnull([# Pag MyMeo], 0) AS [Pag_MyMeo],
	isnull([# Car MyMoche], 0) AS [Car_MyMoche],
	isnull([# Pag MyMoche], 0) AS [Pag_MyMoche],
	isnull([# Car MyUzo], 0) AS [Car_MyUzo],
	isnull([# Pag MyUzo], 0) AS [Pag_MyUzo],
	isnull([€ Car MyAlticeEmpresas], 0) AS [€_Car_MyAlticeEmpresas],
	isnull([€ Pag MyAlticeEmpresas], 0) AS [€_Pag_MyAlticeEmpresas],
	isnull([€ Car MyMeo], 0) AS [€_Car_MyMeo],
	isnull([€ Pag MyMeo], 0) AS [€_Pag_MyMeo],
	isnull([€ Car MyMoche], 0) AS [€_Car_MyMoche],
	isnull([€ Pag MyMoche], 0) AS [€_Pag_MyMoche],
	isnull([€ Car MyUzo], 0) AS [€_Car_MyUzo],
	isnull([€ Pag MyUzo], 0) AS [€_Pag_MyUzo]
FROM finalNum a,
	finalEur b
WHERE a.year_week = b.year_week
