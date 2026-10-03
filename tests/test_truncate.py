"""truncate 的测试。"""

from __future__ import annotations

import pytest

from textkit import truncate
from textkit.truncate import truncate_words


def test_no_truncation_needed():
    assert truncate("hello", 10) == "hello"


def test_exact_fit():
    assert truncate("hello", 5) == "hello"


def test_truncates():
    assert truncate("hello world", 5) == "hello"


def test_zero_limit():
    assert truncate("hello", 0) == ""


def test_rejects_negative_limit():
    with pytest.raises(ValueError):
        truncate("hello", -1)


def test_truncate_words():
    assert truncate_words("hello world", 8) == "hello"
