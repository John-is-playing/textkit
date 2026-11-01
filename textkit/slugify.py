"""文本 → URL 友好 slug。"""

from __future__ import annotations

import re

# 允许保留的字符：字母、数字、下划线、空白、连字符
_UNSAFE = re.compile(r"[^\w\s-]", re.UNICODE)

# 任意长度的空白/连字符序列（可混排）统一折叠成单个连字符
_SEPARATORS = re.compile(r"[\s-]+", re.UNICODE)


def slugify(text: str) -> str:
    """把任意文本转成 URL 友好的 slug。

    规则：
        1. 去掉首尾空白并转小写
        2. 剔除不安全的标点
        3. 空白与连字符统一折叠成单个 ``-``

    示例::

        >>> slugify("Hello World")
        'hello-world'
        >>> slugify("Hello   World")
        'hello-world'
    """
    if not isinstance(text, str):
        raise TypeError("text 必须是字符串")

    text = text.strip().lower()
    text = _UNSAFE.sub("", text)
    # 任意长度的空白/连字符序列折叠为单个连字符
    text = _SEPARATORS.sub("-", text)
    # 去掉折叠后可能残留在首尾的连字符
    return text.strip("-")
