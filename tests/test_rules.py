import sys
import os
from pathlib import Path

# 加入项目根目录
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from rules import match_category

# 测试用的模拟规则
mock_rules = {
    "图片": [".jpg", ".png"],
    "文档": [".docx", ".pdf"],
    "压缩包": [".zip", ".rar"],
}

#测试能否根据后缀名找到对应文件分类
def test_match_known_extensions():
    assert match_category(Path("test.jpg"), mock_rules) == "图片"
    assert match_category(Path("doc.PDF"), mock_rules) == "文档"  # 测试大小写
    assert match_category(Path("archive.rar"), mock_rules) == "压缩包"

#测试没有的拓展
def test_match_unknown_extension():
    assert match_category(Path("file.txt"), mock_rules) is None

#测试无扩展名
def test_match_no_extension():
    assert match_category(Path("file"), mock_rules) is None

#测试空文件名
def test_match_empty_filename():
    assert match_category(Path(""), mock_rules) is None
