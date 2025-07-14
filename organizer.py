import shutil
from pathlib import Path
from rules import match_category
def organize_files(folder:Path,config:dict):
    rules=config.get("rules",{})#读取分类规则
    if not folder.exists() or not folder.is_dir():
        raise ValueError(f"目标文件夹不存在或不是一个目录：{folder}")#判断是否为文件夹或目录
    for file in folder.iterdir():#遍历文件夹
        if file.is_file():
            category = match_category(file, rules)#判断类型
            
            if category:
                    target_dir=folder/category#目标文件路径
                    target_dir.mkdir(exist_ok=True)#不存在就创建
                    shutil.move(str(file),str(target_dir/file.name))#移动文件
                    print(f"已将文件{file.name}移动到{category}/")
                    break
            else:
                print(f"未找到匹配分类：{file.name}") #如果没有匹配任何分类   
