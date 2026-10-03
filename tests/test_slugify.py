"""slugify 的测试。"""

from __future__ import annotations

import pytest

from textkit import slugify


def test_simple_words():
    assert slugify("Hello World") == "hello-world"


def test_lowercased():
    assert slugify("HELLO") == "hello"


def test_strips_surrounding_whitespace():
    assert slugify("  hello world  ") == "hello-world"


def test_punctuation_removed():
    assert slugify("Hello, World!") == "hello-world"


def test_numbers_preserved():
    assert slugify("Version 2 Release") == "version-2-release"


def test_unicode_letters_preserved():
    # \w 在 re.UNICODE 下包含中文
    assert slugify("中文 标题") == "中文-标题"


def test_rejects_non_string():
    with pytest.raises(TypeError):
        slugify(123)  # type: ignore[arg-type]


def test_underscores_preserved():
    assert slugify("foo_bar baz") == "foo_bar-baz"


def test_collapses_consecutive_spaces():
    """连续空白应折叠成单个连字符（对应 issue #2）。"""
    assert slugify("Hello   World") == "hello-world"
    assert slugify("a    b") == "a-b"
    assert slugify("  spaced  out  ") == "spaced-out"
