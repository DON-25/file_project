import sys
import os
from pathlib import Path
import tempfile
import shutil
import pytest

# 加入项目根目录路径（保证能找到 organizer.py）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from organizer import organize_files

def test_organize_files_moves_file():
    with tempfile.TemporaryDirectory() as temp_dir:
        base = Path(temp_dir)

        # 创建两个文件：一个匹配规则，一个不匹配
        file1 = base / "photo.jpg"
        file2 = base / "note.txt"

        file1.write_text("图片内容")
        file2.write_text("文本内容")

        config = {
            "rules": {
                "图片": [".jpg"],
                "文档": [".docx", ".pdf"]
            }
        }

        # 执行整理函数
        organize_files(base, config)

        # 由于break了，只处理第一个文件
        # 所以我们检查是否处理了 file1
        moved_file1 = base / "图片" / "photo.jpg"
        assert moved_file1.exists()
        assert not file1.exists()
        assert file2.exists()  # 第二个文件应该没被处理

#验证传入一个不存在的路径是否能正确抛出异常
def test_organize_files_invalid_path():
    fake_path = Path("不存在的路径")
    config = {"rules": {"图片": [".jpg"]}}
    with pytest.raises(ValueError):
        organize_files(fake_path, config)

#验证：如果一个文件的扩展名不匹配任何分类规则，它不应该被移动
def test_organize_files_unmatched():
    with tempfile.TemporaryDirectory() as temp_dir:
        base = Path(temp_dir)
        file = base / "file.xyz"
        file.write_text("未知扩展名")

        config = {
            "rules": {
                "图片": [".jpg", ".png"]
            }
        }

        organize_files(base, config)

        # 没有匹配规则，不应该被移动
        assert file.exists()
