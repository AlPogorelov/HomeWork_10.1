import pytest

from src.decorators import log


@log('')
def test_func():
    print('func on')


@log('log.txt')
def test_func():
    print('func on')


def test_test_func(capsys):
    test_func()
    capture = capsys.readouterr()
    assert capture.out == 'func on\n'


