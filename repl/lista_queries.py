lista_queries_a_fazer = [
    #["users_ac_asis_d","SELECT * FROM dbo.vw_IND_Users_AC_Asis_D"],
    #["users_ac_day_ltyd","SELECT * FROM dbo.vw_IND_Users_AC_Day_LYTD"],
    #["users_ac_week_ltyd","SELECT * FROM dbo.vw_IND_Users_AC_Week_LYTD"],
    #["users_ac_month_ltyd","SELECT * FROM dbo.vw_IND_Users_AC_Month_LYTD"],
    #["logins_Day_ltyd","SELECT * FROM dbo.vw_LOGINS_Day_LYTD WHERE Qtd_Logins_MyMeo<>0 and Qtd_Logins_Moche<>0 and Qtd_Logins_Uzo <>0"],
    #["logins_Week_ltyd","SELECT * FROM dbo.vw_LOGINS_Week_LYTD WHERE Qtd_Logins_MyMeo<>0 and Qtd_Logins_Moche<>0 and Qtd_Logins_Uzo <>0"],
    #["logins_Month_ltyd","SELECT * FROM dbo.vw_LOGINS_Month_LYTD WHERE Qtd_Logins_MyMeo<>0 and Qtd_Logins_Moche<>0 and Qtd_Logins_Uzo <>0"],
    #["carregamentos_day_ltyd","SELECT * FROM dbo.vw_CARREGPAG_Day_LYTD"],
    #["carregamentos_week_ltyd","SELECT * FROM dbo.vw_CARREGPAG_Week_LYTD"],
    #["carregamentos_month_ltyd","SELECT * FROM dbo.vw_CARREGPAG_Month_LYTD"],
    #["users_ac_asis","SELECT * FROM dbo.vw_IND_Users_AC_Asis"],
    #["users_ac_asis","SELECT * FROM dbo.vw_IND_Users_AC_Asis"],
    ["users_ac_day","SELECT * FROM dbo.vw_IND_Users_AC_Day_LYTM"],
    ["users_ac_week","SELECT * FROM dbo.vw_IND_Users_AC_Week_LYTM"],
    ["users_ac_month","SELECT * FROM dbo.vw_IND_Users_AC_Month_LYTM"],
    ["new_users_day","SELECT * FROM dbo.vw_New_Users_ACC_Day_LYTM"],
    ["new_users_week","SELECT * FROM dbo.vw_New_Users_ACC_Week_LYTM"],
    ["new_users_month","SELECT * FROM dbo.vw_New_Users_ACC_Month_LYTM"],
    ["logins_day","SELECT * FROM dbo.vw_Logins_Day_LYTM"],
    ["logins_week","SELECT * FROM dbo.vw_Logins_Week_LYTM"],
    ["logins_month","SELECT * FROM dbo.vw_Logins_Month_LYTM"],
    ["logins_day_tv","SELECT * FROM dbo.vw_LOGINS_TV_Day_LYTM"],
    ["logins_week_tv","SELECT * FROM dbo.vw_LOGINS_TV_Week_LYTM"],
    ["logins_month_tv","SELECT * FROM dbo.vw_LOGINS_TV_Month_LYTM"],
    #["cpag_day","SELECT * FROM dbo.vw_CARREGPAG_Day_LYTM"],
    #["cpag_week","SELECT * FROM dbo.vw_CARREGPAG_Week_LYTM"],
    #["cpag_month","SELECT * FROM dbo.vw_CARREGPAG_Month_LYTM"],
]

lista: list = [
    "Qtd_Logins_MyMeo",
    "Qtd_Logins_Moche",
    "Qtd_Logins_Uzo",
    "Qtd_Logins_MyPTE",
    "Qtd_Logins_ACE",
    "Qtd_Logins_Unique"
]

lista_sem_uzo_nem_unique: list = [
    "Qtd_Logins_MyMeo",
    "Qtd_Logins_Moche",
    "Qtd_Logins_MyPTE",
    "Qtd_Logins_ACE"
]


lista_unica: list = [
    "Qtd_Logins_MyMeo",
    "Qtd_Logins_Moche",
    "Qtd_Logins_Uzo",
    "Qtd_Logins_MyPTE",
    "Qtd_Logins_ACE"
]

