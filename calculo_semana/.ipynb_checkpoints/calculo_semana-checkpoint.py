from datetime import datetime, timedelta
for i in [2024, 2025, 2026, 2027, 2028, 2029, 2030]:
    dia = datetime(i, 12, 31, 23,59,59)
    print(dia.isocalendar(), i, dia.strftime("%A"))
    if dia.isocalendar().year > i or dia.isocalendar().week == 53:
        print("Semana entre no outro ano")