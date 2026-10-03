"""从任意文本中提取数字。"""

from __future__ import annotations

import re

# 数字：可带负号、千分位逗号、可选小数部分。
# 用负向后顾断言 ``(?<![\d,])`` 保证短横线不会被当成负号：
#   在 "1-2" 中，扫描到 "-" 时前一个字符是数字，因此不从 "-" 开始匹配，
#   于是得到 [1.0, 2.0] 而不是 [1.0, -2.0]。
_NUMBER = re.compile(r"(?<![\d,])-?[\d,]+(?:\.\d+)?")


def parse_numbers(text: str) -> list[float]:
    """提取 ``text`` 中出现的所有数字，按出现顺序返回。

    支持：
        * 整数与小数：``42``、``3.14``
        * 千分位：``1,234`` → ``1234.0``
        * 负数：``-5`` → ``-5.0``

    示例::

        >>> parse_numbers("售价 1,234.50 元")
        [1234.5]
        >>> parse_numbers("范围 1-2")
        [1.0, 2.0]
    """
    out: list[float] = []
    for raw in _NUMBER.findall(text):
        cleaned = raw.replace(",", "")
        try:
            out.append(float(cleaned))
        except ValueError:  # pragma: no cover - 正则已保证可解析
            continue
    return out
