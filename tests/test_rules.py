import sys
import os
from pathlib import Path

# Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from rules import match_category

# Mock rules for testing
mock_rules = {
    "images": [".jpg", ".png"],
    "documents": [".docx", ".pdf"],
    "archives": [".zip", ".rar"],
}

## Test if known extensions are matched correctly
def test_match_known_extensions():
    assert match_category(Path("test.jpg"), mock_rules) == "images"
    assert match_category(Path("doc.PDF"), mock_rules) == "documents"  # Test case-insensitivity
    assert match_category(Path("archive.rar"), mock_rules) == "archives"

#Test for unknown extension
def test_match_unknown_extension():
    assert match_category(Path("file.txt"), mock_rules) is None

#Test for file without extension
def test_match_no_extension():
    assert match_category(Path("file"), mock_rules) is None

#Test for empty filename
def test_match_empty_filename():
    assert match_category(Path(""), mock_rules) is None
