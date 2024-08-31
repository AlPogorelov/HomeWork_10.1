import pandas as pd


def open_xlsx(file_name):
    """Функция открывет excel файл и преобразует его в список словарей"""
    df = pd.read_excel(file_name)
    excel_file = df.to_dict(orient="records")
    return excel_file
