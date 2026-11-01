"""文本统计。"""

from __future__ import annotations


def word_count(text: str) -> int:
    """统计 ``text`` 中的单词数。

    以空格作为分隔符。连续空格、首尾空格的处理见 ``tests/test_stats.py``。

    示例::

        >>> word_count("hello world")
        2
    """
    return len(text.split())


def char_count(text: str, *, ignore_spaces: bool = False) -> int:
    """统计字符数，可选择忽略空白。"""
    if ignore_spaces:
        return sum(1 for ch in text if not ch.isspace())
    return len(text)
