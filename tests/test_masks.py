import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize(
    "card, card_mask",
    [
        ("1111222233334444", "1111 22** **** 4444"),
        ("1111 2222 3333 4444", "1111 22** **** 4444"),
        ("1245", ""),
        ("asdasd", ""),
        ("", ""),
    ],
)
def test_get_mask_card_number(card, card_mask):
    assert get_mask_card_number(card) == card_mask


@pytest.mark.parametrize(
    "account, mask_account", [("12345678912345678912", "**8912"), ("124578", ""), ("", ""), ("sdsf", "")]
)
def test_get_mask_account(account, mask_account):
    assert get_mask_account(account) == mask_account
