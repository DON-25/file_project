#文件分类规则逻辑
from pathlib import Path
from typing import Optional
def match_category(file: Path, rules: dict) -> Optional[str]:
    suffix = file.suffix.lower()
    for category,extensions in rules.items():
         if suffix in extensions:
            return category
    return None
