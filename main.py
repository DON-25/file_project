from pathlib import Path
from config import load_config
from organizer import organize_files#导入模块
def main():
    config_path=Path("config.json")
    target_folder=Path("sample_folder")
    try:
        config=load_config(config_path)#加载配置文件
    except Exception as e: 
        print(f"配置加载失败：{e}")   
        return
    try:
        organize_files(target_folder,config)#整理文件夹
    except Exception as e:
        print(f"整理失败：{e}")
        return
    print("整理完成")
if __name__=="__main__":#启动程序
    main()