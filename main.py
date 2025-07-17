from pathlib import Path
from config import load_config
from organizer import organize_files# Import required modules
def main():
    config_path=Path("config.json")
    target_folder=Path("sample_folder")
    try:
        config=load_config(config_path)# Load configuration file
    except Exception as e: 
        print(f"Configuration loading failed:{e}")   
        return
    try:
        organize_files(target_folder,config)# Organize target folder
    except Exception as e:
        print(f"Failed to organize files:{e}")
        return
    print("Finished")
if __name__=="__main__":# Entry point of the program
    main()