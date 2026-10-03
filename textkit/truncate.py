"""文本截断。"""

from __future__ import annotations


def truncate(text: str, limit: int) -> str:
    """把 ``text`` 截断到 ``limit`` 个字符。

    文本不长于 ``limit`` 时原样返回。

    :param text: 待截断文本
    :param limit: 最大字符数，必须非负
    :returns: 截断后的文本，长度不超过 ``limit``

    示例::

        >>> truncate("hello", 10)
        'hello'
        >>> truncate("hello world", 5)
        'hello'
    """
    if limit < 0:
        raise ValueError("limit 不能为负数")
    if len(text) <= limit:
        return text
    return text[:limit]


def truncate_words(text: str, limit: int) -> str:
    """按单词边界截断，避免截断到单词中间。"""
    if len(text) <= limit:
        return text
    cut = text[:limit].rsplit(" ", 1)[0]
    return cut or text[:limit]
