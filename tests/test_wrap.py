"""wrap 的测试。"""

from __future__ import annotations

import pytest

from textkit import wrap


def test_short_text_single_line():
    assert wrap("hello world", 11) == ["hello world"]


def test_wraps_at_width():
    assert wrap("hello world", 5) == ["hello", "world"]


def test_multiple_lines():
    result = wrap("the quick brown fox jumps", 10)
    assert result == ["the quick", "brown fox", "jumps"]
    for line in result:
        assert len(line) <= 10


def test_empty_text():
    assert wrap("", 10) == []
    assert wrap("   ", 10) == []


def test_rejects_non_positive_width():
    with pytest.raises(ValueError):
        wrap("hello", 0)
    with pytest.raises(ValueError):
        wrap("hello", -1)


def test_long_word_own_line():
    assert wrap("short verylongword", 5) == ["short", "verylongword"]


def test_collapses_extra_whitespace():
    assert wrap("hello    world", 11) == ["hello world"]
