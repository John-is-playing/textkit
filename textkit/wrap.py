"""按宽度折行。"""

from __future__ import annotations


def wrap(text: str, width: int) -> list[str]:
    """把 ``text`` 按 ``width`` 折成多行。

    折行规则：以空白分词，逐词拼装；某行加上下一个词会超宽时换行。
    单个词超过 ``width`` 时独占一行（不做硬切分）。

    :param text: 待折行文本
    :param width: 每行最大字符数，必须为正
    :returns: 每一行的列表

    示例::

        >>> wrap("hello world", 11)
        ['hello world']
        >>> wrap("hello world", 5)
        ['hello', 'world']
    """
    if width <= 0:
        raise ValueError("width 必须为正数")

    words = text.split()
    if not words:
        return []

    lines: list[str] = []
    current = ""
    for word in words:
        candidate = f"{current} {word}".strip()
        if len(candidate) <= width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word

    if current:
        lines.append(current)
    return lines
