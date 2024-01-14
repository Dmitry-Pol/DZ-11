import pytest
import use_functions
import mock
import builtins
import json
import math

a = list(range(5))
assert list(filter(lambda x: x < 3, a)) == [0, 1, 2]
assert list(map(lambda x: x*x, a)) == [0, 1, 4, 9, 16]
assert sorted(a, reverse=True) == [4, 3, 2, 1, 0]
assert str(math.pi)[:4] == '3.14'
assert math.sqrt(4) == 2


def test_fun_increase():
    with mock.patch.object(builtins, 'input', lambda _: 50):
        assert use_functions.fun_increase(50) == 100

def test_fun_buy1():
    # assert use_functions.fun_increase(50) == 'введите сумму'
    with open('text.data', 'r') as f:
        schet = json.load(f)
    with open('text_hist.data', 'r') as f:
        dic = json.load(f)
    with mock.patch.object(builtins, 'input', lambda _: 1200):
        assert use_functions.fun_buy(schet, dic)[0] == schet
    # assert use_functions.fun_buy(schet, dic)[0] == schet

def test_fun_buy2():
    # assert use_functions.fun_increase(50) == 'введите сумму'
    with open('text.data', 'r') as f:
        schet = json.load(f)
    with open('text_hist.data', 'r') as f:
        dic = json.load(f)
    with mock.patch.object(builtins, 'input', lambda _: 600):
        assert use_functions.fun_buy(schet, dic)[0] == schet - 600

def test_fun_history():
    with open('text_hist.data', 'r') as f:
        dic = json.load(f)
    assert use_functions.fun_history(dic) == None
