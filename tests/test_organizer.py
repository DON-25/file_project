import sys
import os
from pathlib import Path
import tempfile
import shutil
import pytest

# Add the project root directory to the Python path (so organizer.py can be found)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from organizer import organize_files

def test_organize_files_moves_file():
    with tempfile.TemporaryDirectory() as temp_dir:
        base = Path(temp_dir)

        # Create two files: one that matches the rule, one that doesn't
        file1 = base / "photo.jpg"
        file2 = base / "note.txt"

        file1.write_text("image content")
        file2.write_text("text content")

        config = {
            "rules": {
                "images": [".jpg"],
                "documents": [".docx", ".pdf"]
            }
        }

        # Execute the organize function
        organize_files(base, config)

        # Only the matching file should be moved
        moved_file1 = base / "images" / "photo.jpg"
        assert moved_file1.exists()
        assert not file1.exists()
        assert file2.exists()  # The second file should remain untouched

# Verify that passing an invalid path raises an exception
def test_organize_files_invalid_path():
    fake_path = Path("nonexistent_path")
    config = {"rules": {"images": [".jpg"]}}
    with pytest.raises(ValueError):
        organize_files(fake_path, config)

# Verify that a file with an unmatched extension should not be moved
def test_organize_files_unmatched():
    with tempfile.TemporaryDirectory() as temp_dir:
        base = Path(temp_dir)
        file = base / "file.xyz"
        file.write_text("unknown extension")

        config = {
            "rules": {
                "images": [".jpg", ".png"]
            }
        }

        organize_files(base, config)

        # No matching rule, file should not be moved
        assert file.exists()
