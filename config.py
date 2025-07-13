import json
def load_config(config_path):
    try:
        with open(config_path,"r",encoding="utf-8") as f:
            config=json.load(f)#读取配置文件
        return config
    except Exception as e:
        raise RuntimeError(f"配置文件加载失败：{e}")    