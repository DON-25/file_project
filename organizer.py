import shutil
from pathlib import Path
from rules import match_category
def organize_files(folder:Path,config:dict):
    rules=config.get("rules",{})#Load classification rules
    if not folder.exists() or not folder.is_dir():
        raise ValueError(f"Target folder does not exist or is not a directory: {folder}")# Check if path is valid
    for file in folder.iterdir():#Iterate over folder contents
        if file.is_file():
            category = match_category(file, rules)# Determine file category
            
            if category:
                    target_dir=folder/category#Construct target path
                    target_dir.mkdir(exist_ok=True)#Create directory if it doesn't exist
                    shutil.move(str(file),str(target_dir/file.name))# Move file to target directory
                    print(f"Moved file{file.name}to{category}/")
            else:
                print(f"No matching category found for{file.name}") #No matching rule   
