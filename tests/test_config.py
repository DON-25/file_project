import json
import tempfile
import pytest
import sys
import os
# 加入项目根目录到 Python 路径
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config import load_config

def test_load_valid_config():
    # 模拟一个合法的 JSON 配置
    config_data = {
        "规则": {
            "图片": [".jpg", ".png"],
            "文档": [".docx", ".pdf"],
            "压缩包":[".zip",".rar",".7z"],
            "视频": [".mp4", ".avi", ".mov"]            
        }
    }

    #创建一个临时的 config.json 测试文件，把内容写进去，并返回它的路径。
    with tempfile.NamedTemporaryFile("w+", delete=False, suffix=".json") as tmp:
        json.dump(config_data, tmp)
        tmp_path = tmp.name

    result = load_config(tmp_path)
    assert isinstance(result, dict)#测试格式
    assert "规则" in result#测试分类
    assert ".jpg" in result["规则"]["图片"]#测试扩展名

def test_load_invalid_json():
    # 模拟一个错误格式的 JSON 文件
    with tempfile.NamedTemporaryFile("w+", delete=False, suffix=".json") as tmp:
        tmp.write("这不是合法 JSON")
        tmp_path = tmp.name

    with pytest.raises(RuntimeError):
        load_config(tmp_path)
