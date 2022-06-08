from scripts import base_v1


def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5

def test_suffix():
    assert base_v1.return_suffix('xt.py') == '.p'
