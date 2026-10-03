"""文本 → URL 友好 slug。"""

from __future__ import annotations

import re

# 允许保留的字符：字母、数字、下划线、空白、连字符
_UNSAFE = re.compile(r"[^\w\s-]", re.UNICODE)


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
    # 空白替换为连字符
    text = text.replace(" ", "-")
    return text
