"""tokenize 的测试。"""

from __future__ import annotations

from textkit import parse_numbers


def test_integers():
    assert parse_numbers("abc 42 def") == [42.0]


def test_decimals():
    assert parse_numbers("pi is 3.14") == [3.14]


def test_thousands_separator():
    assert parse_numbers("售价 1,234.50 元") == [1234.5]


def test_negative_numbers():
    assert parse_numbers("温度 -5 度") == [-5.0]


def test_multiple_numbers_in_order():
    assert parse_numbers("范围 1-2") == [1.0, 2.0]


def test_no_numbers():
    assert parse_numbers("no digits here") == []
