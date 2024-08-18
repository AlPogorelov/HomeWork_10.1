from unittest.mock import mock_open, patch

from src.decorators import log


@log("log.txt")
def add_numbers(a, b):
    return a + b


@log()
def add_numbers_2(a, b):
    return a + b


def test_log_decorator():
    m = mock_open()
    with patch("builtins.open", m):
        result = add_numbers(1, 3)
        assert result == 4
        m.assert_called_with("log.txt", "r+")

        m().write.assert_any_call("Function `add_numbers` start working.\n")
        m().write.assert_any_call("Result function `add_numbers`: 4.\n")
        m().write.assert_any_call("Function `add_numbers` finish.\n")
        assert m().write.call_count == 3


def test_log_console(capsys):
    add_numbers_2(1, 3)
    capture = capsys.readouterr()
    assert "Function `add_numbers_2` start working." in capture.out
    assert "Result function `add_numbers_2`: 4." in capture.out
    assert "Function `add_numbers_2` finish." in capture.out
