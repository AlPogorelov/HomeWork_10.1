import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "card_account, mask",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("", ""),
        ("Счет 1425", ""),
        ("card 12456", ""),
    ],
)
def test_mask_account_card(card_account, mask):
    assert mask_account_card(card_account) == mask


@pytest.mark.parametrize(
    "date, norm_date", [("2024-03-11T02:26:18.671407", "11.03.2024"), ("2024-03-11", "11.03.2024"), ("", "")]
)
def test_get_date(date, norm_date):
    assert get_date(date) == norm_date
