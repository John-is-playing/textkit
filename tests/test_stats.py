"""stats 的测试。"""

from __future__ import annotations

from textkit import word_count
from textkit.stats import char_count


def test_counts_words():
    assert word_count("hello world") == 2


def test_single_word():
    assert word_count("hello") == 1


def test_three_words():
    assert word_count("one two three") == 3


def test_char_count():
    assert char_count("hello") == 5


def test_char_count_ignore_spaces():
    assert char_count("hello world", ignore_spaces=True) == 10
    assert char_count("hello world") == 11
