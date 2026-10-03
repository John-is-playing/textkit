# textkit

一个用于演示/测试 **Fissue** 的小型文本处理库。

> 这个仓库是 **Fissue 的测试夹具**，用真实的小项目来验证「抓取 Issue/PR → AI 评测
> → 生成验证器 → 沙盒 F2P 验证 → 自动修复提 PR」这条链路是否真的能跑通。

## 安装

```bash
pip install -e ".[dev]"
```

## 使用

```python
from textkit import slugify, wrap, word_count, parse_numbers, truncate

slugify("Hello World")        # 'hello-world'
wrap("hello world", 5)        # ['hello', 'world']
word_count("hello world")     # 2
parse_numbers("售价 1,234.50") # [1234.5]
truncate("hello world", 5)    # 'hello'
```

## 运行测试

```bash
python -m pytest -q
```

## API

| 函数 | 说明 |
|---|---|
| `slugify(text)` | 文本 → URL 友好 slug |
| `wrap(text, width)` | 按宽度折行，返回行列表 |
| `word_count(text)` | 统计单词数 |
| `char_count(text, ignore_spaces=False)` | 统计字符数 |
| `parse_numbers(text)` | 提取文本中的数字 |
| `truncate(text, limit)` | 截断文本 |
| `truncate_words(text, limit)` | 按单词边界截断 |

## 已知问题

见本仓库的 Issues 列表。当前版本 `0.3.1`。

## 许可

MIT
