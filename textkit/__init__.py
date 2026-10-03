"""textkit —— 一个用于演示 Fissue 的小型文本处理库。

已发布的稳定功能：
    slugify     文本 → URL 友好 slug
    wrap        按宽度折行
    word_count  统计单词数
    parse_numbers 从文本提取数字
    truncate    截断文本
"""

from .slugify import slugify
from .stats import word_count
from .tokenize import parse_numbers
from .truncate import truncate
from .wrap import wrap

__version__ = "0.3.1"

__all__ = [
    "slugify",
    "wrap",
    "word_count",
    "parse_numbers",
    "truncate",
    "__version__",
]
