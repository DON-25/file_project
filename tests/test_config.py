import json
import tempfile
import pytest
import sys
import os
# Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config import load_config

def test_load_valid_config():
    # Simulate a valid JSON config
    config_data = {
        "rules": {
            "images": [".jpg", ".png"],
            "documents": [".docx", ".pdf"],
            "archives":[".zip",".rar",".7z"],
            "videos": [".mp4", ".avi", ".mov"]            
        }
    }

    # Create a temporary config.json test file with the above content
    with tempfile.NamedTemporaryFile("w+", delete=False, suffix=".json") as tmp:
        json.dump(config_data, tmp)
        tmp_path = tmp.name

    result = load_config(tmp_path)
    assert isinstance(result, dict)#Check that result is a dictionary
    assert "rules" in result#Check rules key exists
    assert ".jpg" in result["rules"]["images"]#Check file extension match

def test_load_invalid_json():
    # Simulate an invalid JSON file
    with tempfile.NamedTemporaryFile("w+", delete=False, suffix=".json") as tmp:
        tmp.write("This is not valid JSON")
        tmp_path = tmp.name

    with pytest.raises(RuntimeError):
        load_config(tmp_path)
