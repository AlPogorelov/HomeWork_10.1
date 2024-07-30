import masks

def mask_account_card(account_card_str: str) -> str:
    '''Функция принимает строку с номером карты или счета и  возвращает маску'''
    account_card_mask = None
    if account_card_str[-20::].isdigit():
        number = account_card_str[-20::]
        account_card_mask = account_card_str[:-20] + masks.get_mask_account(number)
    elif account_card_str[-16::].isdigit():
        number = account_card_str[-16::]
        account_card_mask = account_card_str[:-16] + masks.get_mask_card_number(number)
    return account_card_mask


def get_date(str_date_format: str) -> str:
    '''Функция ворматирует дата вид ДД.ММ.ГГГГ'''
    normal_format_date = ''
    date_split = str_date_format.split('T')
    date_split = date_split[0]
    date_split = [date_split[-2:], date_split[-5:-3], date_split[:4]]
    normal_format_date = '.'.join(date_split)
    return normal_format_date
