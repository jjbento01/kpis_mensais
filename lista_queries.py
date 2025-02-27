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
    ["users_ac_asis","SELECT * FROM dbo.vw_IND_Users_AC_Asis"],
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
    ["cpag_day","SELECT * FROM dbo.vw_CARREGPAG_Day_LYTM"],
    ["cpag_week","SELECT * FROM dbo.vw_CARREGPAG_Week_LYTM"],
    ["cpag_month","SELECT * FROM dbo.vw_CARREGPAG_Month_LYTM"],
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

tags_logins: list = [
        'Área de Cliente',
        '',
        'Logins Web',
        '      Logins My Meo',
        '      Logins Moche',
        '      Logins Uzo',
        '      Logins My PT Empresas',
        '      Logins AC PT Empresas',
        '      Unique Logins',
        '      Average Logins per User']

lista_segm: list = [
        'ACC_Total',
        'ACC_Consumo',
        'ACC_Moche',
        'ACC_Uzo',
        'ACC_Altice_Empresas',
        'ACC_ACE',
        'ACE_Total',
        'ACE_Empresariais',
        'ACE_Altice_Empresas',
        'Altice_Empresas_Total']

lista_tags_users: list = [
    'Logins',
    '      New First Logins',
    '      ACC Total*',
    '            ACC Meo',
    '            ACC Moche*****',
    '            ACC UZO*****',
    '            ACC Altice Empresas****',
    '      ACC ∩ ACE',
    '      ACE Total**',
    '            ACE só Empresariais',
    '            ACE Altice Empresas',
    '      Altice Empresas Total']

cpag_tags = [
    'Pagamentos por AC ***',
    '      MyMeo',
    '      MyMoche',
    '      MyUzo',
    '      MyAlticeEmpresas']

carg_tags = [
    'Carregamentos por AC ***',
    '      MyMeo',
    '      MyMoche',
    '      MyUzo',
    '      MyAlticeEmpresas']

euro_pag_tags = [
    'Pagamentos por AC (€) ***',
    '      MyMeo',
    '      MyMoche',
    '      MyUzo',
    '      MyAlticeEmpresas'
]

euro_car_tags = [
    'Pagamentos por AC (€) ***',
    '      MyMeo',
    '      MyMoche',
    '      MyUzo',
    '      MyAlticeEmpresas'
]


listagem_cpag = [
    'Pag_MyMeo',
    'Pag_MyMoche',
    'Pag_MyUzo',
    'Pag_MyAlticeEmpresas'
]

listagem_carg = [
    'Car_MyMeo',
    'Car_MyMoche',
    'Car_MyUzo',
    'Car_MyAlticeEmpresas'
]

listagem_euro_pag = [
    '€_Pag_MyMeo',
    '€_Pag_MyMoche',
    '€_Pag_MyUzo',
    '€_Pag_MyAlticeEmpresas'
]

listagem_euro_car = [
    '€_Car_MyMeo',
    '€_Car_MyMoche',
    '€_Car_MyUzo',
    '€_Car_MyAlticeEmpresas'
]

lista_iteracoes = [
    [2, 32, 3, cpag_tags, listagem_cpag],
    [2, 37, 3, carg_tags, listagem_carg],
    [2, 42, 3, euro_pag_tags, listagem_euro_pag],
    [2, 47, 3, euro_car_tags, listagem_euro_car]
]
