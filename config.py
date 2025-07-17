import json
def load_config(config_path):
    try:
        with open(config_path,"r",encoding="utf-8") as f:
            config=json.load(f)#Read configuration file
        return config
    except Exception as e:
        raise RuntimeError(f"Failed to load configuration file:{e}")